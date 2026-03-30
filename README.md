# Temp File Cleaner v1.0.0

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple yet powerful command-line utility to help you easily clean temporary files and folders from your Windows system.

## ✨ Features

-   **Default Cleaning**: Clean standard Windows temporary folders (`%temp%`, `C:\Windows\Temp`, etc.) with a single command.
-   **Custom Cleaning**: Option to specify one or two custom folder paths for cleaning.
-   **Interactive Menu**: An easy-to-use, menu-driven interface that guides you through the entire process.
-   **Error Handling**: If a file is in use or cannot be deleted, the script gracefully skips it and continues the process without crashing.
-   **Detailed Summary**: After cleaning, it provides a summary of how many files/folders were deleted and how many were skipped.
-   **No Dependencies**: Uses only Python's standard library, so no need to install any external packages.

## 🚀 How to Use

1.  **Download the File**: Download the `temp-file-cleaner.py` file from this repository.
2.  **Open a Terminal**: Open Command Prompt (CMD) or PowerShell.
3.  **Navigate to the Directory**: Use the `cd` command to go to the folder where you saved the file.
    ```bash
    cd path\to\your\folder
    ```
4.  **Run the Script**: Execute the script using the command below.
    ```bash
    python temp-file-cleaner.py
    ```
5.  **Follow the Prompts**: Choose the options displayed on the screen to start the cleaning process.

## ⚠️ Disclaimer

This script **permanently deletes** files from your computer. Use it at your own risk and discretion. Ensure that the folders you are cleaning do not contain any important data. Providing an incorrect folder path could lead to the deletion of valuable data. The developer will not be held responsible for any data loss.

## 📄 License

This project is licensed under the MIT License.
