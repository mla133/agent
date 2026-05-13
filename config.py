# ------------------------
# AGENT LIMITS
# ------------------------

# Maximum number of reasoning/tool steps per request
MAX_STEPS = 12

# Maximum number of characters returned from any tool
# Prevents blowing up the context window
MAX_TOOL_OUTPUT = 4000


# ------------------------
# MODEL/OUTPUT SAFETY
# ------------------------

# Hard limit on model output length before truncation
MAX_MODEL_OUTPUT = 8000

# Enable fallback detection when model fails JSON
ENABLE_FALLBACK_COMPLETION = True


# ------------------------
# TOOL BEHAVIOR LIMITS
# ------------------------

# Max files returned from list_files
MAX_FILES = 50

# Max lines to read from a file
MAX_FILE_LINES = 150

# Max matches from search_files
MAX_SEARCH_RESULTS = 20


# ------------------------
# LOOP / SAFETY CONTROLS
# ------------------------

# Stop if same tool is called repeatedly
ENABLE_LOOP_DETECTION = True

# Force completion if agent stalls
FORCE_COMPLETION_ON_REPEAT = True

# Detect useless search loops
ENABLE_SEARCH_LOOP_BREAK = True


# ------------------------
# DEBUG / LOGGING
# ------------------------

# Print tool outputs in console
VERBOSE_TOOL_OUTPUT = True

# Print reasoning steps
VERBOSE_REASONING = True
