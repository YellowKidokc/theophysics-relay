"""
gemini_deep_research_runner.py
Automated Gemini Deep Research batch runner using Playwright.

SETUP:
    pip install playwright
    playwright install chromium

USAGE:
    1. Put your prompts in a folder as numbered .txt files:
       prompts/01_consciousness.txt
       prompts/02_moral_realism.txt

    2. Run:
       python gemini_deep_research_runner.py --prompts ./prompts --output ./results

    3. First run: browser opens visible so you can sign into Google.
       After that, it reuses your session (--profile flag).

    4. Results land in ./results/01_consciousness/ etc.

FLAGS:
    --prompts     Folder with numbered .txt prompt files (required)
    --output      Where results go (default: ./results)
    --wait        Minutes to wait for each deep research to finish (default: 12)
    --profile     Browser profile folder for persistent login (default: ./gemini_profile)
    --headless    Run headless after first login (flag, no value)
"""
import argparse
import os
import sys
import time
import glob
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Install playwright first:")
    print("  pip install playwright")
    print("  playwright install chromium")
    sys.exit(1)


def get_prompts(prompts_dir):
    """Read all .txt files from prompts folder, sorted by name."""
    files = sorted(glob.glob(os.path.join(prompts_dir, "*.txt")))
    prompts = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            text = fh.read().strip()
        name = Path(f).stem
        prompts.append({"name": name, "text": text, "file": f})
    return prompts


def wait_for_research_complete(page, timeout_minutes=12):
    """
    Poll the page until deep research results appear.
    Gemini shows a specific container when research is done.
    Adjust selectors if Gemini's UI changes.
    """
    timeout_ms = timeout_minutes * 60 * 1000
    start = time.time()
    poll_interval = 15  # seconds

    print(f"    Waiting up to {timeout_minutes} min for research to complete...")

    while (time.time() - start) < (timeout_minutes * 60):
        # Check for the research complete indicators
        # These selectors may need updating as Gemini changes
        try:
            # Look for the "Research complete" or results container
            # Gemini typically shows a report card when done
            done_indicators = [
                'text="Research complete"',
                'text="View research report"',
                '[data-test-id="research-complete"]',
                'text="Deep research complete"',
            ]
            for selector in done_indicators:
                if page.locator(selector).count() > 0:
                    print(f"    Research complete! ({int(time.time() - start)}s)")
                    return True

            # Also check if the response has stopped streaming
            # (the thinking indicator disappears)
            thinking = page.locator('[data-test-id="thinking-indicator"]')
            if thinking.count() == 0:
                # No thinking indicator - check if there's actual content
                response_blocks = page.locator('.response-container, .model-response')
                if response_blocks.count() > 0:
                    # Wait a few more seconds to make sure it's really done
                    time.sleep(5)
                    if thinking.count() == 0:
                        print(f"    Response appears complete ({int(time.time() - start)}s)")
                        return True

        except Exception:
            pass

        elapsed = int(time.time() - start)
        print(f"    Still working... ({elapsed}s / {timeout_minutes * 60}s)")
        time.sleep(poll_interval)

    print(f"    WARNING: Timed out after {timeout_minutes} minutes")
    return False


