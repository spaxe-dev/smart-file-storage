import json
from pathlib import Path

# configs
DRY_RUN = False

configPath = Path("config.json")

sourcedir = Path('input/')
targetdir = Path('sorted/')

#initialization
with configPath.open("r", encoding="utf-8") as f:
    config = json.load(f)

#mapping \
classMAP = {}
for folder, extension in config.items():
    for extensions in extension:
        classMAP[extensions.lower()] = folder

# functions
def extractfile():
    for file in sourcedir.iterdir():
        if file.is_file():
            move(file)

def fclassify(fpath :Path):
    extType = fpath.suffix.lower().lstrip(".")
    return classMAP.get(extType, "others")
    

def move(fpath: Path):
    folder = fclassify(fpath)
    destination = targetdir / folder

    if DRY_RUN:
        print(f"[DRY-RUN] {fpath} --> {destination}")
        return
    
    destination.mkdir(parents=True, exist_ok=True)
    fpath.rename(destination/fpath.name)
    

extractfile()