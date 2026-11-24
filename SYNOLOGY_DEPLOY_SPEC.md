# Synology Deployment Spec — David-OS v3
**Date:** 2026-11-24

---

## One VM, One Server, All AIs

One Docker container on the Synology NAS (192.168.2.50). Every AI talks to the same
FastAPI endpoints. The VM doesn't care who's calling — Claude, Codex, GPT, Gemini, Kimi
all hit the same API. Session ID tracks who made each call.

## What the NAS package contains

```
DAVID_OS_DEPLOY/
├── 00_AI_README.md          ← orientation for any AI
├── DEPLOY_SPEC.md           ← full deployment instructions
├── pyproject.toml           ← Python project config
├── main.py                  ← FastAPI server (10 endpoints)
├── apps/
│   ├── sort/                ← SORT lane (Claude)
│   ├── classify/            ← CLASSIFY lane (Codex)
│   └── verify/              ← VERIFY lane (GPT)
├── engine/                  ← shared core (~40 modules)
├── shared/                  ← contracts, identity, taxonomy
└── rule_brick/              ← 26+ rules as executable checks
```

## The three systems in one package

### 1. FastAPI Server (the brain)
10 numbered endpoints:

| # | Endpoint | What |
|---|----------|------|
| 1 | `/scan` | Profile one file |
| 2 | `/rules` | Run R01-R26+ against a profile |
| 3 | `/match` | Compare one file against corpus index |
| 4 | `/route` | Full pipeline: scan → rules → match → decision |
| 5 | `/batch` | Route a folder (all files, one at a time) |
| 6 | `/escalate` | Jeb → DeepSeek → HOLD chain |
| 7 | `/verify` | Pre/post gate matrix |
| 8 | `/index` | Build or update corpus index |
| 9 | `/receipt` | Read/write lane receipts |
| 10 | `/status` | Pipeline status, queue, anomaly count |

### 2. Drive Harvester (the reach)
Can access any mounted drive:
- All NAS shares (Obsidian, Documents, Desktop, etc.)
- D:\ on desktop (via SMB mount)
- C:\ on desktop (via SMB mount)
- GitHub repos (cloned or pulled)

The corpus index covers everything the harvester can reach.
If a drive isn't mounted, it logs it and moves on.

### 3. API Relay (the multiplier)
Routes calls to external AI services:
- DeepSeek (escalation, cheap binary calls)
- Ollama (local reasoning, pre-flight checks)
- OpenRouter (if needed)
- Up to 30 concurrent calls (David's standing rule)

The relay handles the Jeb → DeepSeek escalation chain.
Binary calls go to the cheapest model. Reasoning goes to DeepSeek.
Unresolved goes to HOLD for a crew AI or David.

## Docker setup

**Image:** `python:3.12-slim`

**Volume mounts:**
```
/app              → /volume1/homes/h_hp/02_OPERATING_SYSTEM/DAVID_OS_DEPLOY
/data/obsidian    → /volume1/homes/h_hp/Obsidian
/data/b_series    → /volume1/homes/h_hp/Documents/B_series
/data/templates   → /volume1/homes/h_hp/Obsidian/.APICALLS/.Templates
/data/desktop     → /volume1/homes/h_hp/Desktop
```

**Port:** 8100

**Restart policy:** always

**Environment:**
```
DEEPSEEK_API_KEY=<key>
OLLAMA_HOST=http://192.168.2.50:11434
CORPUS_INDEX=/app/data/corpus_index.sqlite
```

## Why one VM

Every AI talks to the same endpoints. The pipeline is shared infrastructure:
- Same rules (R01-R26+)
- Same corpus index
- Same gate matrix
- Same receipts

You'd only need a second VM for a staging environment to test rule changes
before they go live. That's later. For now: one VM, all AIs, one pipeline.

## NAS location

`\\192.168.2.50\h_hp\02_OPERATING_SYSTEM\DAVID_OS_DEPLOY\`

This is the canonical deployment. GitHub has the source. The NAS has the running copy.
