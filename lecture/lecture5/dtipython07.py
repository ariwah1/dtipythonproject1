#โปรเเกรมคำนวนหาพื้นที่ทั้งวงกลม เส้นรอบวงกลม เเละปริมาตรทางหน้าจอเเละปริมาตรทรงกลมจากรัศมีที่ป้อนโดยผู้ใช้ทาง
#เเป้นพิมพ์เเละเเสดงผลพื่้นที่ เส้นรอบ เเละปริมาตรทางหน้าจอ

#ขอ 5 ฟังก์ชชัน
import math
#inputRadius
def inputRadius() :
    #r = input('ป้อนรัศมี : ')
    #หรือ r = float(input('ป้อนรัศมี : ') )
    #r = return r
    return input('ป้อนรัศมี : ')   

    # return input('ป้อนรัศมี : ')
    return float(input('ป้อนรัศมี : ')) 

#calAreaCircle
def calAreaCircle(r):
#area = math.pi = *r ** 2
#area = math.pi = *r * r
    return math.pi * math.pow(r,2) 
    
#calRoundCircle 2 * PI = r
def inputRoundCircle() :
    


#calCubeCircle  4/3 * PI * r * r * r
     print()
