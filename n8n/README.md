# n8n Workflow

## Files

- `job-application-agent-v1.json`: importable V1 workflow

## What This Workflow Does

1. Accepts `job_url` or pasted `job_description`
2. Fetches the page when a URL is provided
3. Cleans the posting text
4. Scores fit and selects the base profile
5. Skips jobs below score `7`
6. Generates:
   - tailored resume
   - cover letter
   - email subject/body
7. Returns a final payload plus a `ready_for_google_sheets` object

## Required Setup

In n8n, set:

- `GROQ_API_KEY`
- `GROQ_MODEL`
- `GEMINI_API_KEY`
- `GEMINI_MODEL`

Recommended split:

- `GROQ_MODEL=llama-3.3-70b-versatile`
- `GEMINI_MODEL=gemini-2.0-flash`

## First Run

1. Import `job-application-agent-v1.json`
2. Open `Set - Job Input`
3. Fill either:
   - `job_url`
   - or `job_description`
4. Set `company` and `role`
5. Execute the workflow

## Provider Split

- `GroqCloud`: role classification + fit scoring
- `Gemini`: resume, cover letter, and email generation

## Next Step

After the core flow works, add:

- `Google Sheets - Append Row`
- `Telegram - Send Message`
- `Manual Review Capture`
- `Learning Extraction`
