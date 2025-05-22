YouTube Firefox Chat Bot

This script automates sending a message into a YouTube Live Chat using multiple Firefox user profiles. Each profile logs in with a different account, sends a message, and exits.

---

🛠 How It Works:

1. You prepare Firefox profiles manually — one per YouTube/Google account.
2. The script copies each profile into a temporary folder.
3. It launches Firefox with the copied profile and opens a live chat.
4. A message is typed and sent using mouse automation.
5. The browser is closed, and the temporary profile is deleted.
6. The process repeats for the next account.

---

📁 Folder & Profile Structure:

1. Create a folder called: accounts
2. Inside it, make numbered subfolders: 1, 2, 3, ...
3. Each subfolder must contain the required files from a Firefox profile that was used to log into YouTube.

Example structure:

accounts/
├── 1/
│   ├── cert9.db
│   ├── cookies.sqlite
│   ├── key4.db
│   ├── places.sqlite
│   ├── prefs.js
│   ├── sessionstore.jsonlz4
│   ├── webappsstore.sqlite
│   └── storage/          (folder)
├── 2/
│   └── (same structure)
├── 3/
    └── ...

How to get these files:

- Open Firefox and create a new profile (about:profiles)
- Log into a YouTube/Google account using that profile
- Fully close Firefox
- Navigate to the profile path (usually under %APPDATA%\Mozilla\Firefox\Profiles\...)
- Copy the following items into your numbered folder:

Required files:
- key4.db
- cookies.sqlite
- cert9.db
- prefs.js
- sessionstore.jsonlz4
- places.sqlite
- places.sqlite-wal (optional)
- places.sqlite-shm (optional)
- webappsstore.sqlite

Required folder:
- storage/

Each profile should be logged into a different YouTube account.

---

⚙️ Configuration:

You can edit the following variables in `main.py`:

- FIREFOX_PATH: path to your Firefox binary
- YOUTUBE_CHAT_URL: the full link to the live chat (you can use any live stream)
- CHAT_INPUT_COORDS: screen coordinates for the input box (use a tool like Paint or mouse position tracker)
- MESSAGE_TEXT: the message you want each account to send

Example:
FIREFOX_PATH = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
YOUTUBE_CHAT_URL = "https://www.youtube.com/live_chat?v=duXhxXjT05E"
CHAT_INPUT_COORDS = "764, 861" (i have fullhd monitor)
MESSAGE_TEXT = "RAID"

---

📦 Dependencies:

You need the following packages:

- pyautogui
- pygetwindow

Install them using:

pip install -r requirements.txt

Contents of `requirements.txt`:
pyautogui
pygetwindow

---

📁 Folder Overview:

/accounts/        — source profiles (you provide)
/temp_profiles/   — temporary profiles (auto-deleted)
/main.py          — main script

---

🚨 Disclaimer:

This tool is for automation, development, and learning purposes only.  
Do NOT use it for spam or to break YouTube’s terms of service.  
You are responsible for how you use it.

Use at your own risk. Accounts may be suspended if abused.

---

Created for self-learning, experimentation, and understanding browser automation(actually just for fun).

Have fun. Stay smart.
