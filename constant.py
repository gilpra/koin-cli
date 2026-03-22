import os

ROOT_TRACKER_DIR = os.path.expanduser("~/.local/share/koin")
DATABASE_PATH = os.path.join(ROOT_TRACKER_DIR, "tracker.json")
VALID_CATEGORY={
    "expense": ["food", "transport", "shopping", "biils", "other"],
    "income": ["salary", "business", "investment", "gift", "other"]
}
