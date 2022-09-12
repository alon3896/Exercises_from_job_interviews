import random
# code by Alon Haim Chitlaru for Nitzanim


# The board of the game, 1 represents a playable place and 0 is an unplayable place
board = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1]]
# the colors of the game "B" = Blue, "p" = pink, "Y"= yellow
colors = ["B", "P", "Y"]
still_playing = False


# function that generates a random pyramid by changing each cell that  equals to 1 to a random color
def build_gameboard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                board[i][j] = random.choice(colors)


# function that prints only the playable pyramid from the board with nested "for" loops
def printer():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print(" ", end=" ")
            else:
                print(board[i][j], end=" ")
        print(" ")


# Boolean function that return True if  there aren't blue cells on the sides of the pyramid
# each side checked separately with "while" loops
def blue_constrain():
    flag = True
    (i, j) = [0, 4]
    while i < len(board):
        if board[i][j] == "B":
            flag = False
            break
        j -= 1
        i += 1
    (i, j) = [0, 4]
    while i < len(board):
        if board[i][j] == "B":
            flag = False
            break
        j += 1
        i += 1
    (i, j) = [4, 0]
    while j < len(board[i]):
        if board[i][j] == "B":
            flag = False
            break
        j += 1
    return flag


# Boolean function that return True if there aren't pink cell attached to blue cell
# each side of a blue cell is checked with index out of bound exception catching
# to prevent from program to crash while checking invalid cells
def pink_constrain():
    flag = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "B":
                try:
                    if board[i - 1][j] == "P":
                        flag = False
                        break
                except IndexError:
                    print()
                try:
                    if board[i][j - 1] == "P":
                        flag = False
                        break
                except IndexError:
                    print()
                try:
                    if board[i][j + 1] == "P":
                        flag = False
                        break
                except IndexError:
                    print()
                try:
                    if board[i + 1][j] == "P":
                        flag = False
                        break
                except IndexError:
                    print()
    return flag


# Boolean function that returns True if there aren't more than 4 yellow cells in a row
def yellow_constrain():
    flag = True
    for i in range(len(board)):
        counter = 0
        for j in range(len(board[i])):
            if board[i][j] == "Y":
                counter += 1
        if counter > 4: flag = False
    return flag


build_gameboard()
printer()
while not still_playing:
    if not blue_constrain():
        (i, j) = [0, 4]
        while i < len(board):
            if board[i][j] == "B":
                board[i][j] = random.choice(colors)
            j -= 1
            i += 1
        (i, j) = [0, 4]
        while i < len(board):
            if board[i][j] == "B":
                board[i][j] = random.choice(colors)
            j += 1
            i += 1
        (i, j) = [4, 0]
        while j < len(board[i]):
            if board[i][j] == "B":
                board[i][j] = random.choice(colors)
            j += 1
    if not pink_constrain():
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "B":
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if board[i][j] == "B":
                                try:
                                    if board[i - 1][j] == "P":
                                        board[i - 1][j] = random.choice(colors)
                                except IndexError:
                                    ()
                                try:
                                    if board[i][j - 1] == "P":
                                        board[i][j - 1] = random.choice(colors)

                                except IndexError:
                                    ()
                                try:
                                    if board[i][j + 1] == "P":
                                        board[i][j + 1] = random.choice(colors)

                                except IndexError:
                                    ()
                                try:
                                    if board[i + 1][j] == "P":
                                        board[i + 1][j] = random.choice(colors)

                                except IndexError:
                                    ()
    if not yellow_constrain():
        for i in range(len(board)):
            counter = 0
            for j in range(len(board[i])):
                if board[i][j] == "Y":
                    counter += 1
            if counter > 4:
                for j in range(len(board[i])):
                    if board[i][j] != 0:
                        board[i][j] = random.choice(colors)
    printer()
    still_playing = blue_constrain() and pink_constrain() and yellow_constrain()
