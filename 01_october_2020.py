# selection of functions created in October 2020
# my very first functions :)

# 5 functions to solve puzzles from https://www.codewars.com/

def longest(s1, s2):        # 7 kyu
    '''
    task:
    Take 2 strings s1 and s2 including only letters from a to z.
    Return a new sorted string, the longest possible, containing distinct letters -
    each taken only once - coming from s1 or s2.

    from: https://www.codewars.com/kata/5656b6906de340bd1b0000ac
    '''

    abc = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    string = ''
    for i in range(len(abc)):
        if abc[i] in s1 or abc[i] in s2:
            string = string + abc[i]
    return string


def reverse_letter(string):   # 7 kyu
    '''
    task:
    Given a string str, reverse it omitting all non-alphabetic characters.

    from: https://www.codewars.com/kata/58b8c94b7df3f116eb00005b
    '''
    reversed = ''
    length = len(string)
    for m in range(length):
        reversed = reversed + string[(length - 1) - m]
    abc = 'abcdefghijklmnopqrstuvwxyz'
    reversed_cleaned = ''
    for n in range(length):
        if reversed[n] in abc:
            reversed_cleaned += reversed[n]
    return reversed_cleaned


def hello(name=''):         # 8 kyu
    '''
    task:
    Define a method hello that returns "Hello, Name!" to a given name,
    or says Hello, World! if name is not given (or passed as an empty String)

    from: https://www.codewars.com/kata/57e3f79c9cb119374600046b
    '''
    if len(name) == 0:
        return 'Hello, World!'
    ls = list(name)
    word = True
    for i in range(len(ls)):
        word = word and ls[i].isalpha()
    if word == True:
        return 'Hello, ' + name[0].upper() + name[1:].lower() + '!'


def get_strings(city):      # 7 kyu
    '''
    task:
    You receive the name of a city as a string, and you need to return a string
    that shows how many times each letter shows up in the string by using asterisks (*).

    from: https://www.codewars.com/kata/5b358a1e228d316283001892
    '''
    short = city.replace(' ','')    # remove spaces
    name = short.lower()            # lowercase letters
    long = ''
    for i in range(len(name)):
        long += name[i] + ':' + '*'*name.count(name[i]) + ','    # add stars according to number of occasions
    ls = long.split(',')        # make an array (coma as split)
    result = []                # new array
    print(ls)
    for x in range(len(ls)):
        if ls[x] not in result:
            result.append(ls[x])     # append only first occasions
    del result [-1]                # remove last char ('')
    return ','.join(result)         # join to string


def dative(word):               # 7 kyu
    '''
    task:
    Your goal is to create a function dative() which returns the valid form of a valid Hungarian word w in dative case
    i. e. append the correct suffix nek or nak to the word w based on vowel harmony rules.

    from: https://www.codewars.com/kata/57fd696e26b06857eb0011e7
    '''
    reverse = word[::-1]
    string_nek = 'eéiíöőüű'
    string_nak = 'aáoóuú'
    nek = ''
    nak = ''
    for index in range(8):
        if string_nek[index] in reverse:
            nek += str(reverse.index(string_nek[index]))
        else:
            nek += '9'
    for index in range(6):
        if string_nak[index] in reverse:
            nak += str(reverse.index(string_nak[index]))
        else:
            nak += '9'
    ls_nek = list(nek)
    ls_nak = list(nak)
    int_nek = list(map(int,ls_nek))
    int_nak = list(map(int,ls_nak))
    sorted_nek = int_nek.sort()
    sorted_nak = int_nak.sort()
    for i in range(len(ls_nek)):
        if int_nek[i] < int_nak [i]:
            return word + 'nek'
        else:
            return word + 'nak'
