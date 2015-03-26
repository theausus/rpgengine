import os
def roll(sides, times):
    roll_list = []
    num_bits = int.bit_length(sides)
    mask = 2 ** num_bits - 1
    rand_size = num_bits // 8 + 1
    for i in range(times):
        random_byte = os.urandom(rand_size)
        random_number = mask & int.from_bytes(random_byte, byteorder="big")
        if random_number > sides or random_number == 0:
            random_number = roll(sides, 1)[0]
        roll_list.append(random_number)
    return roll_list

def parser(input_string):
    input_list = input_string.split(" ")
    total = 0
    for s in input_list:
        if "d" in s:
            parse_this = s.split("d")
            dice_roll = roll(int(parse_this[1]), int(parse_this[0]))
            print(dice_roll)
            total += sum(dice_roll)
        elif "+" in s:
            total += int(s[1:])
        elif "-" in s:
            total += -1 * int(s[1:])
        elif "*" in s:
            total = total * int(s[1:])
        elif "/" in s:
            total = total / int(s[1:])
        elif "note" in s:
            notekeeper()
            return "Now in normal mode again"
        else:
            return "Unknown symbol at " + s
    return total

def notekeeper():
    print("What to name your note?\n(It will erase any existing note of the same name)")
    filename = input("? >")
    line_to_write = ""
    try:
        data_home = os.environ['XDG_DATA_HOME']
        print("Writing to " + filename + " in $XDG_DATA_HOME")
        file = open(data_home + "/" + filename, 'w')
    except:
        home = os.environ['HOME']
        print("Writing to " + filename + " in $HOME/.local/share/\nTo return to normal mode, enter a line only containing a '.'")
        file = open(home + "/.local/share/" + filename, 'w')
    file.truncate()
    while line_to_write != ".":
        line_to_write = input("> >")
        file.write(line_to_write)
        file.write("\n")
    print("Finishing up with " + filename)
    file.close()
