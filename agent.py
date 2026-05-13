import json
import re
import sys
import io

# Fix Windows Unicode issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from llm import chat
from prompts import SYSTEM_PROMPT
from tools.fs import list_files, read_file, search_files
from tools.edit import write_file, save_output
from config import MAX_STEPS, MAX_TOOL_OUTPUT


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "search_files": search_files,
    "write_file": write_file
}


# ------------------------
# JSON EXTRACTION
# ------------------------

def extract_json(text):
    """
    Extract a full JSON object by tracking braces.
    Works with nested JSON.
    """
    start = text.find("{")
    if start == -1:
        return None

    brace_count = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            brace_count += 1
        elif text[i] == "}":
            brace_count -= 1

            if brace_count == 0:
                return text[start:i+1]

    return None

# ------------------------
# PARSER
# ------------------------

def parse_action(output):
    if len(output) > 8000:
        print("Output too long, truncating")
        output = output[:8000]

    json_str = extract_json(output)

    if not json_str:
        return None

    try:
        return json.loads(json_str)
    except:
        return None


# ------------------------
# AGENT LOOP
# ------------------------

def run_agent(user_input):

    # ------------------------
    # DIRECT COMMAND: LIST FILES (TREE MODE)
    # ------------------------
    user_lower = user_input.lower()

    if user_lower.startswith("list files"):
        parts = user_input.split()

        # Default values
        path = "."
        depth = 2

        # Extract path
        if "in" in parts:
            idx = parts.index("in")
            path = " ".join(parts[idx + 1:])

        # Extract depth (optional)
        if "depth" in parts:
            try:
                depth = int(parts[parts.index("depth") + 1])
            except:
                pass

        result = list_files(path, max_depth=depth)

        print("\nFinal Answer:\n")
        print(result)
        return

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input},
    ]

    for step in range(MAX_STEPS):
        output = chat(messages)

        action = parse_action(output)

        if action is None:
            print("\nFailed to parse model output:\n")
            print(output)
            return

        print(f"\nStep {step}")
        print("Reason:", action.get("reason", ""))

        # Final answer
        if action["action"] == "final":
            print("\nFinal Answer:\n")
            print(action["args"]["answer"])
            return

        # Tool call
        tool_name = action.get("tool_name")
        args = action.get("args", {})

        if tool_name not in TOOLS:
            result = " Unknown tool"
        else:
            result = TOOLS[tool_name](**args)

        result_str = str(result)

        if len(result_str) > MAX_TOOL_OUTPUT:
            result_str = result_str[:MAX_TOOL_OUTPUT]

        print(f"\nTool: {tool_name}")
        print(result_str[:300])

        # Add messages
        messages.append({"role": "assistant", "content": output})
        messages.append({"role": "tool", "content": result_str})

        # Fast-path for list_files
        if tool_name == "list_files":
            print("\nFinal Answer:\n")
            if isinstance(result, list):
                print("\n".join(result))
            else:
                print(result)

            return

        if tool_name == "read_file":
            print("\nFinal Answer:\n")
            print(result)
            return

    print(" Max steps reached.")


# ------------------------
# CLI LOOP
# ------------------------

if __name__ == "__main__":
    print("Local Agent")
    print("Type 'exit' to quit\n")

    while True:
        query = input(">>> ")
        if query.lower() == "exit":
            break
        run_agent(query)
