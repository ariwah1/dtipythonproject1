# slicing data in list and tuple

var1 = [10,20,'Hello',True,[111,'WOW'], 'มานะ']

var2 = (10,20,'Hello',True,(111,'WOW'), 'มานะ')

# 20,'Hello',True
print(var1[1:4])
# True , (111,"Wow")
print(var2[3:5])
#10,20,"Hello"
print(var1p[:3])
# 'Hello',True, [111,'Wow'],"มานะ"
print(var1[2:])
