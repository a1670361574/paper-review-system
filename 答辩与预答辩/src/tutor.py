class Tutor:
    def __init__(self, num, tutorName, title, isPhdTutor, centerName, preDay1, preDay2, firstDay, secondDay):
        """

        :param num: 导师在excel中序号
        :param tutorName: 姓名
        :param title: 职称
        :param isPhdTutor: 是否为博导
        :param centerName: 所属中心
        :param preDay1: 是否参加第一天预答辩
        :param preDay2: 是否参加第二天预答辩
        :param firstDay: 是否参加第一天正式答辩
        :param secondDay: 是否参加第二天正式答辩
        """
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
