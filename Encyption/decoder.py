def decode(encoded):
    decoding = ""
    for letter in encoded:
        if letter == "2":
            decoding = decoding + "a"
        elif letter == "x":
            decoding = decoding + "A"
        elif letter == "`":
            decoding = decoding + "B"
        elif letter == "~":
            decoding = decoding + "b"
        elif letter == "x":
            decoding = decoding + "C"
        elif letter == "@":
            decoding = decoding + "c"
        elif letter == "^":
            decoding = decoding + "D"
        elif letter == "=":
            decoding = decoding + "d"
        elif letter == "'":
            decoding = decoding + "E"
        elif letter == "L":
            decoding = decoding + "e"
        elif letter == "#":
            decoding = decoding + "F"
        elif letter == "/":
            decoding = decoding + "f"
        elif letter == "3":
            decoding = decoding + "G"
        elif letter == "|":
            decoding = decoding + "g"
        elif letter == "d":
            decoding = decoding + "H"
        elif letter == "6":
            decoding = decoding + "h"
        elif letter == "+":
            decoding = decoding + "I"
        elif letter == ">":
            decoding = decoding + "i"
        elif letter == "w":
            decoding = decoding + "J"
        elif letter == "$":
            decoding = decoding + "j"
        elif letter == "?":
            decoding = decoding + "K"
        elif letter == "[":
            decoding = decoding + "k"
        elif letter == "-":
            decoding = decoding + "L"
        elif letter == "c":
            decoding = decoding + "l"
        elif letter == "4":
            decoding = decoding + "M"
        elif letter == ":":
            decoding = decoding + "m"
        elif letter == "<":
            decoding = decoding + "N"
        elif letter == "]":
            decoding = decoding + "n"
        elif letter == ".":
            decoding = decoding + "O"
        elif letter == "M":
            decoding = decoding + "o"
        elif letter == "b":
            decoding = decoding + "P"
        elif letter == "{":
            decoding = decoding + "p"
        elif letter == ",":
            decoding = decoding + "Q"
        elif letter == "_":
            decoding = decoding + "q"
        elif letter == "%":
            decoding = decoding + "R"
        elif letter == "!":
            decoding = decoding + "r"
        elif letter == "*":
            decoding = decoding + "S"
        elif letter == "(":
            decoding = decoding + "s"
        elif letter == "&":
            decoding = decoding + "T"
        elif letter == "1":
            decoding = decoding + "t"
        elif letter == "a":
            decoding = decoding + "U"
        elif letter == "5":
            decoding = decoding + "u"
        elif letter == "k":
            decoding = decoding + "V"
        elif letter == "F":
            decoding = decoding + "v"
        elif letter == "7":
            decoding = decoding + "W"
        elif letter == "I":
            decoding = decoding + "w"
        elif letter == "v":
            decoding = decoding + "X"
        elif letter == "8":
            decoding = decoding + "x"
        elif letter == "g":
            decoding = decoding + "Y"
        elif letter == "s":
            decoding = decoding + "y"
        elif letter == "p":
            decoding = decoding + "Z"
        elif letter == ";":
            decoding = decoding + "z"
        elif letter == "B":
            decoding = decoding + "1"
        elif letter == "r":
            decoding = decoding + "2"
        elif letter == "j":
            decoding = decoding + "3"
        elif letter == "Y":
            decoding = decoding + "4"
        elif letter == "N":
            decoding = decoding + "5"
        elif letter == "o":
            decoding = decoding + "6"
        elif letter == "e":
            decoding = decoding + "7"
        elif letter == "U":
            decoding = decoding + "8"
        elif letter == "Z":
            decoding = decoding + "9"
        elif letter == "J":
            decoding = decoding + "0"
        elif letter == "h":
            decoding = decoding + "."
        elif letter == "T":
            decoding = decoding + ","
        elif letter == "i":
            decoding = decoding + "!"
        elif letter == "y":
            decoding = decoding + "?"

        else:
            decoding = decoding + letter
    return decoding


