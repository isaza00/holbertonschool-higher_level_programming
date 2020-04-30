#!/usr/bin/python3
def arguments(args):
    if len(args) <= 1:
            print("0 arguments.")
    else:
        if (len(args)) == 2:
                print(len(args) - 1, "argument:")
        else:
            print(len(args) - 1, "arguments:")

        for i, a in enumerate(args[1:], start=1):
            print("{}: {}".format(i, a))

if __name__ == "__main__":
    import sys
    arguments(sys.argv)
