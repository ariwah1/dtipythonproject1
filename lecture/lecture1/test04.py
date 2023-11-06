#รับค่า คือหยุดให้ user ป้อนทางเเป้นพิมพ์
#variable (ตัวเเปร)

#การเเปลง (casting/tybe)
stu_id = input('ป้อน student id ') 
stuName = input('ป้อน student Name  ') 
stu_birth_year =  input('ป้อน student birth year ') 
print("--------------------------------------------")

print(f"ยินดีต้อนรับ {stu_id} {stuName} สู่ SAU")  
print(f"คุณเกิดปี {stu_birth_year} เเปลว่าคุณอายุ {2023-int(stu_birth_year)} ปี" )


print("ใช้เมธอท format------------------------------------")
print("ยินดีต้อนรับ {} {} สู่ SAU".format(stu_id,stuName) )
print("คุณเกิดปี {} เเปลว่าคุณอายุ {} ปี".format(stu_birth_year,2023-int(stu_birth_year)))  

print("ใฃ้ ,------------------------------------")
print("ยินดีต้อนรับ",stu_id,stuName"สู่ SAU")
print("คุณเกิดปี",stu_birth_year, "เเปลว่าคุณอายุ" ,2023-int(stu_birth_year), "ปี")

print("ใฃ้ +------------------------------------")
print("ยินดีต้อนรับ "+stu_id+" "+stuName" สู่ SAU")
print("คุณเกิดปี"  +stu_birth_year+ "เเปลว่าคุณอายุ" +2023-int+stu_birth_year "ปี"  )
