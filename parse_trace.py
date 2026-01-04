import re

def normalize(line):
    
    # ---------------------------------------------------
    # Extract the syscall name using a regular expression
    # ---------------------------------------------------
    # Example line:
    #   "7577 20:30:38.703575 execve("/usr/bin/python3", [....]) = 0"
    #
    # Regex logic:
    # .*? - skips timestamp and PID parse_trace
    # \s+ = one or more spaces
    # ([a-zA-Z0-9_]+)\( - capture the syscall name before '('
    match = re.match(r'.*?\s+([a-zA-Z0-9_]+)\(', line) 
    
    # If the line doesn’t contain a syscall (maybe an error or incomplete line)
    # Skip it
    if not match:
        return None
    
    # Extract the syscall name from the regex expressiom
    syscall = match.group(1)

    # ---------------------------------------------------------
    # Normalize volatile data
    # ---------------------------------------------------------
    # Replace values that change between runs with placeholders
    # so traces become comparable and consistent.
    #
    # Examples of volatile data:
    #   - Memory addresses:    0x7ffc9b7c1000
    #   - Numbers:             process IDs, return codes, etc.
    #   - Strings:             file paths, command-line args, etc.
    line = re.sub(r'0x[0-9a-fA-F]+', '<HEX>', line) # Memory address
    line = re.sub(r'\d+', '<NUM>', line)  # Numbers (PIDs, FDs, etc)
    line = re.subn(r'\".*?\"', '<STR>', line)  # Strings or file paths

    # Return only the syscall name, tokens are built from these
    return syscall

def parse_trace(file_path):
    tokens = []

    # ---------------------------------------------------------
    # Read each line from the strace output file
    # ---------------------------------------------------------
    with open(file_path) as f:
        for line in f:
            # Normalize and extract syscall from each line
            syscall = normalize(line)

            # If a valid syscall was found, store it
            if syscall:
                tokens.append(syscall)

    # ---------------------------------------------------------
    # The final token list might look like:
    # ['execve', 'brk', 'mmap', 'access', 'openat', 'fstat', ...]
    # ---------------------------------------------------------
    return tokens








