b1 = {'M':3, 'C':3}
b2 = {'M':0, 'C':0}
steps = {(0,2),   (2,0),    (1,1),    (0,1),    (1,0)}

def move(b1, b2, loc, visited):
  global steps
  locs = ['src','des']
  if (b1['C']>b1['M'] and b1['M']!=0) or (b2['C']>b2['M'] and b2['M']!=0):
    return 0
  if (list(b1.values()).copy(), list(b2.values()).copy()) in visited:
    return 0
  if b1['M']==0 and b1['C']==0:
    return 1
  
  visited.append((list(b1.values()).copy(), list(b2.values()).copy()))

  if loc==1:
    for step in steps:
      if step[0]>b1['M'] or step[1]>b1['C']:
        continue
      b1['M'] -= step[0]
      b1['C'] -= step[1]
      b2['M'] += step[0]
      b2['C'] += step[1]
      if move(b1, b2, 2, visited)==1:
        b1['M'] += step[0]
        b1['C'] += step[1]
        b2['M'] -= step[0]
        b2['C'] -= step[1]
        print(step,'from src to des','  ', b2,' ', b1)
        return 1
      if (list(b1.values()).copy(), list(b2.values()).copy()) in visited:
        visited.remove((list(b1.values()).copy(), list(b2.values()).copy()))
      b1['M'] += step[0]
      b1['C'] += step[1]
      b2['M'] -= step[0]
      b2['C'] -= step[1]
  elif loc==2:
    for step in steps:
      if step[0]>b2['M'] or step[1]>b2['C']:
        continue
      b2['M'] -= step[0]
      b2['C'] -= step[1]
      b1['M'] += step[0]
      b1['C'] += step[1]
      if move(b1, b2, 1, visited)==1:
        b2['M'] += step[0]
        b2['C'] += step[1]
        b1['M'] -= step[0]
        b1['C'] -= step[1]
        print(step,'from des to src','  ', b2,' ', b1)
        return 1
      if (list(b1.values()).copy(), list(b2.values()).copy()) in visited:
        visited.remove((list(b1.values()).copy(), list(b2.values()).copy()))
      b2['M'] += step[0]
      b2['C'] += step[1]
      b1['M'] -= step[0]
      b1['C'] -= step[1]

print('Step :                    bank 1             bank 2')
move(b1,b2,1,[])
