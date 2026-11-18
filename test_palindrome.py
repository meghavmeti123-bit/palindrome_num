import sys

def palindrome(num):
    rev = num[::-1]

    if num == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

if __name__ == "__main__":
    num = sys.argv[1]
    result = palindrome(num)
    print(result)