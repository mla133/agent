def write_file(path, content):
    try:
        with open(path, "w") as f:
            f.write(content)
        return f"Wrote {path}"
    except Exception as e:
        return str(e)
