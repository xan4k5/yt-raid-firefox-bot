import os
import shutil
import time
import pyautogui
import subprocess
from pathlib import Path
import pygetwindow as gw

SCRIPT_DIR = Path(__file__).parent
ACCOUNTS_DIR = SCRIPT_DIR / "accounts"
TEMP_PROFILES_DIR = SCRIPT_DIR / "temp_profiles"
TEMP_PROFILES_DIR.mkdir(exist_ok=True)

FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
YOUTUBE_CHAT_URL = "https://www.youtube.com/live_chat?v=duXhxXjT05E"
CHAT_INPUT_COORDS = (764, 861)
MESSAGE_TEXT = "RAID"

REQUIRED_FILES = [
    "key4.db",
    "cookies.sqlite",
    "cert9.db",
    "prefs.js",
    "sessionstore.jsonlz4",
    "places.sqlite",
    "places.sqlite-wal",
    "places.sqlite-shm",
]
REQUIRED_DIRS = ["storage"]

def get_next_account_folder(index: int) -> Path | None:
    folder = ACCOUNTS_DIR / str(index)
    return folder if folder.exists() and folder.is_dir() else None

def prepare_temp_profile(account_folder: Path, temp_folder: Path):
    if temp_folder.exists():
        shutil.rmtree(temp_folder)
    temp_folder.mkdir(exist_ok=True)
    for file_name in REQUIRED_FILES:
        source = account_folder / file_name
        target = temp_folder / file_name
        if source.exists():
            shutil.copy2(source, target)
    for dir_name in REQUIRED_DIRS:
        src_dir = account_folder / dir_name
        dst_dir = temp_folder / dir_name
        if src_dir.exists():
            shutil.copytree(src_dir, dst_dir)
    print("Session copied")

def run_firefox_with_profile(profile_path: Path, url: str):
    proc = subprocess.Popen([
        FIREFOX_PATH,
        "-profile", str(profile_path),
        "--no-remote",
        "-new-instance",
        url
    ])
    print("Browser launched")
    return proc

def move_firefox_window():
    time.sleep(1)
    for window in gw.getWindowsWithTitle("Mozilla Firefox"):
        try:
            window.moveTo(100, 100)
            window.resizeTo(1280, 800)
            print("Browser window moved and resized")
            break
        except:
            pass

def close_firefox():
    os.system("taskkill /IM firefox.exe /F >nul 2>&1")
    print("Browser closed")

def send_message():
    time.sleep(1.5)
    move_firefox_window()
    time.sleep(0.1)
    pyautogui.click(CHAT_INPUT_COORDS)
    time.sleep(0.1)
    pyautogui.write(MESSAGE_TEXT, interval=0.005)
    pyautogui.press("enter")
    print("Message sent")

def main():
    index = 1
    while True:
        account_folder = get_next_account_folder(index)
        if not account_folder:
            print("All accounts processed.")
            break

        print(f"\nWorking with account {index}")
        temp_profile = TEMP_PROFILES_DIR / f"profile_{index}"

        try:
            prepare_temp_profile(account_folder, temp_profile)
            run_firefox_with_profile(temp_profile, YOUTUBE_CHAT_URL)
            send_message()
            close_firefox()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if temp_profile.exists():
                shutil.rmtree(temp_profile, ignore_errors=True)
                print("Temporary profile deleted")

        index += 1
        time.sleep(1)

if __name__ == "__main__":
    main()