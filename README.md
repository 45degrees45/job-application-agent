# Job Application Agent

Self-improving job application automation for Joseph T C.

This project is scoped for `n8n + Gemini + GroqCloud + Google Workspace` and is intentionally split into:

- `V1`: buildable in 1-2 hours
- `V2`: adds scoring, learning, and feedback injection

## Goal

Input:

- Job URL
- Raw job description

Output:

- Tailored resume
- Tailored cover letter
- Tailored email draft
- Optional Gmail send

Learning loop:

- Store generated output
- Store Joseph's edited version
- Extract diffs and patterns
- Reuse style learnings in future generations

## Project Files

- `docs/system-design.md`: V1 and V2 architecture
- `docs/prompts.md`: prompts for generation, scoring, and learning
- `docs/reuse-map.md`: what was pulled from older projects
- `data/joseph_profile.seed.json`: Joseph profile seed adapted from earlier project patterns
- `schemas/learnings.schema.json`: memory payload structure
- `utils/google_auth.py`: shared Google auth helper
- `utils/sheets_store.py`: shared Sheets adapter
- `CLAUDE.md`: project-specific implementation rules

## Recommended V1 Stack

- `n8n`
- `GroqCloud` for scoring
- `Gemini` for generation
- `Google Sheets`
- `Google Docs` or markdown/text output
- `Telegram` or `n8n Form` for review

## Build Order

1. Implement input capture.
2. Generate fit score, resume, cover letter, and email.
3. Save outputs to Google Sheets.
4. Send review copy to Telegram or a simple UI.
5. Capture Joseph's final edits manually in V1.
6. Add automated learning extraction in V2.
