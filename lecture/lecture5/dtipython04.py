#Function 4 : have parameter/have return
def dti1(a,b) :
    print(f'{a} ยกกำลัง {b} = {a ** b}')
    return a ** b

def dti2(a,  b,  c, y) :
    return a + b + c + y + dti1(2,3),"Wow"


c, y = dti2(2, 7, 8, 6)

#Function 4 : have parameter/have return
def dti1(a,b) :
    print(f'{a} ยกกำลัง {b} = {a ** b}')
    return a ** b

def dti2(a,  b,  c, y) :
    return a + b + c + y + dti1(2,3),"Wow"


c, y = dti2(2, 7, 8, 6)

print(f'{c} t_t {y}')