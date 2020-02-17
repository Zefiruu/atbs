heartGrid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printHeart(heart):
    x = 0
    y = 0
    string = ''
                    # Printing column by column


    while x <= len(heart[0]):
        try:
            if y == len(heart):
                y = 0
                print(string)
                string = ''    
            while y < len(heart):
                    string += heart[y][x]
                    y += 1
            x += 1
        except:
            pass

                    #  Printing row by row

    # while y < len(heart):
    #     for i in heart[y]:
    #         if x == len(heart[y]) - 1:
    #             x = 0
    #             print(string)
    #             string = ''
    #         else:
    #             string += heart[y][x]
    #             x += 1
    #     y += 1
        
printHeart(heartGrid)