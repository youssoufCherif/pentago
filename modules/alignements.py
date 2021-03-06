# Verifie un alignement de p valeurs de j dans le sens horizontal
def alignHoriz(n, list, p, j):
    count = 1
    state = False
    for a in range(0, n):
        for b in range(0, n-1):
            if list[a][b] == j and list[a][b+1] == j:
                count +=1
            else:
                count =1
            if count == p:
                state = True
                break

    return state

# Verifie un alignement de p valeurs de j dans le sens vertical
def alignVert(n, list, p, j):
    count = 1
    state = False
    for a in range(0, n):
        for b in range(0, n-1):
            if list[b][a] == j and list[b+1][a] == j:
                count +=1
            else:
                count =1
            if count == p:
                state = True
                break
    return state

# Verifie un alignement de p valeurs de j en diagonale de bas gauche vers haut droit
def alignLeftDiag(n, list, p, j):
    count = 1
    state = False
    for a in range(1, n):
        if list[n-a][a-1] == j and list[n-a-1][a] == j:
            count +=1
        else:
            count =1
    if count == p:
        state = True
    return state

# Verifie un alignement de p valeurs de j en diagonale de haut gauche vers bas droit
def alignRightDiag(n, list, p, j):
    count = 1
    state = False
    for a in range(1, n):
        if list[a-1][n-a] == j and list[a][n-a-1] == j:
            count +=1
        else:
            count =1
    if count == p:
        state = True
    return state

# Verifie un alignement de p valeurs de j dans au moins une des quatres directions
def align(list, n, p, j):
    states = [alignHoriz(n, list, p, j),
              alignVert(n, list, p, j),
              alignLeftDiag(n, list, p, j),
              alignRightDiag(n, list, p, j)]
    if True in states:
        return True
    return False
