class Tutor:
    def __init__(self, num, tutorName, title, isPhdTutor, centerName, preDay1, preDay2, firstDay, secondDay):
        self.num = num
        self.tutorName = tutorName
        if ("教授" in title) & ("副" not in title) \
                & ("助理" not in title):
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
        print('{:>5} {:<20} {:<15} {:<10} {:<20} {:<3} {:<3} {:<3} {:<3}'.format(
            self.num, self.tutorName, self.title, self.isPhdTutor, self.centerName, self.preDay1,
            self.preDay2, self.firstDay, self.secondDay))
