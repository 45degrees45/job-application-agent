# Architecture

A self-improving job application automation system that takes a job URL or description as input and outputs a tailored resume, cover letter, and email draft using GroqCloud for fit scoring and Gemini for content generation. A learning loop stores diffs between AI-generated and human-edited outputs to improve future generations.

## V1 Flow

```mermaid
flowchart TD
    A([Manual Trigger / Telegram Trigger]) --> B[Switch: Input Type]
    B -->|URL provided| C[HTTP Request: Fetch Job Page]
    B -->|Raw description| E[Set: Normalize Job Payload]
    C --> D[HTML Extract: Job Content]
    D --> E
    E --> F[GroqCloud: Role Classifier + Fit Scorer]
    F --> G{IF: Score >= 7?}
    G -->|No — score < 7| H[Return: Fit Score + Gaps + Skip Recommendation]
    G -->|Yes| I[Gemini: Resume Tailor]
    I --> J[Gemini: Cover Letter Writer]
    J --> K[Gemini: Email Writer]
    K --> L[Google Sheets: Append Generation Row\napplications tab]
    L --> M[Telegram: Send Review Package]
    M --> N([Joseph Reviews and Edits])
    N --> O[Manual: Paste Final Edits]
    O --> P[Google Sheets: Update Final Output]
```

## V2 Learning Loop

```mermaid
flowchart TD
    P[Google Sheets: Finalized Row] --> Q[Gemini: Diff Analyzer]
    Q --> R[Code: Learnings Consolidator]
    R --> S[Google Sheets: Append Learnings Row\nlearnings tab]
    S --> T[Gemini: Style Guide Merger]
    T --> U[Google Docs: Joseph Style Guide]
    U -->|Injected into future prompts| V[Gemini: Resume / Cover Letter / Email Generation]
```

## Component Map

| Component | Role |
|---|---|
| n8n | Workflow orchestration |
| GroqCloud (`llama-3.3-70b-versatile`) | Role classification and fit scoring |
| Gemini (`gemini-2.0-flash`) | Resume, cover letter, and email generation |
| Google Sheets (`applications` tab) | Stores generated and final-edited outputs |
| Google Sheets (`learnings` tab) | Stores per-application style diffs and patterns |
| Google Docs | Canonical Joseph Style Guide (V2) |
| Telegram | Review delivery and trigger |
| Python utils | Google auth helper + Sheets adapter |
