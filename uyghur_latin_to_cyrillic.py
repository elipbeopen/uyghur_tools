import argparse

INFILE = "Uyghur_intonation_list.txt"
OUTFILE = "cyrillic_uyghur_intonation_list.txt"

MAP_1 = {
    "A": "А",
    "a": "а",
    "E": "Ә",
    "e": "ә",
    "B": "Б",
    "b": "б",
    "P": "П",
    "p": "п",
    "T": "Т",
    "t": "т",
    "J": "Җ",
    "j": "җ",
    "X": "Х",
    "x": "х",
    "D": "Д",
    "d": "д",
    "R": "Р",
    "r": "р",
    "Z": "З",
    "z": "з",
    "S": "С",
    "s": "с",
    "F": "Ф",
    "f": "ф",
    "Q": "Қ",
    "q": "қ",
    "K": "К",
    "k": "к",
    "G": "Г",
    "g": "г",
    "L": "Л",
    "l": "л",
    "M": "М",
    "m": "м",
    "N": "Н",
    "n": "н",
    "H": "Һ",
    "h": "һ",
    "O": "О",
    "o": "о",
    "U": "У",
    "u": "у",
    "Ö": "Ө",
    "ö": "ө",
    "Ü": "Ү",
    "ü": "ү",
    "W": "В",
    "w": "в",
    "É": "Е",
    "é": "е",
    "I": "И",
    "i": "и",
    "Y": "Й",
    "y": "й"
}

MAP_2 = {
    "Ng": "Ң",
    "ng": "ң",
    "Sh": "Ш",
    "sh": "ш",
    "Gh": "Ғ",
    "gh": "ғ",
    "Zh": "Ж",
    "zh": "ж",
    "Ch": "Ч",
    "ch": "ч"
}

def convert_latin_to_cyrillic(infile, outfile):
    with open(infile, "r") as f:
        file = f.read()

    # Replace all two character sequences
    for key in MAP_2:
        file = file.replace(key, MAP_2[key])

    # Remove miscellaneous characters
    file = file.replace("'", "")
    file = file.replace("=", "")
    file = file.replace("’", "")


    # Replace all one character sequences
    for key in MAP_1:
        file = file.replace(key, MAP_1[key])

    with open(outfile, "w") as f:
        f.write(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert latin Uyghur script to cyrillic")
    parser.add_argument("infile", type=str, help="The file to read latin script from")
    parser.add_argument("outfile", type=str, help="The file to write cyrillic script to", default=1)
    args = parser.parse_args()
    convert_latin_to_cyrillic(args.infile, args.outfile)