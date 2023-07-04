def electrons(electron):
    atom = []
    shells = 1
    for el in range(shells, electron):
        current_el = 2 * el ** 2
        if electron - current_el >= 0:
            electron -= current_el
        else:
            current_el = electron
            electron = 0
        atom.append(current_el)
        if electron == 0:
            break
    return atom


numbers_of_electrons = int(input())
print(electrons(numbers_of_electrons))

# --------------------------------- 06. Electron Distribution ---------------------
# You will receive a single integer - the number of electrons.
# Your task is to fill shells until there are no more electrons left. The rules for electron distribution are as follows:
# · The maximum number of electrons in a shell can be 2n2,
# where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
# · You should start filling the shells from the first one at the first position.
# · If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
# In the end, print a list with the filled shells.

# Inputs:
# 10
# 44

# Outputs:
# [2, 8]
# [2, 8, 18, 16]
