import test06 # user(Dev)-define module
import math # build in module  

from test08 import calSquaArena,calTriangleArena,calCircleArena
print(f'ผลรวมของ 10 + 20 ={test06.sumNumber(10,20)}')

test06.showHi()

print(f'ราคาสินค้า 20000 ภาษีเป็นเงิน {2000 * test06.vat}')

print(f'7 ยกกำลัง 15 มีค่า{math.pow(7,15)}')

print(f'พื้นที่วงกลม รัศมี 3 มีค่า){math.pi * math.pow(3,2)}')

print(f'พื้นที่วงกลม รัศมี 9 มีค่า {calCircleArena(8)}')

print(f'พื้นที่สี่เหลี่ยม กว้าง 18 ยาว 5ค่า {calSquaArena(10,5)}')
