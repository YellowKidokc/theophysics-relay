# theophysics-relay — Build Specification
## The Universal Access Layer for the Theophysics AI Crew

**Author:** David Lowe (POF 2828) + Claude Opus 4.6
**Date:** November 24, 2026
**Repo name:** `theophysics-relay`
**Purpose:** One API, one URL, any AI, anywhere. Universal file access, shared memory, crew messaging, search, scheduling, and corpus audit — accessible from any sandbox through a Cloudflare Worker and tunnel to the NAS.

---

## Architecture

```
Any AI (Claude, GPT, Gemini, Kimi, Codex)
         ↓ HTTPS
relay.faiththruphysics.com (Cloudflare Worker)
         ↓ Cloudflare Tunnel (existing on NAS)
Relay Service (FastAPI on NAS or desktop)
         ↓
┌────────────────────────────────────────────┐
│  NAS (192.168.2.50)                        │
│  ├── Vault / Obsidian                      │
│  ├── .APICALLS stations                    │
│  ├── Memory store (markdown + Postgres)    │
│  └── File access to all shares             │
├────────────────────────────────────────────┤
│  Desktop (hp)                              │
│  ├── C:\_RELAY (INBOX/OUTBOX/MESSAGES)     │
│  ├── D:\_RELAY (same)                      │
│  ├── Drive Brain (:28280)                  │
│  ├── Local RAG / ChromaDB (:9000)          │
│  ├── Ollama (:11434)                       │
│  ├── Postgres (:2665 on 192.168.1.177)     │
│  └── MCP notification listener             │
├────────────────────────────────────────────┤
│  Laptop                                    │
│  └── Top of Mind (OpenCovibe) — receives   │
│      all messages, David's single hub      │
└────────────────────────────────────────────┘
```

---

## Unified API Contract

One endpoint. One shape. The `action` field tells it what to do.

```
POST https://relay.faiththruphysics.com/v1
Content-Type: application/json
```

### Authentication
Every call carries an API key. One key per AI identity.
Keys stored in Cloudflare Worker secrets. Revocable instantly.

```json
{
  "key": "claude-opus-abc123",
  "action": "<action>",
  ...action-specific fields
}
```

### Response envelope
```json
{
  "status": "ok" | "error",
  "data": { ... },
  "receipt": {
    "timestamp": "ISO-8601",
    "who": "claude-opus",
    "action": "file.get",
    "session_id": "optional"
  }
}
```

---

## Actions

### 1. memory — Shared persistent notes
```json
{"action": "memory", "op": "read",   "path": "/crew/decisions/2026-11-24.md"}
{"action": "memory", "op": "write",  "path": "/crew/claude/notes.md", "content": "..."}
{"action": "memory", "op": "append", "path": "/crew/log.md", "content": "New entry..."}
{"action": "memory", "op": "list",   "prefix": "/crew/"}
{"action": "memory", "op": "search", "query": "is-ought gap"}
```
Storage: markdown files on NAS under a `_MEMORY/` folder. Postgres indexes for search.

### 2. message — Send to David's Top of Mind
```json
{"action": "message", "to": "david", "text": "Research done. 47 sources found."}
{"action": "message", "to": "david", "priority": "high", "text": "Found an error in Paper 7."}
```
Lands in Top of Mind inbox. Priority "high" triggers desktop notification.

### 3. file — Get/return files from anywhere
```json
{"action": "file", "op": "get",    "path": "\\\\192.168.2.50\\h_hp\\Obsidian\\.APICALLS\\03_CHAPEL\\..."}
{"action": "file", "op": "return", "path": "same path", "content": "...modified..."}
{"action": "file", "op": "list",   "path": "\\\\192.168.2.50\\h_hp\\Obsidian\\", "depth": 1}
{"action": "file", "op": "status"}
```
File checkout tracking: who has what, when checked out, auto-return after configurable timer (default 5 min). `status` shows all checked-out files.

### 4. board — Crew comms
```json
{"action": "board", "op": "post",   "room": "all",    "text": "CHAPEL build complete."}
{"action": "board", "op": "post",   "room": "claude",  "text": "Private note to Claude."}
{"action": "board", "op": "read",   "room": "all",    "limit": 20}
{"action": "board", "op": "unread"}
```
Rooms: `all`, `claude`, `gpt`, `gemini`, `kimi`, `codex`, `david`, or any custom room name.

