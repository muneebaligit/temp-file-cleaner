import os
import sys
import ctypes
import shutil

VERSION = "1.0.0"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

DEFAULT_FOLDERS = [
    os.path.join(os.environ.get("LOCALAPPDATA", ""), "Temp"),
    os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Prefetch"),
    os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Temp"),
]

def ask(user1):
    val = input(f"  {user1} ").strip().lower()
    if val == "exit":
        return "EXIT"
    if val == "back":
        return "BACK"
    return val

def ask_path(user2):
    val = input(f"  {user2} ").strip()
    if val.lower() == "exit":
        return "EXIT"
    if val.lower() == "back":
        return "BACK"
    return val

def clean_folder(path):
    deleted = 0
    skipped = 0
    if not os.path.exists(path):
        print(f"  [NOT FOUND]   {path}")
        return

    print(f"  [SCANNING]    {path}")

    try:
        entries = os.listdir(path)
    except PermissionError:
        print(f"  [ACCESS DENIED] {path}\n")
        return
    except Exception as e:
        print(f"  [ERROR]  {e}\n")
        return

    for name in entries:
        full = os.path.join(path, name)
        try:
            if os.path.isfile(full) or os.path.islink(full):
                os.remove(full)
            else:
                shutil.rmtree(full)
            deleted += 1
        except PermissionError:
            skipped += 1
        except Exception:
            skipped += 1

    print(f"  [DONE]\n  Removed: {deleted}  |  Skipped: {skipped}\n")

def run_cleanup(folders):
    print("\n" + "-" * 45)
    for f in folders:
        clean_folder(f)
    print("-" * 45)
    print("  Cleanup completed!\n")

def get_folders():
    while True:
        print("  Which folders to clean?\n")
        print("  1    -> Default Windows Temp folders")
        print("  2    -> Custom folder(s)")
        print("  Exit -> Quit\n")

        choice = ask("Choice:")
        if choice == "EXIT":
            return "EXIT"
        if choice == "BACK":
            return "BACK"
        if choice == "1":
            return DEFAULT_FOLDERS

        if choice == "2":
            while True:
                print("  How many custom folders?\n")
                print("  1    -> One folder")
                print("  2    -> Two folders\n")
                print("  EXIT -> Quit\n")

                num = ask("Choice (1/2):")
                if num == "EXIT":
                    return "EXIT"
                if num == "BACK":
                    break
                if num not in ("1", "2"):
                    print("\n  [ERROR] Enter 1 or 2.")
                    input("  Press Enter to try again...")
                    continue

                paths = []
                go_back = False

                for i in range(int(num)):
                    while True:
                        print(f"  Enter path for folder {i + 1} of {num}\n")
                        path = ask_path(f"Folder {i + 1} path:")
                        if path == "EXIT":
                            return "EXIT"
                        if path == "BACK":
                            go_back = True
                            return "BACK"
                        paths.append(path)
                        break
                    if go_back:
                        break
                if go_back:
                    continue
                return paths

        print("\n  [ERROR] Enter 1, 2, or 'exit'.")
        input("  Press Enter to try again...")

def main():
    while True:
        folders = get_folders()
        if folders == "EXIT":
            break

        run_cleanup(folders)

        while True:
            choice = ask("Run again? (repeat / exit):")
            if choice == "repeat":
                break
            if choice == "EXIT":
                folders = "EXIT"
                break
            print("\n  [ERROR] Type 'repeat' or 'exit'.")

        if folders == "EXIT":
            break

    print("  Goodbye!\n")
    print("=" * 20 + "\n")

if __name__ == "__main__":
    if not is_admin():
        print("  [INFO] Admin rights needed. Requesting elevation...")
        elevate()
    main()
