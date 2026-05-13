import os
from extra_utils import CYAN, RED, GREEN, WHITE, YELLOW, OFF

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

def list_files(path=".", max_depth=2):
    """
    Return a tree-style directory listing.
    """

    # Normalize path
    path = path.strip()

    if not os.path.exists(path):
        return f"{RED}Path not found: {path}{OFF}"

    if os.path.isfile(path):
        return f"{CYAN}{path} is a file{OFF}"

    lines = []

    def walk(current_path, prefix="", depth=0):
        if depth > max_depth:
            return

        try:
            items = sorted(os.listdir(current_path))
        except Exception as e:
            lines.append(f"{RED}{prefix} Error: {str(e)}{OFF}")
            return

        # Optional: filter hidden files
        items = [f for f in items if not f.startswith(".")]

        for i, item in enumerate(items):
            full_path = os.path.join(current_path, item)
            is_last = (i == len(items) - 1)

            connector = f"{CYAN}└──{OFF}" if is_last else f"{CYAN}├──{OFF}"
            if os.path.isdir(full_path):
                name = f"{CYAN}{item}/{OFF}"
            elif item.endswith(".py"):
                name = f"{GREEN}{item}{OFF}"
            else:
                name = f"{WHITE}{item}{OFF}"

            line = prefix + connector + item

            if os.path.isdir(full_path):
                line += f"{CYAN}/{OFF}"

            lines.append(line)

            if os.path.isdir(full_path):
                next_prefix = prefix + (f"    " if is_last else f"{CYAN}│   {OFF}")
                walk(full_path, next_prefix, depth + 1)

    # Root header (important for clarity)
    lines.append(f"{CYAN}{path}/{OFF}")
    walk(path)

    return "\n".join(lines)
