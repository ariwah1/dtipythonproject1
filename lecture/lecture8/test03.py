# oop
class DtiSau : 
    #data property member คำข้อมูล
    stu_name = ''
    score = 0
    gpa = 0

    # method member คือการทำงาน
    def hiStudent(self):
       print(f'สวัสดี' (self.stu_name))

    def showScoreAndGrade(self):
        print(f"คะเเนน" (self.score) "ได้เกรด" (self.gpa))

# สร้าง object 
obj01 = DtiSau() # ช็อตคลาส () เราเรียกว่าเป็นการสั่งให้ contructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stu_name = 'สมชาย'
obj01.hiStudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 90
obj02.gpa = 3.99
