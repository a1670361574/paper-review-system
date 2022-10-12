from src.student import Student
from src.tutor import Tutor


class PreGroup:
    group_leader = None
    members = None
    students = None

    def __init__(self, group_leader, members, student):
        self.group_leader = group_leader
        self.members = members
        self.students = student

    def get_members_list(self):
        temp = []
        for i in self.members:
            temp.append(i.tutorName)
        return temp

    def get_students_list(self):
        temp = []
        for i in self.students:
            temp.append(i.sName)
        return temp

    def get_members_str(self):
        temp = ""
        for i in self.members:
            temp += f' {i.tutorName}'
        return temp

    def print_group(self):
        print("预答辩组组长：", self.group_leader.tutorName)
        print("预答辩组委员：", self.get_members_list())
        print("预答辩学生：", self.get_students_list())
