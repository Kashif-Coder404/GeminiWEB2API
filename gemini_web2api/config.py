"""Configuration management."""
import json
import os

DEFAULT_CONFIG = {
    "port": 8081,
    "host": "0.0.0.0",
    "retry_attempts": 3,
    "retry_delay_sec": 2,
    "request_timeout_sec": 180,
    "gemini_bl": "boq_assistant-bard-web-server_20260716.08_p0",
    "auth_user": None,
    "xsrf_token": None,
    "default_model": "gemini-3.6-flash",
    "log_requests": True,
    "cookie_file": None,
    "proxy": None,
    "api_keys": [],
    "temporary_chats": False,
}

CONFIG = dict(DEFAULT_CONFIG)
xsrf = os.environ.get("XSRF_TOKEN") or os.environ.get("xsrf_token")
if xsrf:
    CONFIG["xsrf_token"] = xsrf
bl_env = os.environ.get("GEMINI_BL") or os.environ.get("gemini_bl")
if bl_env:
    CONFIG["gemini_bl"] = bl_env
auth_u = os.environ.get("AUTH_USER") or os.environ.get("auth_user")
if auth_u:
    CONFIG["auth_user"] = auth_u


def load_config(path: str = None):
    """Load config from JSON file."""
    if path and os.path.exists(path):
        with open(path) as f:
            CONFIG.update(json.load(f))
    return CONFIG


def find_config():
    """Search for config file in standard locations."""
    for p in ["./config.json", os.path.expanduser("~/.config/gemini-web2api/config.json")]:
        if os.path.exists(p):
            return p
    return None
