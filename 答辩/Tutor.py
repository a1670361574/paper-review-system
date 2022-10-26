# wht
# 2022/10/10 16:43


class Tutor:
    def __init__(self, num, tutorName, title, isPhdTutor, centerName, preDay1, preDay2, firstDay, secondDay):
        self.num = num
        self.tutorName = tutorName
        if title == "教授":
            self.title = "教授"
        else:
            self.title = title
        self.isPhdTutor = isPhdTutor
        self.centerName = centerName
        self.preDay1 = preDay1
        self.preDay2 = preDay2
        self.firstDay = firstDay
        self.secondDay = secondDay

    def print_info(self):
        print(self.num, self.tutorName, self.title, self.isPhdTutor, self.centerName, self.preDay1, self.preDay2, self.firstDay, self.secondDay)

