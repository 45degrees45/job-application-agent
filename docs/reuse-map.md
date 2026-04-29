# Reuse Map

This project now reuses concrete patterns from older local projects instead of inventing new ones.

## Reused Sources

### `applypilot`

Source:

- `/home/jo/claude_projects/applypilot/profile.example.json`

Reused idea:

- Structured job-application profile shape
- Clear split between personal info, work authorization, availability, compensation, and resume facts

Used here:

- `data/joseph_profile.seed.json`

### `pricewise`

Sources:

- `/home/jo/claude_projects/pricewise/google_auth.py`
- `/home/jo/claude_projects/pricewise/sheets.py`
- `/home/jo/claude_projects/pricewise/bot.py`

Reused ideas:

- Service-account auth via env JSON
- Minimal gspread client wrapper
- Practical Telegram review/confirmation flow pattern

Used here:

- `utils/google_auth.py`
- `utils/sheets_store.py`
- Telegram review flow design in `docs/system-design.md`

### `closewise`

Source:

- `/home/jo/claude_projects/closewise/sheets.py`

Reused idea:

- Keep Google Sheets access isolated behind one module
- Return plain dict/list payloads so the rest of the system is sheet-agnostic

Used here:

- `utils/sheets_store.py`

### `homeo-clinic-management`

Source:

- `/home/jo/claude_projects/homeo-clinic-management/clinic_bot/sheets_sync.py`

Reused idea:

- Clean worksheet initialization pattern
- Worksheet creation on first run

Used here:

- `utils/sheets_store.py`

## Practical Decision

The n8n workflow remains the main orchestrator.

These helper modules exist for:

- local testing
- fallback scripts
- future webhook/API wrappers
- keeping sheet/profile logic out of the workflow JSON

