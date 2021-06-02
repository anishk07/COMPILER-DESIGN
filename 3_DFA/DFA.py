"""@author: ANISHK YADAV"""

n_state = int(input("Enter The Number Of States: "))
state = [input("Enter The States: ") for i in range(0, n_state)]
n_string = int(input("Enter The Number Of Strings: "))
strings = [input("Enter The Strings: ") for i in range(0, n_string)]
f_state = input("Enter The Final State: ")

k = [0 for i in range(len(state))]
for i in range(len(state)):
    k[i] = [0 for j in range(len(strings))]
    for j in range(len(strings)):
        k[i][j] = input('From ' + state[i] + ' If String Is ' +
                        strings[j] + ' Then Go To: ')


def _check(x, y):
    table.append(k[state.index(x)][strings.index(y)])
    return k[state.index(x)][strings.index(y)]


while True:
    table = []
    start = state[0]

    inp_str = input("Enter The String To Check: ")
    for i in inp_str:
        start = _check(start, i)

    if table[-1] == f_state:
        print("Given String Accepted!!")
    else:
        print("Given String Not Accepted!")
