# Selection of functions created in March 2021

# 5 functions to solve puzzles from https://www.codewars.com/
# I've been learning RegExes :)

def nickname_generator(name):           # 7 kyu
    '''
    task:
    Write a function, nicknameGenerator that takes a string name as an argument
    and returns the first 3 or 4 letters as a nickname.
    If the 3rd letter is a consonant, return the first 3 letters.

    from: https://www.codewars.com/kata/593b1909e68ff627c9000186
    '''
    import re
    if len(name) < 4:
        return "Error: Name too short"
    else:
        return ''.join(re.findall("(?:^..[^aeiou])|(?:^....)", name))


def read_zalgo(zalgotext):        # 7 kyu
    '''
    task:
    Complete the function that converts a string of Zalgo text into a
    string interpretable by our mortal eyes.

    from: https://www.codewars.com/kata/588fe9eaadbbfb44b70001fc
    '''
    import re
    return re.sub('[^a-zA-Z !?.,]', '', zalgotext)


def to_cents(amount):     # 7 kyu
    '''
    task:
    Implement String#to_cents, which should parse prices expressed as $1.23 and return number of cents,
    or in case of bad format return nil.

    from: https://www.codewars.com/kata/56833b76371e86f8b6000015
    '''
    import re
    if "\n" in amount:
        return None
    for match in re.findall(r"^\$([0-9]+?).([0-9][0-9])$", amount):
        output = ''.join(match)
        return int(output)
    else:
        return None


def has_subpattern(string):       # 6 kyu
    '''
    task:
    In this kata you need to build a function to return either true/True or false/False
    if a string can be seen as the repetition of a simpler/shorter subpattern or not.

    from: https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b
    '''

    import re
    return bool(re.search(r"^(.+)\1+$", string))


def is_valid_coordinates(coordinates):          # 6 kyu
    '''
    task:
    You need to create a function that will validate if given parameters are valid geographical coordinates.
    Valid coordinates look like the following: "23.32353342, -32.543534534".
    The return value should be either true or false.
    Latitude (which is first float) can be between 0 and 90, positive or negative.
    Longitude (which is second float) can be between 0 and 180, positive or negative.
    Coordinates can only contain digits, or one of the following symbols (including space after comma) __ -, . __
    There should be no space between the minus "-" sign and the digit after it.

    from: https://www.codewars.com/kata/5269452810342858ec000951
    '''
    import re
    return bool(re.fullmatch("^-?(?:[0-8]?[\d]|[9][0])\.?\d*[,__\s-]?\s?-?(?:\d?\d|17\d|180)(?:\.?\d*)$", coordinates))