### 5. search — Query Drive Brain registries
```json
{"action": "search", "query": "is-ought", "doc_type": "", "limit": 50}
{"action": "search", "query": "Master Equation", "brain_id": "BRN-specific-drive"}
```
Searches across all registered drives (C:, D:, NAS).

### 6. done — Session sign-off
```json
{"action": "done", "summary": "Reviewed 3 papers, found 2 issues, posted to board."}
```
Logs the session summary. Updates crew status board.

### 7. vector — Semantic search (ChromaDB / local-rag)
```json
{"action": "vector", "query": "quantum error correction redemption", "limit": 10}
{"action": "vector", "op": "index", "path": "\\\\192.168.2.50\\h_hp\\Obsidian\\..."}
```
Wraps local-rag API on port 9000.

### 8. postgres — Direct database query
```json
{"action": "postgres", "db": "kj", "query": "SELECT * FROM axioms WHERE domain='physics' LIMIT 10"}
{"action": "postgres", "db": "crawlab_data", "query": "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"}
```
Read-only by default. Write requires explicit flag.

### 9. wake — Notify/wake desktop AIs
```json
{"action": "wake", "target": "all", "text": "New assignment ready."}
{"action": "wake", "target": "claude", "text": "David needs you on the is-ought paper."}
```
Triggers MCP notification listener on desktop. Each AI session can opt in/ignore.

### 10. schedule — Timed messages and jobs
```json
{"action": "schedule", "op": "add", "cron": "0 0 * * *", "payload": {"action": "board", "op": "post", "room": "all", "text": "Daily: compress yesterday's messages before starting work."}}
{"action": "schedule", "op": "add", "at": "2026-11-25T06:00:00", "payload": {"action": "message", "to": "david", "text": "Morning briefing ready."}}
{"action": "schedule", "op": "list"}
{"action": "schedule", "op": "remove", "id": "sched-abc123"}
```
Cron or one-shot. Payload is any valid relay action. Daily→weekly→monthly compression built in.

### 11. audit — Corpus rotation / paper review queue
```json
{"action": "audit", "op": "assign", "series": "ONE_STORY", "papers": ["AX_GI_01", "AX_GI_02", ...]}
{"action": "audit", "op": "next"}
{"action": "audit", "op": "submit", "paper_id": "AX_GI_07", "findings": "...1-2 page audit..."}
{"action": "audit", "op": "status", "series": "ONE_STORY"}
```
David feeds a series in. Each AI calls `next` to get assigned a paper. Reads it. Writes findings. All findings collected per paper. Parallel across 5-6 AIs.

### 12. orient — Get full context on boot
```json
{"action": "orient"}
```
Returns: who David is (1 paragraph), project summary, active work, crew status, what's running, where everything is, links to AI-CREW orientation docs. One call, full context for a cold-start AI.

---

## Existing Code to Pull In

