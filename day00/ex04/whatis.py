import sys

def is_valid_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    argc = len(sys.argv)
    assert argc <= 2, "more than one argument is provided"
    if (argc != 2):
        return
    
    assert is_valid_integer(sys.argv[1]), "argument is not an integer"

    if int(sys.argv[1]) % 2:
        print("I'm Odd")
    else:
        print("I'm Even")

if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")