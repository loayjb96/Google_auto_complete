import os
import re
import json
# files_names = {}


def fill_trie_base():
    regex = re.compile('[^a-zA-Z\n\s]')
    l = []
    with open("C:/Users/loay-/PycharmProjects/play_ground/files_name.json", "a") as file_names:
        file_names.write("[")
    with open("C:/Users/loay-/PycharmProjects/play_ground/Compined_Suffixes.json", "a") as file:
        file.write("[")
    for data, name in read_files():
        index = 0

        for line in data.split('\n'):
            save_line = line[:]
            # global files_names
            if save_line != "|n":
                with open("C:/Users/loay-/PycharmProjects/play_ground/files_name.json", "a") as file_names:
                    json.dump({save_line: name}, file_names)
                    file_names.write(",")

            # files_names[save_line] = name
            line = regex.sub('', line)
            line = line.lower()
            line = line
            line = line.split(" ")
            suffixes = all_suffixes(" ".join(line))
            for i, string in enumerate(suffixes):
                suffixes[i] = string + "\n"
            suffixes.append("\n")
            if save_line != "":
                l.append({index: suffixes})
            index += 1
        with open("C:/Users/loay-/PycharmProjects/play_ground/Compined_Suffixes.json", "a") as file:
            json.dump({name: l}, file)
            file.write(",")
    with open("C:/Users/loay-/PycharmProjects/play_ground/Compined_Suffixes.json", "rb+") as file:
        file.seek(-1, os.SEEK_END)
        file.truncate()

    with open("C:/Users/loay-/PycharmProjects/play_ground/Compined_Suffixes.json", "a") as file:
        file.write("]")

    with open("C:/Users/loay-/PycharmProjects/play_ground/files_name.json", "rb+") as file_names:
        file_names.seek(-1, os.SEEK_END)
        file_names.truncate()
    with open("C:/Users/loay-/PycharmProjects/play_ground/files_name.json", "a") as file_names:
        file_names.write("]")


def read_files():
    for subdir, dirs, files in os.walk("C:/Users/loay-/Desktop/Google_Progect/small"):
        for file in files:
            with open(os.path.join(subdir, file), encoding="utf8") as f:
                data = f.read()
                print(os.path.join(subdir, file))
                yield data, file


def all_suffixes(s):
    return [s[-i:] for i in range(1, len(s)+1,2)]


fill_trie_base()