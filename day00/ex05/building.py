import sys
import string


def get_user_input() -> str:
    """
    Read the input from the user otherwise prompt for input
    """
    argc = len(sys.argv)

    if argc > 2:
        raise AssertionError("Too many arguments")
    elif argc == 2:
        return sys.argv[1]
    
    print("What is the text to count?")
    content: list[str] = []
    try:
        while True:
            content.append(input())
    except EOFError:
        return ' '.join(content).replace('\n', ' ')


def get_result(content: str):
    """
    Count the type of each character in a string
    """
    result = {
        'total': len(content),
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'space': 0,
        'digit': 0
    }

    for char in content:
        if char.isupper():
            result['upper'] += 1
        elif char.islower():
            result['lower'] += 1
        elif char.isdigit():
            result['digit'] += 1
        elif char == ' ':
            result['space'] += 1
        elif char in string.punctuation:
            result['punctuation'] += 1
    return result


def main():
    user_input = get_user_input()
    if (len(user_input) == 0):
        raise AssertionError("invalid input")
    result = get_result(user_input)
    print(f"""The text contains {result['total']} characters:
{result['upper']} upper letters
{result['lower']} lower letters
{result['punctuation']} punctuation marks
{result['space']} spaces
{result['digit']} digits""")


if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}", file=sys.stderr)
