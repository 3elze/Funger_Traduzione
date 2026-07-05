import shutil
from pathlib import Path

source = Path(r"D:\MODDING\Funger\Mods\Italiano\Github")
destination = Path(r"D:\MODDING\Funger\Fear & Hunger\www\data")

if not source.exists():
    raise FileNotFoundError(f"La cartella sorgente non esiste: {source}")

destination.mkdir(parents=True, exist_ok=True)

for item in source.rglob("*"):
    relative_path = item.relative_to(source)
    dest_item = destination / relative_path

    if item.is_dir():
        dest_item.mkdir(parents=True, exist_ok=True)
    else:
        dest_item.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, dest_item)

print("Operazione completata.")