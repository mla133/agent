import os

def list_files(path="."):
    try:
        return os.listdir(path)[:50]
    except Exception as e:
        return str(e)

def read_file(path, max_lines=150):
    try:
        with open(path, "r") as f:
            lines = f.readlines()
        return "".join(lines[:max_lines])
    except Exception as e:
        return str(e)

def search_files(query):
    matches = []
    for root, _, files in os.walk("."):
        for f in files:
            if query.lower() in f.lower():
                matches.append(os.path.join(root, f))
    return matches[:20]
