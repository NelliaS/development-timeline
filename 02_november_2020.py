# Selection of functions created in October 2020
# I've learnt a lot Python functionalities :)

# 5 functions to solve puzzles from https://www.codewars.com/

def likes(names):       # 6 kyu
    '''
    task:
    Implement a function likes :: [String] -> String, which must take in input array,
    containing the names of people who like an item.

    from: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
    '''

    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) > 3:
        number_of_others = len(names) - 2
        return f'{names[0]}, {names[1]} and {number_of_others} others like this'


def alphabet_position(text):   # 6 kyu
    '''
    task:
    In this kata you are required to, given a string, replace every letter with its position in the alphabet.

    from: https://www.codewars.com/kata/546f922b54af40e1e90001da
    '''

    from string import ascii_lowercase as abc
    new_text = ''
    output = ''
    for char in text:
        if char.isalpha() is True:
            new_text += char.lower()
    for char in new_text:
        output += str(abc.index(char) + 1) + ' '
    return output[:-1]


def make_readable(sec):         # 5 kyu
    '''
    task:
    Write a function, which takes a non-negative integer (seconds) as input
    and returns the time in a human-readable format (HH:MM:SS).

    from: https://www.codewars.com/kata/52685f7382004e774f0001f7
    '''
    seconds = sec % 60
    minutes = (sec // 60) % 60
    hours = (sec // 60) // 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hours < 10:
        hours = '0' + str(hours)
    return f'{hours}:{minutes}:{seconds}'


def scramble(s1, s2):           # 5 kyu
    '''
    task:
    Complete the function scramble(str1, str2) that returns true if a portion of str1 characters
    can be rearranged to match str2, otherwise returns false.

    from: https://www.codewars.com/kata/55c04b4cc56a697bb0000048
    '''
    from string import ascii_lowercase as abc
    letters = list(abc)
    count_s1 = []
    count_s2 = []
    for i in range(len(letters)):
        count_s1.append(s1.count(letters[i]))
    for i in range(len(letters)):
        count_s2.append(s2.count(letters[i]))
    dict_s1 = dict(zip(letters, count_s1))
    dict_s2 = dict(zip(letters, count_s2))
    for letter in s2:
        if dict_s2[letter] <= dict_s1[letter]:
            pass
        else:
            return False
    return True


def generate_hashtag(string):       # 5 kyu
    '''
    task:
    Let's help them with our own Hashtag Generator!
    Here's the deal:
        It must start with a hashtag (#).
        All words must have their first letter capitalized.
        If the final result is longer than 140 chars it must return false.
        If the input or the result is an empty string it must return false.

    from: https://www.codewars.com/kata/52449b062fb80683ec000024
    '''
    if not string:
        return False
    string = string.title()
    array = string.split()
    string = ''.join(array)
    string = f'#{string}'
    if len(string) > 140:
        return False
    else:
        return string