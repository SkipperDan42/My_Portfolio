import os
import json

BASE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.join(BASE_DIR, "resources")  # change "resources" if needed
OUTPUT_FILE = os.path.join(BASE_DIR, "manifest.json")

def build_structure(path):
    structure = {}
    for item in sorted(os.listdir(path)):
        # Skip hidden/system files (.DS_Store, ._* etc.) and temp files (~, $)
        if item.startswith('.') or item.startswith('~') or item.startswith('$'):
            continue

        full_path = os.path.join(path, item)
        rel_path = os.path.relpath(full_path, BASE_DIR)
        if os.path.isdir(full_path):
            sub = build_structure(full_path)
            if sub:
                structure[item] = sub
        else:
            structure[item] = rel_path.replace("\\", "/")
    return structure

if __name__ == "__main__":
    manifest = {os.path.basename(ROOT_DIR): build_structure(ROOT_DIR)}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"✅ Manifest written to {OUTPUT_FILE}")