# คุณสมบัติเด่น Encapsulation (ห่อหุ้ม data)
class DtiTest05 : 
    # data 
     infoA = 10 #ไม่ได้ห่อหุ่ม
     _infoB = 20 # ห่อหุ่ม

     def _init_(self,infoC,infoD): 
          self._infoC = infoC #ไม่ได้ห่อหุ่ม
          self._infoD = infoD # Encap ดูจาก _>>>>>>เป็น

#เมื่อใดก็ตาม Encap จะต้องมี method 2 ตัวนัี้เสมอ คึือ get,set ของ data ตัวนั้น
     def setInfoB(self,infoB):
          self._infoB = infoB
     
     def getinfoB(self,infoB):
         return self._infoB
     
     def getinfoD(self,infoD):
          self._infoD = infoD

     def getinfoB(self,infoD):
          return self._infoD 
     
     def showInfo(self):
          print(self.infoA)
          print(self._infoB)
          print(self.infoC)
          print(self._infoD)
          print("--------------")
          

ob1 = DtiTest05(30,40)
ob2 = DtiTest05(30,100)
ob1.showInfo()
ob1.infoA = 555  
ob1._setinfoB(999)  
ob1.showInfo()
print(ob1.getinfoB+ob1.getinfoD)
