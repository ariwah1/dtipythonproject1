# Constructor
class DtiTest03 :
    # data 
    infoA = 10
 
    
    # constuctor จะเป็นตัวทำให้ object ที่สร้างจาก class เดียวกันไม่จำเป็นต้องเหมือนกัน
    # constuctor จะทำงานทุกครั้งที่มีการสร้าง object 
    def _init_(self,infoB,infoC) :
        self.infoB = infoB
        self.infoC = infoC
        print('Team Spirit')
    # method 
    def showMixandInfo(self,mix):
        print(self.infoA+self.infoB+self.infoC+mix)
    
# สร้าง object 
SAU01  = DtiTest03(10,20)
SAU02  = DtiTest03(10,30)
SAU03  = DtiTest03(10,25)


