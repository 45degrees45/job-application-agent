"""Google service account helper reused from earlier project patterns."""

from __future__ import annotations

import json
import os

from google.oauth2 import service_account

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]


def get_google_creds() -> service_account.Credentials:
    """Return Google credentials from inline JSON or a file path."""
    raw_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
    file_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "").strip()

    if raw_json:
        info = json.loads(raw_json)
        return service_account.Credentials.from_service_account_info(info, scopes=SCOPES)

    if file_path:
        return service_account.Credentials.from_service_account_file(file_path, scopes=SCOPES)

    raise RuntimeError(
        "Set GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_APPLICATION_CREDENTIALS before using Sheets."
    )

