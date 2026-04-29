"""Google Sheets storage adapter for job application runs."""

from __future__ import annotations

import gspread

from utils.google_auth import get_google_creds

APPLICATION_HEADERS = [
    "id",
    "date",
    "company",
    "role",
    "job_url",
    "job_description",
    "base_profile_used",
    "fit_score",
    "fit_gaps",
    "decision",
    "generated_resume",
    "generated_cover_letter",
    "generated_email_subject",
    "generated_email_body",
    "final_resume",
    "final_cover_letter",
    "final_email_subject",
    "final_email_body",
    "editor_notes",
]

LEARNINGS_HEADERS = [
    "application_id",
    "date",
    "company",
    "role",
    "base_profile_used",
    "diff_summary",
    "avoid",
    "prefer",
    "structure_preferences",
    "tone_preferences",
    "evidence_preferences",
    "style_guide_updates",
    "confidence",
]


def _get_client() -> gspread.Client:
    return gspread.authorize(get_google_creds())


def _open_workbook(sheet_id: str) -> gspread.Spreadsheet:
    return _get_client().open_by_key(sheet_id)


def _get_or_create_tab(sheet_id: str, tab_name: str, headers: list[str]) -> gspread.Worksheet:
    workbook = _open_workbook(sheet_id)
    try:
        return workbook.worksheet(tab_name)
    except gspread.WorksheetNotFound:
        ws = workbook.add_worksheet(title=tab_name, rows=1000, cols=max(len(headers), 20))
        ws.append_row(headers)
        return ws


def append_application(sheet_id: str, row: dict) -> None:
    ws = _get_or_create_tab(sheet_id, "applications", APPLICATION_HEADERS)
    ws.append_row([row.get(header, "") for header in APPLICATION_HEADERS], value_input_option="USER_ENTERED")


def append_learning(sheet_id: str, row: dict) -> None:
    ws = _get_or_create_tab(sheet_id, "learnings", LEARNINGS_HEADERS)
    ws.append_row([row.get(header, "") for header in LEARNINGS_HEADERS], value_input_option="USER_ENTERED")


def get_style_learnings(sheet_id: str) -> list[dict]:
    ws = _get_or_create_tab(sheet_id, "learnings", LEARNINGS_HEADERS)
    return ws.get_all_records()
