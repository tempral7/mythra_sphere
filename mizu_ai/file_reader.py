# file_reader.py – read and lightly summarize Python files

import os

def read_file(path):
    """
    Read the entire file at `path`.
    Returns its text, or an error message if not found.
    """
    if not os.path.isfile(path):
        return f"❌ Error: File '{path}' not found."
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def summarize_file(path, max_lines=10):
    """
    Return the first `max_lines` of the file for a quick preview.
    Splits by newline and joins the first few lines.
    """
    content = read_file(path)
    if content.startswith("❌"):
        return content  # pass error upstream
    lines = content.splitlines()
    preview = lines[:max_lines]
    return "\n".join(preview) or "(file is empty)"
