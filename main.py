# exit w/ 0 for valid json
# exit w/ 1 for invalid json

import sys

test_filepath = sys.argv[1]


def main():
    print("start")

    with open(test_filepath) as f:
        contents = f.read()

    print(repr(contents))

    if not contents:
        sys.exit("Invalid JSON")

    i = 0
    while i < len(contents):
        c = contents[i]
        print(c)
        i += 1

    if contents[0] == "{" and contents[len(contents) - 1] == "}":
        sys.exit(0)
    else:
        sys.exit("Invalid JSON")

if __name__ == "__main__":
    main()