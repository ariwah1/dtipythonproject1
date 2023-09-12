#คำสั่ง return ที่ไม่มีอะไรตอท้าย หมายถึง เป็นการบ่งบอกว่าการทำงาน นั้นๆว่าเสร็จเเล่้ว
def example():
    print(111)
    print(222)
    return
    print(333)
    print(444)
    return

#Default Parameter มีการกำหนดเริ่มต้นให้กับพารามิเตอร์
def dtiTest(x,y, z = 20,a = 30 ):
    print(f'{x} + {y} + {z} + {a} = {x+y+z+a} ')

    dtiTest(5, 100) 

    dtiTest(9, 6, 3)