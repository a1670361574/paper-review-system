# wht
# 2022/10/10 16:43

class Student:
    firstTutor = ""
    secondTutor = ""

    def __init__(self, num, sId, sName, tutorName, centerName):
        self.num = num
        self.sId = sId
        self.sName = sName
        self.tutorName = tutorName
        self.centerName = centerName

    def print_info(self):
        print(self.num, self.sId, self.sName, self.tutorName, self.centerName)
