# Настройки проекта
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"

load_dotenv(env_path)
token = os.getenv("BOT_TOKEN")

print(token)  # ← ОБЯЗАТЕЛЬНО проверить
# print("CWD:", os.getcwd())

# import sys
# print("PATH:", sys.path)
# print("PYTHONPATH:", os.getenv("PYTHONPATH"))
