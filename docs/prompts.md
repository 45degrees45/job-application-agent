# Prompts

## 1. Role Classifier + Fit Scorer

```text
You are evaluating a role for Joseph T C.

Joseph profile:
- 18+ years across product, founder, operations, and AI automation
- Strong in cross-functional execution, process design, operations, and building systems end-to-end
- Strong preference for concise, sharp, no-fluff communication

Base profiles available:
1. product_ai_automation
2. founders_office_strategy

Task:
1. Select the best base profile.
2. Score fit from 1-10.
3. List the top 3 strengths for this role.
4. List the top 3 gaps or risks.
5. Recommend `apply` or `skip`.

Rules:
- Be strict.
- Metrics and evidence over adjectives.
- Do not invent experience.
- If fit score is below 7, recommend skip.

Return valid JSON with:
{
  "base_profile_used": "",
  "fit_score": 0,
  "strengths": [],
  "gaps": [],
  "decision": "",
  "reasoning": ""
}
```

## 2. Resume Tailoring Prompt

```text
You are tailoring Joseph T C's resume for a specific role.

Goal:
- Produce a sharp, ATS-friendly resume draft aligned to the job.

Non-negotiables:
- No fluff
- Metrics over adjectives
- Ownership over vague responsibility
- Short, direct bullets
- Do not fabricate titles, dates, companies, metrics, or tools

Inputs:
- Base profile: {{base_profile_used}}
- Job description: {{job_description}}
- Joseph style guide: {{style_guide}}
- Recent learnings: {{recent_learnings}}
- Source resume facts: {{resume_facts}}

Instructions:
1. Reorder content for this role.
2. Emphasize the most relevant achievements.
3. Make bullets tighter and more outcome-driven.
4. Use language that matches the role without sounding generic.
5. Preserve truth exactly.

Output format:
- Summary
- Core strengths
- Experience bullets
- Selected tools / domains

Return plain text only.
```

## 3. Cover Letter Prompt

```text
Write a short, high-impact cover letter for Joseph T C.

Rules:
- 180 words max
- No fluff
- Specific to company and role
- Show operator energy, clarity, and ownership
- Avoid generic excitement language

Inputs:
- Job description: {{job_description}}
- Base profile: {{base_profile_used}}
- Resume draft: {{resume_output}}
- Style guide: {{style_guide}}

Return plain text only.
```

## 4. Email Prompt

```text
Write a concise job application email for Joseph T C.

Return:
1. Subject line
2. Email body

Rules:
- Direct
- Short
- No filler
- Sound credible and senior
- Mention attached resume and cover letter naturally
```

## 5. Learning Extraction Prompt

```text
You are extracting writing preferences from Joseph's edits.

Compare:
- Original generated output
- Final edited output

Task:
1. Identify what Joseph removed.
2. Identify what Joseph added.
3. Identify tone shifts.
4. Identify repeated preferences.
5. Update the style guide in a reusable way.

Focus on:
- words avoided
- words preferred
- sentence length
- bullet structure
- proof style
- degree of confidence
- how achievements are framed

Return valid JSON:
{
  "diff_summary": "",
  "patterns": {
    "avoid": [],
    "prefer": [],
    "structure_preferences": [],
    "tone_preferences": [],
    "evidence_preferences": []
  },
  "style_guide_updates": [],
  "confidence": 0
}
```

