import os
from datetime import datetime

OUTPUT_DIR = "output"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def write_file(path, content):
    try:
        # --- original write ---
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        # --- also save a copy in output/ ---
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        base_name = os.path.basename(path)
        output_path = os.path.join(
            OUTPUT_DIR,
            f"{timestamp}_{base_name}"
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Wrote {path} and saved copy to {output_path}"

    except Exception as e:
        return f"Write failed: {str(e)}"

def save_output(content, prefix="response"):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.txt"
        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path
    except Exception as e:
        return f"Output save failed: {str(e)}"
