# SORTIFY

Sortify is a Python script designed to automatically sort and organize files within a specified directory. By categorizing files into predefined folders based on their file types, this utility streamlines the process of managing a cluttered file system.

**Note:** If you are using Windows, use the file named `file_sorter_windows.py`. If you are using macOS or Linux, use the file named `file_sorter_mac.py`.

## Features

- **Automatic Folder Creation:** Creates necessary folders for various file types if they do not already exist.
- **File Categorization:** Moves files into the appropriate folders based on their extensions. Supported categories include:
  - CSV Files
  - Image Files
  - Text Files
  - Excel Files
  - Word Documents
  - PowerPoint Presentations
  - Python Scripts
  - PDFs
  - Audio Files
  - Video Files
  - Web Files
  - Archives
- **Error Handling:** Provides user-friendly error messages if the specified path does not exist.

## Usage

1. Run the script.
2. Enter the path to the directory containing the files you want to organize.
3. The script will create folders (if they don’t exist) and move the files into the corresponding folders based on their file types.

**Note:** Ensure the provided path is correct and accessible. The script handles various file types and moves them to categorized folders such as 'IMAGE FILES', 'TEXT FILES', 'ARCHIVES', etc.

## Setup

1. Ensure Python is installed on your system.
2. Save the script as a `.py` file and execute it using a Python interpreter:
    ```bash
    python your_script_name.py
    ```
3. After running, the files in the specified path will be sorted into their respective folders, making file management easier and more organized.

## Customization

Feel free to customize the script to add additional file types or categories as needed.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.
