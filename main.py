import os

from constants import audio_path
print(f"audio_path={audio_path}")

# Get files from directory
files = os.listdir(audio_path)
print(f"Found {len(files):,} files")
