import json
from pathlib import Path

# configs

configPath = Path("config.json")
undolog = Path("sortlog.json")

#initialization
def loadconfig() -> dict:
    with configPath.open("r", encoding="utf-8") as f:
        config = json.load(f)
    return config

def resetlog():
    undolog.write_text("[]", encoding="utf-8")

#mapping \
def buildClassMap(config: dict) -> dict:
    classMAP = {}
    for folder, extension in config.items():
        for extensions in extension:
            classMAP[extensions.lower()] = folder
    return classMAP

# functions
def extractfile(sourcedir: Path, targetdir: Path, classMap:dict, dry_run: bool):
    for file in sourcedir.iterdir():
        if file.is_file():
            move(file, targetdir, classMap, dry_run)
        else: 
            if file.is_dir():
                extractfile(sourcedir=file, targetdir=targetdir, classMap=classMap, dry_run=dry_run)
                
            
            
def fclassify(fpath :Path, classMAP: dict) -> str:
    extType = fpath.suffix.lower().lstrip(".")
    return classMAP.get(extType, "others")
    

def move(fpath: Path, targetdir: Path, classMap: dict, dry_run: bool):
    folder = fclassify(fpath, classMap)
    destination = targetdir / folder/ fpath.name

    if dry_run:
        print(f"[DRY-RUN] {fpath} --> {destination}")
        return
    
    destination.parent.mkdir(parents=True, exist_ok=True)
    fpath.rename(destination)

    move_log(fpath.resolve(), destination.resolve())
    
def runSort(source: Path, target: Path, dry: bool = False):
    config = loadconfig()
    classMAP = buildClassMap(config)
    if not dry:
        resetlog()
    extractfile(sourcedir=source, targetdir=target, classMap=classMAP, dry_run=dry)

def move_log(src: Path, dst: Path):
    data = json.loads(undolog.read_text(encoding="utf-8"))
    data.append({
        "from": str(src.resolve()),
        "to": str(dst.resolve())
    })
    text = json.dumps(data)
    undolog.write_text(text, encoding="utf-8")

def undorun():
    
    if not undolog.exists():
        print("Undo log doesnt exist, unable to undo.")

    data = json.loads(undolog.read_text(encoding="utf-8"))
    
    for entry in reversed(data):
        src = Path(entry["to"])
        dst = Path(entry["from"])

        if not src.exists():
            print(f"[SKIPPED] Missing File: {src}")
            continue
        
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)