# list
#                              #0   1
  #       0  1    2       3    4            5
vars1 = [10,20,'Hellow',True,[111,'WOW'], 'มานะ']
  #      -6 -5   -4      -3    -2           -1       
                              #-2  -1

print(vars1[0]+ vars1[1])
print(vars1[-5]+ vars1[-6])
print(vars1[0]+ vars1[4][0])
print(vars1[-6]+ vars1[-2][-2])

# Tuple
#
vars2 = (10,20,'Hellow',True,(111,'WOW'), 'มานะ')
#
print(vars2[0]+vars2[1])
print(vars2[-6]+vars2[-5])
print(vars2[-6]+vars2[-2][-2])
print(f'{vars2[2]}.....{vars2[5]} {vars2[4][1]}........')