# wht
# 2022/10/10 19:54

from Student import *
from Tutor import *

# class Group:
#
#     def __init__(self, group_leader, members, secretary, student):
#         self.group_leader = group_leader
#         self.members = members
#         self.secretary = secretary
#         self.student = student
#
#
#     def print_group(self):
#         print("答辩组组长：", self.group_leader, "\n")
#         print("答辩组委员：", self.members, "\n")
#         print("答辩组秘书：", self.secretary, "\n")
#         print("答辩学生：", self.student, "\n")

class Group:
    group_leader = None
    members = None
    secretary = None
    students = None

    def __init__(self, group_leader, members, secretary, student):
        self.group_leader = group_leader
        self.members = members
        self.secretary = secretary
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
        print("正式答辩组组长：", self.group_leader.name)
        print("正式答辩组委员：", self.get_members_list())
        print("正式答辩组秘书：", self.secretary.tutorName)
        print("预答辩学生：", self.get_students_list())