
#คำนวณงินที่จะเเชร์กัน ป้อนเงิน ป้อนคน เเล้วคำนวณเเละเเสดงเงินที่จะเเชร์กัน
#โดยให้เขียนเป็นฟังชันก์ ขอ 2 ฟังชันก์
def inputpersonmoney() :
    Money = float( input('Money:'))
    Person = int( input('Person:'))
    return Money, Person 
    
def calinputSharemoney(money, person) :
    M = format(money,".2f")
    print(f'จำนวนเงิน {money:.2f} บาท  {person} คน เเชร์กันคนละ {round(money/person)} บาท')
    print("จำนวนเงิน",("%.2f"%money),"บาท",(person),"คน เเชร์คนละ",round(money/person),"บาท")
    print("จำนวนเงิน"+str("%.2f"%money)+'บาท '+str(person)+'คน เเชร์คนละ '+str(round(money/person)))
    print('จำนวนเงิน {:.2f} บาท  {} คน เเชร์กันคนละ {} บาท'.format(money,person, round(money/person)))
    print('จำนวนเงิน %s บาท %d คน เเชร์กันคนละ %d บาท'.format(M,person, round(money/person)))    
Money,Person = inputpersonmoney()
calinputSharemoney(Money,Person)