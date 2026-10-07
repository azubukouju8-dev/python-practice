# Exercise 7: File handling
# Writes, appends and reads a text file, saves and loads JSON,
# and handles a missing file safely.

import json
from pathlib import Path

# Build file paths relative to this script, so it works from any folder
BASE_DIR = Path(__file__).parent
NOTES_FILE = BASE_DIR / "notes.txt"
DATA_FILE = BASE_DIR / "profile.json"


def write_notes(lines):
    """Create (or overwrite) the notes file with one note per line."""
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def append_note(line):
    """Add one note to the end of the notes file."""
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(line + "\n")


def read_lines(path):
    """Return the lines of a file as a list, or None if the file is missing."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return None


def save_json(data):
    """Save a dictionary to a JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_json():
    """Load a dictionary back from the JSON file."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    write_notes(["Learn Python basics", "Build a practice repository"])
    append_note("Write automated tests")

    notes = read_lines(NOTES_FILE)
    print("Notes in file:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")
    print("Total notes:", len(notes))

    profile = {"name": "Uju", "skills": ["Python", "n8n", "Supabase"]}
    save_json(profile)
    loaded = load_json()
    print("Loaded from JSON:", loaded)
    print("Skills count:", len(loaded["skills"]))

    print("Missing file:", read_lines(BASE_DIR / "does_not_exist.txt"))