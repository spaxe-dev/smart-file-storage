
# Smart File Storage

Smart File Storage is a minimal, config-driven Python CLI tool that organizes files into folders based on their file extensions.

The project focuses on **explicit data flow**, **clean separation of concerns**, and **predictable behavior**. Classification rules live entirely in a JSON config file, while the CLI provides safe and flexible control over execution.

---

## Features

* Command-line interface powered by Click
* Config-driven file classification using JSON
* Automatic destination folder creation
* Safe dry-run mode (`--dry`) to preview changes
* Handles unknown file types via an `others` category
* No global state or hidden dependencies
* Uses modern `pathlib` for filesystem operations
* Minimal dependencies (only Click)

---

## Project Structure

```
smart-file-storage/
│
├── input/              # Default source directory
├── sorted/             # Default output directory
│
├── config.json         # File type classification rules
├── main.py             # CLI entry point
├── sorter.py           # Core sorting logic
├── requirements.txt
└── README.md
```

---

## How It Works

1. The CLI parses user input (`--source`, `--target`, `--dry`)
2. The core sorter loads `config.json`
3. File extensions are mapped to destination folders
4. Files are scanned in the source directory
5. Destination folders are created on demand
6. Files are moved (or previewed in dry-run mode)

All data flows explicitly through function arguments — no globals, no side effects.

---

## Configuration

Classification rules are defined in `config.json`.

### Example `config.json`

```json
{
  "images": ["png", "jpg", "jpeg", "gif"],
  "documents": ["pdf", "txt", "docx"],
  "audio": ["mp3", "wav"],
  "video": ["mp4", "mkv"]
}
```

Rules:

* Keys are destination folder names
* Values are lists of file extensions (without dots)
* Matching is case-insensitive
* Unknown extensions go to `others/`

No code changes are required to add or modify file types.

---

## Installation

### Requirements

* Python 3.10 or higher

### Setup (recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## Usage

### Show help

```bash
python main.py --help
```

### Default run

```bash
python main.py
```

### Dry-run (preview only)

```bash
python main.py --dry
```

### Custom source and target

```bash
python main.py --source Downloads --target Sorted
```

---

## Dry-Run Mode

When `--dry` is enabled:

* No files are moved
* No folders are created
* All actions are printed to the console

Example output:

```
[DRY-RUN] input/example.pdf -> sorted/documents/example.pdf
```

This allows safe testing and configuration changes.

---

## Design Principles

* Explicit dependency passing over global state
* Clear separation between CLI and core logic
* Configuration over hardcoded behavior
* Predictable, testable functions
* Minimal surface area for bugs

---

## Planned Improvements

* Recursive directory sorting
* Ignore rules for common folders
* Collision-safe file renaming
* Summary report after execution
* Packaging as an installable CLI command
* Optional logging support

---

## License

MIT License

---