def download_result(page, output_dir, prompt_name):
    """
    Try to download/copy the research result.
    Falls back to copying the page text if download isn't available.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Strategy 1: Try the share/export button
    try:
        share_btn = page.locator('button:has-text("Share"), button:has-text("Export")')
        if share_btn.count() > 0:
            share_btn.first.click()
            time.sleep(2)

            # Look for "Copy" or "Download" in the share menu
            copy_btn = page.locator('text="Copy to clipboard", text="Copy"')
            if copy_btn.count() > 0:
                copy_btn.first.click()
                time.sleep(1)
                # Get from clipboard
                content = page.evaluate("navigator.clipboard.readText()")
                if content:
                    filepath = os.path.join(output_dir, f"{prompt_name}.md")
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"    Saved via clipboard: {filepath}")
                    return True
    except Exception as e:
        print(f"    Share/export failed: {e}")

    # Strategy 2: Scrape the response text from the page
    try:
        # Get all response text from the page
        response_elements = page.locator(
            '.model-response-text, .response-container-content, '
            '.markdown-content, [data-message-author-role="model"]'
        )

        texts = []
        for i in range(response_elements.count()):
            text = response_elements.nth(i).inner_text()
            if text.strip():
                texts.append(text.strip())

        if texts:
            # Take the last response (the deep research result)
            content = texts[-1]
            filepath = os.path.join(output_dir, f"{prompt_name}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"    Saved via scrape: {filepath}")
            return True
    except Exception as e:
        print(f"    Scrape failed: {e}")

    # Strategy 3: Full page text as last resort
    try:
        content = page.inner_text("body")
        filepath = os.path.join(output_dir, f"{prompt_name}_full_page.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"    Saved full page text: {filepath}")
        return True
    except Exception as e:
        print(f"    Full page save failed: {e}")

    return False


def run_batch(prompts_dir, output_dir, wait_minutes, profile_dir, headless):
    prompts = get_prompts(prompts_dir)
    if not prompts:
        print(f"No .txt files found in {prompts_dir}")
        return

    print(f"Found {len(prompts)} prompts:")
    for p in prompts:
        print(f"  {p['name']}: {p['text'][:60]}...")
    print()

    with sync_playwright() as pw:
        # Use persistent context so Google login sticks
        browser = pw.chromium.launch_persistent_context(
            profile_dir,
            headless=headless,
            args=["--disable-blink-features=AutomationControlled"],
            viewport={"width": 1280, "height": 900},
        )

        page = browser.pages[0] if browser.pages else browser.new_page()

        for i, prompt in enumerate(prompts):
            print(f"\n{'='*60}")
            print(f"[{i+1}/{len(prompts)}] {prompt['name']}")
            print(f"{'='*60}")

            # Navigate to Gemini
            page.goto("https://gemini.google.com/app", wait_until="networkidle")
            time.sleep(3)

            # Check if we need to sign in
            if "accounts.google.com" in page.url:
                print("  Please sign into Google in the browser window.")
                print("  Waiting for you to complete sign-in...")
                page.wait_for_url("**/gemini.google.com/**", timeout=300000)
                print("  Sign-in complete!")
                time.sleep(2)

            # Find the input field and type the prompt
            # Gemini uses a contenteditable div or textarea
            input_selectors = [
                '[aria-label="Enter a prompt here"]',
                '.ql-editor',
                'div[contenteditable="true"]',
                'textarea',
            ]

            input_found = False
            for selector in input_selectors:
                try:
                    el = page.locator(selector).first
                    if el.is_visible():
                        el.click()
                        time.sleep(0.5)
                        # Type the prompt
                        page.keyboard.type(prompt["text"], delay=10)
                        input_found = True
                        break
                except Exception:
                    continue

            if not input_found:
                print("  ERROR: Could not find input field. Skipping.")
                continue

            time.sleep(1)

            # Submit - press Enter or click send button
            try:
                send_btn = page.locator('button[aria-label="Send message"]')
                if send_btn.count() > 0 and send_btn.first.is_enabled():
                    send_btn.first.click()
                else:
                    page.keyboard.press("Enter")
            except Exception:
                page.keyboard.press("Enter")

            print(f"  Prompt submitted. Waiting for deep research...")
            time.sleep(5)

            # Wait for research to complete
            success = wait_for_research_complete(page, wait_minutes)

            # Download the result
            prompt_output = os.path.join(output_dir, prompt["name"])
            downloaded = download_result(page, prompt_output, prompt["name"])

            if downloaded:
                print(f"  Result saved to {prompt_output}/")
            else:
                print(f"  WARNING: Could not save result for {prompt['name']}")

            # Small pause before next prompt
            if i < len(prompts) - 1:
                print(f"  Pausing 10s before next prompt...")
                time.sleep(10)

        print(f"\n{'='*60}")
        print(f"DONE. {len(prompts)} prompts processed.")
        print(f"Results in: {output_dir}")
        print(f"{'='*60}")

        browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gemini Deep Research batch runner")
    parser.add_argument("--prompts", required=True, help="Folder with .txt prompt files")
    parser.add_argument("--output", default="./results", help="Output folder")
    parser.add_argument("--wait", type=int, default=12, help="Minutes to wait per research")
    parser.add_argument("--profile", default="./gemini_profile", help="Browser profile dir")
    parser.add_argument("--headless", action="store_true", help="Run headless")

    args = parser.parse_args()
    run_batch(args.prompts, args.output, args.wait, args.profile, args.headless)
