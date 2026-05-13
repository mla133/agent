import sys, os, glob
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Just some ANSI color schemes for use in scripting
# see print_ansi_colors below for usage...

BLACK           = '\033[30m'
RED             = '\033[31m'
GREEN           = '\033[32m'
YELLOW          = '\033[33m'
BLUE            = '\033[34m'
MAGENTA         = '\033[35m'
CYAN            = '\033[36m'
WHITE           = '\033[37m'
BRIGHT_BLACK    = '\033[90m'
BRIGHT_RED      = '\033[91m'
BRIGHT_GREEN    = '\033[92m'
BRIGHT_YELLOW   = '\033[93m'
BRIGHT_BLUE     = '\033[94m'
BRIGHT_MAGENTA  = '\033[95m'
BRIGHT_CYAN     = '\033[96m'
BRIGHT_WHITE    = '\033[97m'
OFF             = '\033[0m'

def color_text(text, color):
    return f"{color}{text}{OFF}"

def get_most_recent_file(directory = None):
    # Set the default directory if none is provided
    if directory is None:
        directory = os.getcwd()

    # Get list of files in the directory
    files = glob.glob(os.path.join(directory, '*'))
    # Get most recent file
    most_recent_file = max(files, key=os.path.getctime)
    return most_recent_file

def print_module_functions(module):
    functions = [name for name in dir(module) if callable(getattr(module, name))]
    print(functions)

def print_ansi_colors():
    print(f'{BLACK}BLACK{OFF}')
    print(f'{RED}RED{OFF}')
    print(f'{GREEN}GREEN{OFF}')
    print(f'{YELLOW}YELLOW{OFF}')
    print(f'{BLUE}BLUE{OFF}')
    print(f'{MAGENTA}MAGENTA{OFF}')
    print(f'{CYAN}CYAN{OFF}')
    print(f'{WHITE}WHITE{OFF}')
    print()
    print(f'{BRIGHT_BLACK}BRIGHT_BLACK{OFF}')
    print(f'{BRIGHT_RED}BRIGHT_RED{OFF}')
    print(f'{BRIGHT_GREEN}BRIGHT_GREEN{OFF}')
    print(f'{BRIGHT_YELLOW}BRIGHT_YELLOW{OFF}')
    print(f'{BRIGHT_BLUE}BRIGHT_BLUE{OFF}')
    print(f'{BRIGHT_MAGENTA}BRIGHT_MAGENTA{OFF}')
    print(f'{BRIGHT_CYAN}BRIGHT_CYAN{OFF}')
    print(f'{BRIGHT_WHITE}BRIGHT_WHITE{OFF}')

def log_write(message):
    sys.stdout.write(f"{message}\n")
    sys.stdout.flush()

def log_info(message):
    sys.stdout.write(f"{YELLOW}{message}{OFF}\n")
    sys.stdout.flush()

def log_status(message):
    sys.stdout.write(f"{GREEN}{message}{OFF}\n")
    sys.stdout.flush()

def log_err(message):
    sys.stdout.write(f"{RED}{message}{OFF}\n")
    sys.stdout.flush()

def log_overwrite(message):
    sys.stdout.write('\r')           # Move cursor to beginning of line
    sys.stdout.write(' ' * 80)       # Clear line with 80 spaces (adjust if needed)
    sys.stdout.write('\r')           # Move cursor back to beginning
    sys.stdout.write(f"{message}")   # Write message 
    sys.stdout.flush()

def writeToFile(file, text):
    file = open(file, "a")
    file.write(text)
    file.write("\n")
    file.close()
