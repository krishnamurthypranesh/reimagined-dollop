inp = ['UDDDUDUU', 'DDUUUUDD',]

def countingValleys(steps: str):
    mountains, valleys, curr_alt = [0,] * 3

    for step in steps:
        if step == 'D':
            if curr_alt == 0: # hiker at sea level, valley start
                valleys += 1

            curr_alt -= 1
        if step == 'U':
            if curr_alt == 0: # hiker at sea level, mountain start
                mountains += 1 
            curr_alt += 1

    return valleys

print(list(map(countingValleys, inp)))
