# list 
my_list = [10,20,10,'Hi',True,[20,'Hello'],(10,20),{10,20}]

# Tuple 
my_tuple = (10,20,10,'Hi',True,(20,'Hello',))

# Set
my_set ={10,20,10,'Hi',True,(10,20)}
            # key คือ index ตัวอ้างอิงไปยัง Value
            # value คือ คำข้อมูลที่สามารถเอาไปใช้งาน
# Dictionary ---- Key : value / Key -> String-Number / Value->Everthing
my_dict = { 'name':' สมชาย ',   'age':20,666:888,  'flag':True}
print(my_dict['name'])
print(my_dict['age'] + my_dict[666])
my_dict['name'] = 'สมหญิง'
my_dict['major'] = 'DTI'
print(my_dict)
my_dict.pop('name')
my_dict.pop(666)
print(my_dict)
my_dict.popitem()
print(my_dict)

for data in my_dict :
    print(data,end = '')

print()

for data in my_dict.keys() :
    print(data,end='')

print()

for data in my_dict.values() : 
    print(data,end='')


my_dict1 = {'a':10,'b':20,'c':30}

my_dict2 = my_dict1

my_dict3 = my_dict1.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict2['a'] = 999
my_dict3['b'] = 888
print('----------------------')
print(my_dict1)
print(my_dict2)
print(my_dict3)

