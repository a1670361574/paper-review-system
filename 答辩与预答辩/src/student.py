class Student:
    firstTutor = ""
    secondTutor = ""

    def __init__(self, num, sId, sName, tutorName, centerName):
        """

        :param num: 学生在excel中序号
        :param sId: 学号
        :param sName: 姓名
        :param tutorName: 导师姓名
        :param centerName: 所属中心
        """
        self.num = num
        self.sId = sId
        self.sName = sName
        self.tutorName = tutorName
        self.centerName = centerName

    def print_info(self):
        print(self.num, self.sId, self.sName, self.tutorName, self.centerName)
