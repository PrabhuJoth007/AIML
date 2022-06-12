import numpy 
import math

def derivefunc(x):
    return activation(x)*(1-activation(x))

def activation(x): 
    x=0-x
    return 1/(1+math.exp(x))

inp = []
wgt = [[]]
n = int(input('Enter no. of inputs :'))
for i in range(0,n):
    x=int(input('Enter input value :')) 
    inp.append(x)
hn=int(input('No. of nodes in hidden layer')) 
hw=[0]*hn
hd=[0]*hn
for i in range(0,hn):
    hw.append(int(input('Enter hidden weight : '))) 
hw.pop(0)
for i in range(0,hn): 
    ex=[]
    for j in range(0,n):
        hf=int(input('Enter value of weights :')) 
        ex.append(hf)
    wgt.append(ex)
wgt.pop(0)

def feedf():
    for i in range(0,hn): 
        val=0
        for j in range(0,n):
            val= val+wgt[j][i]*inp[j] 
        b=int(input('Enter bias')) 
        val=val+b 
        hd[i]=activation(val)
    val=0
    for i in range(0,hn): 
        val=val+hd[i]*hw[i]
    b=int(input('Enter bias :')) 
    val=val+b 
    val=activation(val) 
    print(val)
    return val 
    val=feedf()
    for i in range(0,hn): 
        hw[i]=hw[i]+0.1*derivefunc(val)*hd[i] 
        print(hw[i])
    for i in range(0,hn): 
        for j in range(0,n):
            wgt[j][i]=wgt[j][i]+0.1*derivefunc(hd[i])*inp[j] 
            print(wgt[j][i])
    abc=feedf() 
    print(abc)
