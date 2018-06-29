import string
import argparse

def test_string(s):
    assert(s is not None)
    assert(s.isalpha())

def reverse_string(s):
    return s[::-1]

def reverse_string_using_join(s):
    return ''.join(reversed(s))

def is_palindrome(s, m):
    
    test_string(s)

    if m is 'j':
        method = reverse_string_using_join
    else:
        method = reverse_string

    reverse_s = method(s)

    if (s == reverse_s):
        return True
    return False


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This script evaluates a string of alphabetic characters '
                                                 'and returns True/False if it is a palindrome.')
    parser.add_argument('-s', '--string', help='Provide string for palindrome check', required=True)
    parser.add_argument('-m', '--method', help='Specify reverse method for string, either "j" for join or "r" for index reverse', required=False, default='r')
    args = parser.parse_args()

    STRING = args.string
    METHOD = args.method

    print is_palindrome(STRING, METHOD)
