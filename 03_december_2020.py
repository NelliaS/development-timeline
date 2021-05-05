# Selection of functions created in December 2020

# 3 functions to solve puzzles from https://www.codewars.com/
# I've started to write code simplier and it also has better logic :)

def song_decoder(song):     # 6 kyu
    '''
    task:
    Polycarpus inserts a certain number of words "WUB" before the first word of the song
    (the number may be zero), after the last word (the number may be zero),
    and between words (at least one between any pair of neighbouring words),
    and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
    Restore original song.

    from: https://www.codewars.com/kata/551dc350bf4e526099000ae5
    '''
    array = song.split('WUB')
    for empty_cell in range(array.count('')):
        array.remove('')
    original = ' '.join(array)
    return original


def tickets(people):       # 6 kyu
    Vasya = []
    for received_money in people:
        if received_money == 25:
            Vasya.append(received_money)
        elif received_money == 50:
            if 25 in Vasya:
                Vasya.remove(25)
                Vasya.append(received_money)
            else:
                return 'NO'
        else:
            if 50 in Vasya and 25 in Vasya:
                Vasya.remove(25)
                Vasya.remove(50)
            elif Vasya.count(25) == 3:
                for i in range(3):
                    Vasya.remove(25)
            else:
                return 'NO'
    return 'YES'


def find_uniq(arr):     # 6 kyu
    '''
    task:
    Implement the function unique_in_order which takes as argument a sequence and
    returns a list of items without any elements with the same value next to each
    other and preserving the original order of elements.

    from: https://www.codewars.com/kata/54e6533c92449cc251001667
    '''
    for i, char in enumerate(arr):
        try:
            if char != arr[i+1] and char != arr[i+2]:
                return char
        except IndexError:
            if char != arr[i-1]:
                return char


# 2 days of solving puzzles from https://adventofcode.com/


# Day 4 - before I've learnt RegEx

batch = []

with open('day_4.txt') as f:
    one_entry = []
    for line in f:
        if line != '\n':
            line = line.rstrip().split(' ')
            for item in line:
                one_entry.append(item)
        else:                           # note that 2 blank lines need to be added at the end of day_4.txt
            batch.append(one_entry)
            one_entry = []


def count_valid(batch):
    valid = 0
    for entry in batch:
        dictionary = {}
        for item in entry:
            key = item[:item.index(':')]
            value = item[item.index(':')+1:]
            dictionary.setdefault(key, value)
        if (len(dictionary.keys()) == 7 and 'cid' not in dictionary.keys()) or (len(dictionary.keys()) == 8):
            valid += 1
    return valid                # 242

print(count_valid(batch))


def count_valid2(batch):
    valid = 0
    for entry in batch:
        dictionary = {}
        for item in entry:
            key = item[:item.index(':')]
            value = item[item.index(':')+1:]
            dictionary.setdefault(key, value)
        if (len(dictionary.keys()) == 7 and 'cid' not in dictionary.keys()) or (len(dictionary.keys()) == 8):
            valid += validate(dictionary)
    return valid                                # 186


def validate(dictionary):
    byr_value = dictionary['byr']
    iyr_value = dictionary['iyr']
    eyr_value = dictionary['eyr']
    hgt_value = dictionary['hgt']
    hcl_value = dictionary['hcl']
    ecl_value = dictionary['ecl']
    pid_value = dictionary['pid']
    try:
        if len(byr_value) != 4 or int(byr_value) not in range(1920, 2003):
            return 0
        if len(iyr_value) != 4 or int(iyr_value) not in range(2010, 2021):
            return 0
        if len(eyr_value) != 4 or int(eyr_value) not in range(2020, 2031):
            return 0
        if 'cm' not in hgt_value and 'in' not in hgt_value:
            return 0
        if 'cm' in hgt_value and int(hgt_value[:-2]) not in range(150, 194):
            return 0
        if 'in' in hgt_value and int(hgt_value[:-2]) not in range(59, 77):
            return 0
        if hcl_value[0] != '#' or len(hcl_value) != 7:
            if hcl_value.isdigit() is False:
                return 0
            else:
                for char in hcl_value[1:]:
                    if char not in 'abcdef':
                        return 0
        if ecl_value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return 0
        if len(pid_value) != 9 or pid_value.isdigit() is False:
            return 0
    except ValueError:
        return 0
    else:
        return 1

