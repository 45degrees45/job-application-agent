# PROJECT BRIEF — Job Application Agent

## Problem Statement
Writing tailored resumes and cover letters for each job application is time-intensive. The output quality depends heavily on effort, and there is no learning loop to improve over time based on what works.

## Solution Built
A self-improving job application automation system using n8n, Gemini, and GroqCloud. Takes a job URL/description as input and outputs a tailored resume, cover letter, and email draft. Captures edits and learns from the delta between generated and final versions.

## Key Features
- AI resume tailoring (2 modes: product_ai_automation / founders_office_strategy)
- AI cover letter and email draft generation
- Fit scoring via GroqCloud
- Google Sheets memory store
- Learning loop: stores diffs between AI output and human edits
- Telegram/n8n form review interface
- V1 (1-2 hrs buildable) and V2 (with learning injection) roadmap

## Tech Stack
n8n · Gemini API · GroqCloud · Google Sheets · Google Docs · Telegram · Python (utils)

## Status
In Progress

## Vibe Coding Effort
Sessions: ___ | Est. Hours: ___

## Users & Signups
Active Users: ___ (personal use — Joseph T C)

## Growth Tracking
_Track applications generated, interview rate, learning loop iterations._

## Last Updated
2026-04 (Apr 2026)

## Key Files
- `docs/system-design.md` — V1 and V2 architecture
- `docs/prompts.md` — generation/scoring/learning prompts
- `data/joseph_profile.seed.json` — user profile seed
- `CLAUDE.md` — project implementation rules
