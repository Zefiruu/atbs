import random
def coinFlip(nFlips):
    i = 0
    string = ''
    while i < nFlips:
        i += 1
        rand = random.randint(0,1)
        if rand == 0:
            string += 'H'
        else: 
            string += 'T'
    previousJ = ''
    countJ = 1
    streak6 = 0
    for j in string:
        if countJ == 6:
            streak6 += 1
            countJ = 1
        elif j == previousJ:
            countJ += 1
        else:
            countJ = 1
        previousJ = j
    x = (streak6*100)/nFlips

    print(streak6, 'The likelihood of getting the same side of the coin in a row is: ' + str(x) + '%')

coinFlip(100)