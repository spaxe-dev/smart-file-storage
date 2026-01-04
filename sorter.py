import json
import argparse
from pathlib import Path

# configs

configPath = Path("config.json")

#initialization
def loadconfig() -> dict:
    with configPath.open("r", encoding="utf-8") as f:
        config = json.load(f)
    return config

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
    destination = targetdir / folder

    if dry_run:
        print(f"[DRY-RUN] {fpath} --> {destination}")
        return
    
    destination.mkdir(parents=True, exist_ok=True)
    fpath.rename(destination/fpath.name)
    
def runSort(source: Path, target: Path, dry: bool = False):
    config = loadconfig()
    classMAP = buildClassMap(config)
     
    extractfile(sourcedir=source, targetdir=target, classMap=classMAP, dry_run=dry)