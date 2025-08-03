# Username Availability Checker

This project automates the process of checking and assigning available usernames using the Pyrogram library with the Telegram API.

## 📁 Project Structure

📦 Project Root
┣ 📜 startwork.py
┣ 📜 work.py
┣ 📜 .env
┣ 📜 requirements.txt
┣ 📜 .gitignore


---

## 🚀 Getting Started

### 1. Install Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt

You must also have Git and Python 3.10+ installed.
2. Environment Setup

Create a .env file in the root directory:

API_ID=your_api_id
API_HASH=your_api_hash
PHONE=+1234567890
LOGIN=session_name

🧠 Script Workflow
✅ startwork.py

    Initializes a Pyrogram client session.

    Sends a test message to your own Telegram account to verify setup.

    Automatically starts the client without stopping it after execution.

Usage:

python startwork.py

⚙️ work.py

    Loads a list of usernames from a .txt file (e.g. usernames.txt).

    Iterates over each username with a 15-second cooldown.

    Tries to assign the username to the Telegram account.

    Saves all successful usernames to success_log.txt.

    Shows results at the end of execution.

Usage:

python work.py

    ⚠️ Make sure the session is already authorized (run startwork.py at least once).

📄 Input Format

Your usernames.txt file must:

    Contain one username per line.

    Not include the @ symbol (e.g. username123, not @username123).

Example:

user1
username_test
sample_name
