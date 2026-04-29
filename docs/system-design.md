# System Design

## V1

Fastest workable version.

Provider split:

- `GroqCloud` for strict fit scoring and profile selection
- `Gemini` for resume, cover letter, and email generation

### Flow

1. Receive `job_url` or `job_description`.
2. If URL is provided, fetch and clean the posting text.
3. Classify role type:
   - `product_ai_automation`
   - `founders_office_strategy`
4. Score fit from 1-10.
5. If score `< 7`, stop and return:
   - fit score
   - key gaps
   - recommendation to skip
6. If score `>= 7`, generate:
   - tailored resume
   - short cover letter
   - direct email draft
7. Save everything to Google Sheets.
8. Send result to Telegram or a simple review UI.
9. Joseph edits manually.
10. Final edited version is pasted back and stored.

### n8n Workflow Design

#### Workflow: `Job Application Agent V1`

1. `Manual Trigger` or `Telegram Trigger`
2. `Switch - Input Type`
3. `HTTP Request - Fetch Job Page`
4. `HTML Extract - Job Content`
5. `Set - Normalize Job Payload`
6. `OpenAI Chat Model - Role Classifier + Fit Scorer`
7. `IF - Score Gate`
8. `OpenAI Chat Model - Resume Tailor`
9. `OpenAI Chat Model - Cover Letter Writer`
10. `OpenAI Chat Model - Email Writer`
11. `Google Sheets - Append Generation Row`
12. `Telegram - Send Review Package`
13. `Manual Trigger - Final Edit Capture`
14. `Google Sheets - Update Final Output`

### Connections

- `Manual Trigger` -> `Switch - Input Type`
- `Telegram Trigger` -> `Switch - Input Type`
- `Switch - Input Type` -> `HTTP Request - Fetch Job Page`
- `Switch - Input Type` -> `Set - Normalize Job Payload`
- `HTTP Request - Fetch Job Page` -> `HTML Extract - Job Content`
- `HTML Extract - Job Content` -> `Set - Normalize Job Payload`
- `Set - Normalize Job Payload` -> `OpenAI Chat Model - Role Classifier + Fit Scorer`
- `OpenAI Chat Model - Role Classifier + Fit Scorer` -> `IF - Score Gate`
- `IF - Score Gate` true -> `OpenAI Chat Model - Resume Tailor`
- `OpenAI Chat Model - Resume Tailor` -> `OpenAI Chat Model - Cover Letter Writer`
- `OpenAI Chat Model - Cover Letter Writer` -> `OpenAI Chat Model - Email Writer`
- `OpenAI Chat Model - Email Writer` -> `Google Sheets - Append Generation Row`
- `Google Sheets - Append Generation Row` -> `Telegram - Send Review Package`
- `Manual Trigger - Final Edit Capture` -> `Google Sheets - Update Final Output`

### V1 Storage Table

Use one Google Sheet named `applications`.

Columns:

- `id`
- `date`
- `company`
- `role`
- `job_url`
- `job_description`
- `base_profile_used`
- `fit_score`
- `fit_gaps`
- `decision`
- `generated_resume`
- `generated_cover_letter`
- `generated_email_subject`
- `generated_email_body`
- `final_resume`
- `final_cover_letter`
- `final_email_subject`
- `final_email_body`
- `editor_notes`

### V1 Notes

- Keep final edit capture manual.
- Do not automate Gmail send until outputs look consistently right.
- Use markdown or plain text first, not PDF generation.

## V2

Adds memory and learning.

### New Components

1. `OpenAI Chat Model - Diff Analyzer`
2. `Code - Learnings Consolidator`
3. `Google Sheets - Append Learnings Row`
4. `Google Sheets - Read Prior Learnings`
5. `OpenAI Chat Model - Style Guide Merger`
6. `Google Docs` or `Notion` page for canonical `Joseph Style Guide`

### V2 Learning Loop

1. Read original output and final edited output.
2. Extract:
   - removed phrases
   - preferred structure
   - tone corrections
   - stronger phrasing patterns
   - repeated keyword choices
3. Save structured learnings.
4. Merge repeated learnings into `Joseph Style Guide`.
5. Inject style guide into all future generation prompts.

### V2 Additional n8n Nodes

1. `Google Sheets - Read Finalized Rows`
2. `OpenAI Chat Model - Learning Extraction`
3. `Code - Aggregate Repeated Patterns`
4. `Google Sheets - Append Learnings`
5. `Google Docs - Update Style Guide`
6. `Google Sheets - Lookup Style Guide Context`

### V2 Intelligence

- Skip jobs below score threshold.
- Surface missing keywords before applying.
- Suggest resume improvements before final generation.
- Explain why one base profile was chosen.

## Prompt Inputs

Each generation call should receive:

- Joseph profile
- selected base profile
- normalized job description
- style guide
- recent learnings
- output format contract

## Minimal JSON Payload

```json
{
  "company": "Acme",
  "role": "Chief of Staff",
  "job_url": "https://example.com/job",
  "job_description": "Full cleaned posting text",
  "base_profile_used": "founders_office_strategy",
  "fit_score": 8,
  "fit_gaps": ["B2B SaaS finance exposure"],
  "decision": "apply"
}
```
