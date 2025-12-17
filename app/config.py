import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("MODEL", "gpt-4.1-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
LOG_DB = os.getenv("LOG_DB", "./tutoragent.sqlite")

# Optional: hard fail if you want
# if not OPENAI_API_KEY:
#     raise RuntimeError("OPENAI_API_KEY missing. Put it in .env or Codespaces secrets.")