print(count_valid2(batch))


# Day 12 - after I've started finally using docstrings

import turtle

instructions = []
with open('day_12.txt') as f:
    for line in f:
        line = line.rstrip().lower()
        instructions.append(line.rstrip())


def turtle_move_easy(instructions):
    '''Instructions - [n - north, s - south, e - east, w - west, l - left, r - right, f - forward] + number,
    make appropriate moves and return position of turtle (x,y)'''
    ship = turtle.Turtle()
    ship.speed(0)
    for move in instructions:
        number = int(move[1:])
        instr = move[0]
        if instr in 'nsew':
            x = ship.xcor()
            y = ship.ycor()
            if instr == 'n':
                y += number
            elif instr == 's':
                y -= number
            elif instr == 'e':
                x += number
            else:
                x -= number
            ship.goto(x,y)
        elif instr == 'r':
            ship.rt(number)
        elif instr == 'l':
            ship.lt(number)
        else:       # f
            ship.fd(number)
    return abs(ship.xcor()) + abs(ship.ycor())


print(turtle_move_easy(instructions))


def rotate(instr, number, x_r, y_r):
    '''Helping function double_turtle(), doing rotations of relative distance between 2 turtles'''
    if number in (90, 270):
        if number == 90 and instr == 'r' or number == 270 and instr == 'l':
            x_r, y_r = y_r, -x_r
        else:
            x_r, y_r = -y_r, x_r
    else:               # 180
        x_r, y_r = -x_r, -y_r
    return x_r, y_r


def double_turtle(instructions):
    '''two turtles - ship, waypoint; with ship, waypoint moves also,
    instructions:
        f move ship in direction of waypoint (in number given times),
        n / s / e / w - moves waypoint in number given,
        r / l rotates waypoint around ship - ..... ?
    '''
    waypoint = turtle.Turtle()
    waypoint.shape('triangle')
    ship = turtle.Turtle()
    ship.shape('turtle'), ship.speed(0)
    waypoint.speed(0), waypoint.pu(), waypoint.goto(10,1)       # origin => x = 10, y = 1
    for move in instructions:
        number = int(move[1:])
        instr = move[0]
        x_w = int(waypoint.xcor())          # waypoint coordinates
        y_w = int(waypoint.ycor())
        x_s = int(ship.xcor())              # ship coordinates
        y_s = int(ship.ycor())
        x_r = x_w - x_s                  # distance between ship and waypoint
        y_r = y_w - y_s
        if instr == 'f':
            x_s += x_r * number
            y_s += y_r * number
            ship.goto(x_s, y_s)
            x_w = x_s + x_r
            y_w = y_s + y_r
            waypoint.goto(x_w, y_w)
        elif instr in 'nsew':
            if instr == 'n':
                y_w += number
            elif instr == 's':
                y_w -= number
            elif instr == 'e':
                x_w += number
            else:
                x_w -= number
            waypoint.goto(x_w, y_w)
        else:
            x_r, y_r = rotate(instr, number, x_r, y_r)
            x_w = x_s + x_r
            y_w = y_s + y_r
            waypoint.goto(x_w, y_w)
    print(f'final: ship:{x_s}, {y_s}')
    print(f'final: waypoint:{x_w}, {y_w}')
    print(f'final: distance between:{x_r}, {y_r}')
    return abs(ship.xcor()) + abs(ship.ycor())


print(double_turtle(instructions))