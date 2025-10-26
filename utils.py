import re


def validate_input(value):
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    if not value.strip():
        raise ValueError("Input string cannot be empty")


def tokenize_text(text):
    return re.findall(r"[A-Za-z0-9]+", text.lower())
