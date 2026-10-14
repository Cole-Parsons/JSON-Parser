# exit w/ 0 for valid json
# exit w/ 1 for invalid json

PUNCTUATIONS = ("{", "}", ":", ",")

import sys

test_filepath = sys.argv[1]

def lex(text):
    tokens = []
    i = 0
    while i < len(text):
        c = text[i]

        if c.isspace():
            i += 1

        elif c == PUNCTUATIONS[3]:
            if not text[i + 1].isalpha():
                sys.exit("Invalid JSON, impropper comma location")

        elif c in PUNCTUATIONS:
            tokens.append(c)
            i += 1

        elif c == '"':
            i += 1
            token_start = i
            
            while i < len(text) and text[i] != '"':
                i += 1

            if i == len(text):
                sys.exit("Invalid JSON, reached end of string w/o }")
            else:
                tokens.append(text[token_start:i - 1])
                i += 1
        else:
            sys.exit("Invalid JSON, failed")
    print("lex finished")

#finish elif from cluade >>>

def main():
    print("start")

    with open(test_filepath) as f:
        contents = f.read()

    print(repr(contents))

    if not contents:
        sys.exit("Invalid JSON, file empty")

    lex(contents)

if __name__ == "__main__":
    main()