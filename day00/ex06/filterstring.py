import sys
from ft_filter import ft_filter


def main():
    assert len(sys.argv) == 3, "invalid number of arguments 2 expected"
    try:
        count = int(sys.argv[2])
        gen = ft_filter(lambda val: len(val) >= count, sys.argv[1].split())
        print([item for item in gen])
    except ValueError:
        raise AssertionError("the second argument must be an integer")

    

if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}", file=sys.stderr)