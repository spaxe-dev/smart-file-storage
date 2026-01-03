
# Smart File Storage

A simple and extensible Python-based file organizer that automatically sorts files into folders based on their file extensions.

This project is designed to be minimal, readable, and easy to extend later with smarter rules or ML-based classification.

---

## Features

* Automatically scans an input directory
* Sorts files into categorized folders (images, text files, PDFs, etc.)
* Creates destination folders automatically
* Handles unknown file types by placing them in an `others` folder
* Written using modern `pathlib` (no fragile path string handling)
* Easy to extend and refactor

---

## Project Structure

```
smart-file-storage/
│
├── input/          # Place files to be sorted here
├── sorted/         # Output directory (auto-created)
│   ├── imgs/
│   ├── txt/
│   ├── pdfs/
│   └── others/
│
├── main.py         # Main script
└── README.md
```

---

## How It Works

The script:

1. Iterates through all files in the `input/` directory
2. Checks the file extension
3. Maps the extension to a target folder
4. Moves the file into the corresponding folder inside `sorted/`

---

## Supported File Types

| Extension               | Destination Folder |
| ----------------------- | ------------------ |
| `.png`, `.jpg`, `.jpeg` | `imgs/`            |
| `.txt`                  | `txt/`             |
| `.pdf`                  | `pdfs/`            |
| others / no extension   | `others/`          |

You can easily add more file types by editing the extension map.

---

## Usage

1. Make sure you have Python 3.10 or higher installed
2. Clone the repository
3. Place files inside the `input/` folder
4. Run the script:

```bash
python main.py
```

The files will be moved into the `sorted/` directory.

---

## Example Extension Map

```python
EXT_MAP = {
    ".png": "imgs",
    ".jpg": "imgs",
    ".jpeg": "imgs",
    ".txt": "txt",
    ".pdf": "pdfs",
}
```

---

## Future Improvements

* Dry-run mode
* Undo / rollback support
* Content-based classification
* ML-based semantic sorting
* CLI flags
* Logging and batch history

---

## License

MIT License

---
