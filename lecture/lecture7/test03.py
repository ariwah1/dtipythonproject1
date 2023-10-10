# List Method
var1 = [10,20,'Hello',True,[111,'WOW'], 'มานะ']
# append
var1.append(555)
var1.append(['Hi','Hey',888])
print(var1)
# extend เพิ่มเเต่ละข้อมูล
var1.extend([10,20,30])
print(var1)
# remove
var1.remove('Hello')
var1.remove(10)
print(var1)
# ----------------------
var2 = [10,20,'Hi','Hello']
# pop
var2.pop()
print(var2)
var2.pop(1)
print(var2)
# index
print(var2.index('Hi'))
# count นับจำนวนข้อมูลนั้นๆที่ซ้ำที่อยู่ใน List
# มีกี่ตัว
print(var1.count(10))
var3 =[10,10,20,'Hi',10,'Hi']
print(f'ใน var3 มี 10 ทั้งหมด {var3.count(10)} ตัว')
print(f'ใน var3 มี Hi ทั้งหมด {var3.count("Hi")} ตัว')
print('Hi \'SAU\'')
print("Hi 'SAU'")     
print("Hi \'DTI\'")     
print('Hi "DTI"')     
# เมธอทต่อไปนี้ใช้ได้เฉพาะข้อมูลที่เป็นประเภทเดียวกันเท่านั้น
# sort
var4= [10,10,20,'Hi',10,'Hi']
# var4.sort()error
var5= [99,34,]