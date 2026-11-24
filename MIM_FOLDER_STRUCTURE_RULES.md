# Math Is Moral folder structure rules

MIM-specific rules from David's direction, 2026-11-24. The relay repository holds the governing document. Other locations should link here. This defines the target layout for the folder-by-folder pass. Proposed names and open choices are marked below. It does not record a completed migration.

The earlier God IS layout in the [naming reference](NAMING_AND_STRUCTURE_REFERENCE.md) describes a different working design. Apply the MIM rules here to MIM. Do not treat either layout as automatically adopted for another series.

## Frontside and Backside

Obsidian is the Frontside. The Frontside is for the papers and the material a person can read and navigate in Obsidian as-is. Keep CSV, Excel, JSON, raw API files, execution data, and other formats that need extra machinery on the Backside. Do not add a plugin or force a format into the Frontside just to make a machine artifact visible. If a reader needs its result, write a readable Markdown summary and link to the source.

Use one series Backside at `00_MIM_SERIES/.BACKSIDE`. Organize its contents by paper ID and purpose so the machine files, media, and receipts can still be traced to the paper that owns them. A paper folder does not need a second Backside just to explain where a file went. For example, MIM.00 currently has a local Backside containing a move receipt. Retain that receipt in the series Backside with its paper association. Put a useful link in the paper's readable navigation if the reader needs it.

Keep media on the series Backside. This includes images, WebP, folder pictures, NotebookLM visual PDFs, and other media. Obsidian notes should link to the asset and embed it where the format supports embedding. Check that the link or embed still works after relocation. The PDF example here is a NotebookLM visual export. Classify an ordinary research PDF by its role as a source and link to it from the Research Dossier.

## Paper folder layout

| Where | What belongs there |
|---|---|
| Paper root | Main readable manuscript under its established paper ID. Keep intentional short and long readings visibly labeled and linked. Do not assume a missing long version is a duplicate, a draft, or absent from the wider series. |
| `00_PLEASE_READ_ME.md` | What the reader needs to know about this folder and paper, including local exceptions or open issues that matter to the reader. |
| `00_FOLDER_ORIENTATION.md` | Proposed filename for the folder index. Describe the folder's purpose and link to its files, child folders, and parent. At the series root, explain the whole layout and link to each paper and series category. |
| `RD/` | **Research Dossier.** Use the uppercase folder name `RD` in place of `research`. Keep readable research records and source links here. Store raw machine files and media on the series Backside. |
| `Operators/` | Replace the role of `Operator Visuals` with an Operators folder. Keep `Operators.md` and reader-facing operator notes here. Link or embed the visuals from the Backside. |
| `Tangents/` | Readable companion branches with links to the paper or claim they extend. |
| `Drafts/` | Working copies and revisions. Keep the selected main paper at the root. Identify unresolved edition choices before relabeling a manuscript as a draft. |
| `AI/` | Proposed home for readable AI notepads and review notes. Keep raw API outputs and machine receipts on the series Backside. Confirm the final name against the existing review structure during the first paper pass. |
| `Info HTML/` | Optional, proposed name. Create only when a particular folder needs a dedicated HTML view because of size, classification, or unusual contents. Review unused instances when moving into the HTML phase and remove ones with no material to preserve or links to update. |

Keep other material in a folder that describes its role. Use existing series categories where they fit. When a file's role is unclear, record the question and preserve the file for review. A folder should earn its place by giving the reader or the workflow somewhere specific to go.

## Research Dossier source folders

Use four immediate folders under each paper's RD as the starting layout:

- **YT** for video source notes, timecoded references, and transcripts used in the paper.
- **Web** for websites, articles, and other online sources without a better fit.
- **Our Work** (proposed name) for links to David's related papers, notes, and prior work. Link to the existing record in place.
- **Formal Papers** for outside scholarly papers and formal research reports. Keep the full citation, a DOI or stable link when available, and the page or section that supports the claim. Cite that record from the manuscript so the reader can trace it to the source.

Keep source notes directly inside these folders. Use links, filenames, or metadata for topic, provenance, alternate versions, and review status. Avoid a third folder level for transcript archives and variants. Add an empty source folder when it clarifies where future material belongs. Revisit unused folders after the first pass. Keep raw exports and media on the series Backside under the existing rules.

## Navigation and linking

The folder tree is the primary way to browse. Open a paper folder or the series hub and see its useful groups immediately. Orientation notes and links can explain a folder and point to related records. They are shortcuts, never additional steps required to find a file. Use permanent paper addresses and EZRA record IDs where available. Check Obsidian links and embeds when files move.

## Keep the folder tree shallow

Use at most two folder levels below the series hub or an individual paper folder in the human-facing layout. Count the first category as level one and its immediate subcategories as level two. Put the files at that second level. Skip an intermediate folder when it only leads to one file or repeats a label. Forty useful sibling folders are acceptable. Keep existing machine paths that require deeper structure visible as exceptions to discuss before changing them.

## Proposed consolidation for discussion

Put the papers' review categories together under one top-level group, provisionally named **CHAPEL**. Keep the categories side by side inside it and put the readable files directly in those categories. Keep record types distinct so reports still know whether a record is a claim, a derivation, an evidence item, or a falsification condition.

```text
00_MIM_SERIES/
  CHAPEL/
    Claims/
    Hypotheses/
    Proof and Lean/
    Evidence/
    Falsification/
```

The live categories include `23_CLAIMS_ATOMS`, `04_HYPOTHESIS`, `24_PROOFS_LEAN`, `05_EVIDENCE`, and `06_FALSIFICATION`. The proposal groups their reader-facing material. Inside Proof and Lean, distinguish a written derivation from a checked result. Raw runs and machine receipts follow the series Backside rule. Confirm what “Lean forward” refers to before assigning any additional folder. Discuss whether dependencies, objections, and ORBITS should join CHAPEL or stay visible as separate siblings.

