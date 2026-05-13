import os

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
        return f"Path not found: {path}"

    if os.path.isfile(path):
        return f"{path} is a file"

    lines = []

    def walk(current_path, prefix="", depth=0):
        if depth > max_depth:
            return

        try:
            items = sorted(os.listdir(current_path))
        except Exception as e:
            lines.append(f"{prefix} Error: {str(e)}")
            return

        # Optional: filter hidden files
        items = [f for f in items if not f.startswith(".")]

        for i, item in enumerate(items):
            full_path = os.path.join(current_path, item)
            is_last = (i == len(items) - 1)

            connector = "└── " if is_last else "├── "
            line = prefix + connector + item

            if os.path.isdir(full_path):
                line += "/"

            lines.append(line)

            if os.path.isdir(full_path):
                next_prefix = prefix + ("    " if is_last else "│   ")
                walk(full_path, next_prefix, depth + 1)

    # Root header (important for clarity)
    lines.append(f"{path}/")

    walk(path)

    return "\n".join(lines)
