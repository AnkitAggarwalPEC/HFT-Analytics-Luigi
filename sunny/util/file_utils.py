import os

def check_if_file_present(path):
    """
    Utility to check if file present at the path specified
    """
    return os.path.exists(path) and os.path.isfile(path)

