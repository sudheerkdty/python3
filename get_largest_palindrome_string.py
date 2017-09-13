
def get_largest_palindrome_string(word):
    """(str) -> (str)
    Returns the largest palindrome of a given word

    check_palindrome("popboobloooolvaaaaaav")
    >>>vaaaaaav
    check_palindrome("doodle")
    >>>dood

    """
    palindrome = ""
    for count in range(len(word)):
        for index in range(len(word)):
            substring = word[count:index+1]

            if len(substring) <=1:
                pass
            elif substring == substring[::-1]:

                if len(substring) > len(palindrome):
                    palindrome = substring
    return palindrome

if __name__ == '__main__':
    word = input("Enter a string\n>>>")
    print(get_largest_palindrome_string(word))

