import os
import mutagen
from mutagen.id3 import ID3NoHeaderError
from mutagen.mp3 import HeaderNotFoundError
from termcolor import colored, cprint
from mutagen.easyid3 import EasyID3


def normalize_text(string):
    string = string.replace("|", '')
    string = string.replace("+", '')
    string = string.replace("(", '')
    string = string.replace(")", '')
    string = string.replace("~", ' ')
    string = string.replace(":", '')
    string = string.replace("-", '')
    string = string.replace("?", '')
    string = string.replace("/", '')
    string = string.replace("&", 'and')
    string = string.replace("\"", '')
    string = string.replace("\'", '')
    return string.strip().lower()


def rename_mp3_files():
    global old_filepath, id3info, meta
    location = "/media/victor/Storage/Music"
    for root, dirs, files in os.walk(location):
        for m_file in files:
            old_filepath = os.path.join(root, m_file)
            try:
                meta = EasyID3(old_filepath)
            except ID3NoHeaderError:
                try:
                    meta = mutagen.File(old_filepath, easy=True)
                except HeaderNotFoundError as e:
                    continue
            try:
                meta.save(old_filepath)
            except AttributeError:
                pass
            try:
                title = str(meta['title'][0])
            except (KeyError, OSError, TypeError):
                continue

            new_filename = f"{normalize_text(title)}.mp3"
            new_filepath = os.path.join(root, new_filename)
            os.rename(old_filepath, new_filepath)
            cprint(colored(f"[+] {old_filepath} -> {new_filename}", 'green'))
