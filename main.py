import os
from pathlib import Path

# configs
DRY_RUN = True
EXT_MAP = {
    ".png": "imgs",
    ".jpg": "imgs",
    ".jpeg": "imgs",
    ".txt": "txt",
    ".pdf": "pdfs",
}

sourcedir = Path('input/')
targetdir = Path('sorted/')
def extractfile():
    for file in sourcedir.iterdir():
        if file.is_file():
            fpath = file
            fname = fpath.stem
            move(fpath)
            # fextension = fpath.suffix.lower()
            # print(f"{fname} {fextension}\n")


def move(fpath: Path):
    folder = EXT_MAP.get(fpath.suffix.lower())
    destination = targetdir / folder

    if DRY_RUN:
        print(f"[DRY-RUN] {fpath} --> {destination}")
        return
    
    destination.parent.mkdir(parents=True, exist_ok=True)
    fpath.rename(destination/fpath.name)
    

extractfile()