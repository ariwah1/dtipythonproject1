class Test04 : 
    data1 = 10 
    
    # contrustor 
    def __init__(self,data2,data3):
        print('Hi')
        self.data3 = data3
        self.data2 = data2

    # method member 
    def showSumData(self):
        print(self.data1 + self.data2 + self.data3)
        self.showWow()
    
    def showWow(self):
        print('Wow,wow,wpw...')

objA = Test04(20,30)
objB = Test04(10,20)
objC = Test04(20,100)
