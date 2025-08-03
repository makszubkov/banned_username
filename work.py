from pyrogram import Client
from decouple import config
import time
import logging
import sys

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Config
USERNAME_FILE = "myfile"  # Replace with your file name if different
OUTPUT_FILE = "successful_usernames.txt"
COOLDOWN = 15
successful_usernames = []

# Load usernames from file
def load_usernames(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip().lstrip("@") for line in f if line.strip().startswith("@")]

# Initialize Pyrogram client
bot = Client(
    name=config("LOGIN"),
    api_id=config("API_ID"),
    api_hash=config("API_HASH"),
    phone_number=config("PHONE")
)

usernames = load_usernames(USERNAME_FILE)

with bot:
    logger.info(f"Loaded {len(usernames)} usernames. Starting attempts...")

    for i, username in enumerate(usernames, 1):
        logger.info(f"[{i}/{len(usernames)}] Trying @{username}")
        try:
            result = bot.set_username(username)
            if result:
                logger.info(f"✅ Successfully set username: @{username}")
                successful_usernames.append(username)
            else:
                logger.warning(f"⚠️ Telegram returned no result for @{username}")
        except Exception as e:
            logger.warning(f"❌ Failed to set @{username}: {e}")

        if i < len(usernames):
            logger.info(f"⏳ Waiting {COOLDOWN} seconds before next attempt...")
            time.sleep(COOLDOWN)

# Save successful usernames to file
if successful_usernames:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for uname in successful_usernames:
            f.write(f"@{uname}\n")

# Final output
print("\n📋 Successfully set usernames:")
for uname in successful_usernames:
    print(f"✅ @{uname}")
print(f"\nSaved to file: {OUTPUT_FILE}")
