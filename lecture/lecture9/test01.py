class DtiTest :
    pass
class DtiTest01 :
# data/ attibuilt/ property/ fieald/ คือตัวเเปรประเภทหนึ่ง 
    infoA = ''
    infoB = 20

# method คิอ ฟังชันก์ประเภทหนึ่ง 
    
    def  showHi(self):
        print('Ho')
    def showinfoAandB(self) :
        print(self.infoA)
        print(self.infoB)

# สร้าง object 
ObjA = DtiTest01()
ObjB = DtiTest()
OJ   = DtiTest01()

ObjA.infoA = 50
ObjB.infoB = 160
print(ObjA.infoA+ObjB.infoB)

print(ObjA.infoA + ObjB.infoB)

OJ.showinfoAandB()