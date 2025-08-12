"""
File utility functions.
"""
import os

def file_exists(path):
    return os.path.exists(path)

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
