# คุณสมบัตื inheritace สืบทอด คือ การที่คลาสหนึ่ง สืบทอดอีกคลาสหนึ่ง (reuse)
# สืบทอด มีเเม่ (super class) มีลุูก (sub class)

# คุณสมบัติเด่น Polymorphism (พ้องรูป:พฤตืกรรมเดียวกันวิืธีการต่างกัน) คือ การที่คลาสลูกเอาเมธอตของเเม่มาเขียนใหม่

class Sau01 :
    infoA = 10 

    def showHi():
        print('Hi')

class Sau02(Sau01):   #inheritance
    infoB = 20

    def showhey():
        print('hey')
    
    # overiding method : Polymorphim
    
    def showHi():
        print('Hi Hi Hi')

ob1 = Sau01()
ob2 = Sau02()
ob2.showHi()


