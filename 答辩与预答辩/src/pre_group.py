class PreGroup:

    def __init__(self, group_leader, members, student):
        self.group_leader = group_leader
        self.members = members
        self.student = student

    def print_group(self):
        print("预答辩组组长：", self.group_leader)
        print("预答辩组委员：", self.members)
        print("预答辩学生：", self.student)
