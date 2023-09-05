#ใช้ modular opertor % 2313git 
print ('hello.....%d %f %sHi....'%(20, 17,18))
emp_name=input("ป้อนชื่อพนักงาน")
sale_price=input ("ยอดขาย") 
print("----------------------")
#int(),float()
#ฟังก์ชันเเแปลง string เป็น Number -> int(),float()
commision = float( sale_price )* 10/100

print(f"คุณ{emp_name} ยอดขาย {float(sale_price)} บาท ได้คำตอบ{commision:.2f}บาท")
print("คุณ",(emp_name),"ยอดขาย",float(sale_price),"บาท ได้คำตอบ",(commision),"บาท")#ใช้ ,
print(คุณ)
