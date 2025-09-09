def add(*args):
    sum = 0
    for i in args :
        sum += i
    print(sum)
        
add(0,1,2,3,4,5)

def calc(**kwargs):
    i+=kwargs['add']
    i*=kwargs['mult']
        
calc(2,add='3',mult='5')