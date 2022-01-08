import os

from constants import audio_path

from data_prep.helper_functions import get_all_files_info

if __name__ == '__main__':

    print(f"audio_path={audio_path}")

    # Get files from directory
    files = os.listdir(audio_path)
    print(f"Found {len(files):,} files")

    # File information
    file_info = get_all_files_info(files)


