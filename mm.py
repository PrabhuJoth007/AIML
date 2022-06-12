def prntbox(s):
    print(s[:3])
    print(s[3:6])
    print(s[6:9])

def cnt(ch, arr):
    c = 0
    for a in arr:
        if a==ch:
            c += 1
    return c

def evalu(s):
    scores = {'X':0, 'O':0}
    rows = [s[:3], s[3:6], s[6:9]]
    cols = [[s[0],s[3],s[6]],
            [s[1],s[4],s[7]],
            [s[2],s[5],s[8]]]
    diags = [[s[6],s[2],s[4]], [s[0],s[4],s[8]]]
    for r in [rows, cols, diags]:
        for now in r:
            if 'O' not in now: scores['X']+=cnt('X', now)
            if 'X' not in now: scores['O']+=cnt('O', now)
    return scores['X']-scores['O']

def checkwin(s):
    rows = [[0,1,2],[3,4,5],[6,7,8]]
    cols = [[0,3,6],[1,4,7],[2,5,8]]
    diag = [[0,4,8],[2,4,6]]
    for now in [rows, cols, diag]:
        for r in now:
            if s[r[0]]==s[r[1]] and s[r[1]]==s[r[2]]:
                if s[r[0]]=='X':
                    print('Max player won')
                    return 1
                elif s[r[0]]=='O':
                    print("Min player won")
                    return 1
    return -1

p = 1
s = ('_','_','_','_','_','_','_','_','_')

print("Initial state :")
prntbox(s)
print()
ply = ['Min', 'Max']
sym = ['O', 'X']

while '_' in s:
    d = {}
    for pl in range(9):
        if s[pl] == '_':
            newb = list(s).copy()
            newb[pl] = sym[p]
            d[tuple(newb)] = evalu(newb)
    nxt = ()
    score = float('inf')
    if p==1: score = -score
    for k in d.keys():
        if (d[k]>score and p==1)   or    (d[k]<score and p==0):
            nxt = k
            score = d[k]
    print(ply[p]+" made move :")
    prntbox(nxt)
    print(d[nxt],'\n\n')
    s = nxt
    if checkwin(s)==1:
        prntbox(s)
        break
    p = -p + 1