| File/Folder | Current Location | What It Does |
|---|---|---|
| `relay.py` | `\\192.168.2.50\h_hp\Obsidian\.APICALLS\_engine\relay.py` | API call passthrough (DeepSeek/OpenRouter) with receipts |
| `paths.py` | same `_engine/` folder | Path resolution |
| `naming.py` | same | Naming conventions |
| `config/paths.json` | same | Path config |
| `config/keys.txt` | same (not committed) | API keys |
| `brain_server.py` | `D:\GitHub\pipeline-workflows\FAST API\brain_server.py` | Drive Brain — discovery, search, scan, dashboard (port 28280) |
| `config.json` | same folder | Drive Brain config (NAS roots, FIS dir) |
| `PORTS.json` | same folder | Locked port registry (23 services) |
| `connect.py` + `.env` | `D:\GitHub\POSTGRES_WORKSPACE\` | Postgres connection (192.168.1.177:2665) |
| `local-rag/` | `D:\GitHub\local-rag\` | Full RAG system — FastAPI + ChromaDB + file watcher (port 9000) |
| `FolderWatcher.py` | `D:\GitHub\pipeline-workflows\AUTOFOLDER\channel_watchers\` | Folder watch daemon |
| `relay_deployed_configs/` | `AUTOFOLDER\` | YAML configs for relay channels |
| `router_station/` | `AUTOFOLDER\` | Route + deploy scripts |
| `AI-CREW/` | `D:\GitHub\AI-CREW\` | Crew orientation, charter, protocols, handoffs (REFERENCE — not duplicated, served via orient endpoint) |
| `crew-comms/` | `D:\GitHub\crew-comms\` | Crew communication system |

---

## New Code to Build

### 1. Cloudflare Worker (`worker/`)
- `relay.faiththruphysics.com`
- Validates API key from Worker secrets
- Routes to NAS relay service through existing Cloudflare tunnel
- ~150 lines
- Rate limiting per key
- Request/response logging

### 2. Relay Service (`service/`)
- FastAPI app that handles all 12 actions
- Runs on NAS behind the tunnel
- Extends brain_server.py pattern
- Port: pick from PORTS.json open slots (suggest 28295)
- Imports existing relay.py, connect.py, wraps local-rag API

### 3. Memory Service (`service/memory/`)
- Markdown files under `_MEMORY/` on NAS
- JSON index for fast listing
- Postgres table for full-text search
- Revision tracking (who wrote what, when)

### 4. File Checkout Tracker (`service/files/`)
- SQLite table: path, checked_out_by, checked_out_at, auto_return_minutes
- Watcher thread returns files after timer
- Conflict detection (two AIs want same file)

### 5. Scheduler (`service/scheduler/`)
- Cron parser + one-shot timer
- Stores scheduled jobs in SQLite
- Fires relay actions at scheduled times
- Daily→weekly→monthly message compression

### 6. Audit Queue (`service/audit/`)
- Paper assignment queue per series
- Round-robin across available AIs
- Collects findings per paper
- Status dashboard

### 7. Wake/Notification Bridge (`service/wake/`)
- Posts to MCP notification endpoint on desktop
- Each AI session subscribes via WebSocket or polling
- Opt-in per session

### 8. _RELAY Folder Setup (`setup/`)
- Creates `C:\_RELAY\` and `D:\_RELAY\` with:
  - `INBOX/` — files dropped here get processed
  - `OUTBOX/` — results land here
  - `MESSAGES/` — crew messages
  - `ORIENTATION.md` — auto-generated from PORTS.json + brain discovery
- Folder watcher ties to relay service

### 9. Orientation Generator (`service/orient/`)
- Reads PORTS.json, brain discovery, AI-CREW orientation docs
- Generates context packet for cold-start AIs
- Updated on each `orient` call

---

## Port Assignment
Add to PORTS.json:
```json
{"port": 28295, "name": "Theophysics Relay", "status": "planned", "host": "0.0.0.0"}
```

---

## Build Order

1. **Relay service skeleton** — FastAPI with orient + search + file actions working locally
2. **Memory service** — markdown CRUD + Postgres index
3. **Board integration** — connect to crew-comms
4. **Cloudflare Worker + tunnel** — external access working
5. **File checkout tracker** — auto-return timer
6. **Scheduler** — cron + one-shot
7. **Audit queue** — corpus rotation
8. **Wake bridge** — desktop notifications
9. **_RELAY folder setup** — C: and D: relay points
10. **Vector search wrapper** — local-rag integration

---

## Rules

- Read-only by default for file and postgres actions. Write requires explicit flag.
- No AI ever moves, renames, or rearranges David's original documents.
- All scripts portable — work from any location after a GitHub download.
- Every action is logged with receipt (who, what, when).
- API keys are per-AI, stored in Worker secrets, revocable instantly.
- File checkouts auto-return. No permanent locks.
- Orientation is auto-generated, never hand-maintained.
- Dark-themed dashboard if one is built.

---

## Dependencies

- Python 3.12+
- FastAPI + uvicorn
- psycopg2-binary (Postgres)
- chromadb (vector search, via local-rag)
- watchdog (file watching)
- Cloudflare Wrangler (Worker deployment)
- cloudflared (tunnel — already on NAS)

---

## Related Repos (not duplicated, referenced)

- `AI-CREW` — crew orientation, charter, protocols
- `crew-comms` — crew messaging system
- `pipeline-workflows` — APICALLS stations, AUTOFOLDER, Drive Brain
- `local-rag` — vector search / ChromaDB
- `POSTGRES_WORKSPACE` — database connection
- `OpenCovibe` → Top of Mind (separate repo, receives messages from relay)
