# index of game
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)


# functions

# printing frame


def print_frame():
    print('---------')
    for i in range(3):
        print('|', end=' ')
        for j in range(3):
            print(str(inpfields[i][j]), end=" ")
        print('|')
    print('---------')

# evaluating conditions


def check(arr, val):
    if(arr[0] == val and arr[0] == arr[1] and arr[1] == arr[2]):
        return True
    else:
        return False

# loop for input


def ask_input(str1):
    y = 0
    while(True):
        try:
            coord = [int(x)
                     for x in input('Enter the coordinates:') if x != ' ']

            if coord[0] > 0 and coord[0] < 4 and coord[1] > 0 and coord[1] < 4:
                if inpfields[abs(coord[1]-3)][coord[0]-1] == 'X' or inpfields[abs(coord[1]-3)][coord[0]-1] == 'O':
                    print('This cell is occupied! Choose another one!')
                else:
                    inpfields[abs(coord[1]-3)][abs(coord[0]-1)] = str1
                    print_frame()
                    break

            else:
                print('Coordinates should be from 1 to 3!')
        except:
            print('You should enter numbers!')

# checking conditions


def check_conditions(str2):
    hor_1 = inpfields[0]
    hor_2 = inpfields[1]
    hor_3 = inpfields[2]
    ver_1, ver_2, ver_3, diag_1, diag_2 = [], [], [], [], []
    i = 0
    j = 2
    for row in inpfields:
        ver_1.append(row[0])
        ver_2.append(row[1])
        ver_3.append(row[2])
        diag_1.append(row[i])
        diag_2.append(row[j])
        i += 1
        j -= 1
    cond = [hor_1, hor_2, hor_3, ver_1, ver_2, ver_3, diag_1, diag_2]
    cond_x = []
    cond_o = []

    # function call for evaluating conditions
    for i in range(len(cond)):
        cond_x.append(check(cond[i], str2))

    # checking if impossible
    # freq = {'X': 0, 'O': 0, '-': 0}
    # for val in inp:
    #     if val == 'X':
    #         freq['X'] += 1
    #     elif val == 'O':
    #         freq['O'] += 1
    #     else:
    #         freq['-'] += 1

    # final printing
    # if abs(freq['X']-freq['O']) >= 2 or (sum(cond_x) >= 1 and sum(cond_o) >= 1):
    #     print('Impossible')
    if sum(cond_x) >= 1:
        print(str2+' wins')
        return 1
    elif sum(cond_o) >= 1:
        print(str2+' wins')
        return 1
    elif ' ' not in inpfields[0] and ' ' not in inpfields[1] and ' ' not in inpfields[2]:
        print("Draw")
        return 1


# inputs
inpfields = [[' ' for _ in range(3)] for _ in range(3)]
inp = []
for x in inpfields:
    for y in x:
        inp.append(y)
flag = 0
print_frame()
# x = 0

# for i in range(3):
#     for j in range(3):
#         inpfields[i][j] = inp[x]
#         x += 1

# conditions
while(not flag):
    ask_input('X')
    flag = check_conditions('X')
    if flag == 1:
        break
    ask_input('O')
    flag = check_conditions('O')
