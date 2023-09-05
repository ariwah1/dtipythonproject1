#Function เเบบที่ 2 - Have:parameter/No:return
#parameters: คือ เป็นตัวเเปรประเภทหนึ่ง เอาไว้รับมาใช้เฉพาะในฟังก์ชั้นนั้นๆ เท่านั้น

def funcA(x,y):
    print(f'X is {x}')
    print(f'Y is {y}')
    print(f'Sum {x} + {y} = {x+y}')

    funcA(10,20)#call function ข้อมูลที่ส่งไปให้ parameter เรียกว่า afgiment 
    funcA(1,4)
    print('DTI')
    funcA(5,5)
    