Routine fixes to labels and links can be made while working. Discuss category mergers, changes to governing locations, and treatment of disputed material before applying them. Inventory existing files and links first, including repeated index and routing filenames, so a merger cannot overwrite a unique record.

## HTML view rules

The legacy `analysis_<paper-id>.html` and `card_<paper-id>.html` exports are candidates for removal throughout the MIM series. The two MIM.00 examples are `analysis_MIM.00.MEPHISTO.html` and `card_MIM.00.MEPHISTO.html`. The replacement workflow is in `pipeline-workflows/FOLDER_SNAPSHOT/MIM_FOLDER_CONTROL`. Check legacy files against the current workflow and preserve any unique notes or data before removing the superseded copies. An intentional folder-level view in `Info HTML/` is a separate case.

## Folder-by-folder pass

1. Start with MIM.00 and use the result to check the naming and navigation rules. Then work through MIM.01 to MIM.20 in order.
2. Inventory the manuscript, editions, drafts, research, operators, tangents, AI notes, media, machine artifacts, and legacy HTML for that paper. Identify anything that needs a ruling.
3. Route each item by its role, preserve source IDs and move receipts, and update the folder orientation.
4. Open the paper, follow links up and down the tree, and test representative media embeds before closing the paper's pass.
5. Scan the series after the pass. List superseded cards, unused optional folders, unresolved manuscripts, and unclassified material separately so cleanup can be reviewed against what is actually there.

This is the rules document for the next pass. The folder-by-folder changes and removal of superseded files are pending.

## Change log and diffs

Use the existing series `37_CHANGE_LOG` as the proposed home for readable change history. A diff shows exactly what changed between two versions. Red marks removed lines and green marks added lines. For a meaningful change, record a short summary of what changed and why, who changed it, and the before and after references. Link to the exact diff or show it in a Markdown diff block. Keep raw patch files and machine-generated receipts on the series Backside. Keep draft manuscripts in their paper's Drafts folder.


For meaningful changes, put the contributor record at the bottom of the diff or change note. See [Contributor credit and first entries](CONTRIBUTOR_CREDIT.md) for the introduction, credit threshold, and fields.

## Numbering inside a paper folder

Keep the paper's permanent `SERIES.POSITION.SLUG` address. The numbers below organize the contents of that paper folder.

| Number | What it means |
| --- | --- |
| 00 | Main paper, visible at the top. |
| 01–09 | Drafts in order, kept in `Drafts`. |
| 10–89 | Working material such as research, YouTube evaluations, and readable summaries of API results. |
| 90–98 | Reserved slots for harvests, companions, or other specifically designated material. |
| 99 | Final working version of the paper. |
| 999 | Definitive final edition. Record whether it has been published and link to the published copy if it has. |

Within 10–89, use the number for ordering and a plain name for purpose. Keep research in `RD` with `YT`, `Web`, `Our Work`, and `Formal Papers` immediately under it. For example, `RD/YT/23_youtube_eval.md` is a readable evaluation. Put raw API responses and machine receipts on the series Backside and link to them from the readable summary when needed. Use a subfolder only if it helps the reader find material. Keep the two-level limit below each paper root.

Put this numbering key in each paper's Please Read Me and show its actual layout in its Folder Navigation note as that folder is organized. Use the existing order and edition evidence when assigning numbers to existing files. A known final paper can be recorded as such without reconstructing every old draft. The number records its role and does not itself establish a publication date.



## Expandable item codes and permanent links

The 10?89 range identifies working slots. Do not allocate one of the 80 slots to every transcript or run, and do not spill into another category when a collection grows. Use a slot plus an item-kind letter and a stable sequence. In the proposed YouTube example, `23T-00001` is a transcript and `23E-00001` is an evaluation. The slot number and letter assignments in this example are proposals, not a universal category registry. Keep research files flat under `RD/YT` and keep review status in the record rather than renaming whenever status changes.

| View | Example |
| --- | --- |
| Local label | `23T-00001` |
| Qualified label across papers | `MIM.06.ACTS::23T-00001` |
| Durable target for either label | `tp://<record-id>` |

Use one EZRA ID for the same record. Treat the qualified label as a display reference. Keep the existing document and artifact validators as their own contracts until an extension is approved and implemented. Before bulk changes, save an original link, rename a scratch fixture, rescan, and verify the old link resolves to the renamed file. Check ordinary Markdown and Obsidian path links separately. Keep a receipt and revision or hash for checks tied to exact content.

The scratch trial found 22,226 visible Markdown files under MIM.06's YouTube tree. Flat basename-only naming produced 8,966 competing paths, and unique 10?89 numbering could not cover the collection. The trial proved a collision-free scratch filename mapping, not uniqueness of sources or a completed migration. Use explicit navigation ordering for 99 and 999 rather than relying on filename sorting.

## Templates and Folder Maker

Keep the reusable template catalog and Python Folder Maker in David-OSv3 under `apps/folder-cleanup/.BACKSIDE/template_maker/`. A readable form defines the expected content. The maker reads the layout and creates folders and forms. Keep raw API results and execution receipts on the series Backside. Keep local copies of rules to links only. Scripts using rules from the relay should record the exact commit used for a run.

## Series main page

Feature the papers directly. Provide **AI**, **Diff**, and **Acknowledgments** in that order. AI links to crew openings and the working rules. Diff records meaningful structural decisions with the reason and any useful comparison. Acknowledgments gives credit for substantive contributions and can link to the credit block at the bottom of the relevant change. Keep working material in plainly named folders.
