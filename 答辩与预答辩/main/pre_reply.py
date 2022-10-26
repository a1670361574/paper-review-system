from src.student import Student
from src.tutor import Tutor
from src.pre_group import PreGroup
import random


def pre_reply(student_sheet, tutor_sheet, group_number=5):
    """
    预答辩安排
    :param group_number: 每天进行答辩的组数
    :param student_sheet: 包含学生信息的sheet表格
    :param tutor_sheet: 导师信息sheet表格
    :return: 分配好的两天预答辩的各个组
    """

    # 从表中读取学生信息，每个学生是一个Student对象，所有对象保存在studentInfo列表里
    studentInfo = []
    for i in range(1, student_sheet.nrows):
        temp = Student(student_sheet.cell_value(i, 0), student_sheet.cell_value(i, 1), student_sheet.cell_value(i, 2),
                       student_sheet.cell_value(i, 3), student_sheet.cell_value(i, 4))
        studentInfo.append(temp)

    # 从表中读取导师信息，每个老师是一个Tutor对象，所有对象保存在tutorInfo列表里
    tutorInfo = []
    for i in range(2, tutor_sheet.nrows):
        temp = Tutor(tutor_sheet.cell_value(i, 0), tutor_sheet.cell_value(i, 1), tutor_sheet.cell_value(i, 5),
                     tutor_sheet.cell_value(i, 6), tutor_sheet.cell_value(i, 8), tutor_sheet.cell_value(i, 13),
                     tutor_sheet.cell_value(i, 14), tutor_sheet.cell_value(i, 15), tutor_sheet.cell_value(i, 16))
        tutorInfo.append(temp)

    # 可参加第一天预答辩的教授与其他导师
    prof_day1 = []
    other_day1 = []

    # 可参加第二天预答辩的教授与其他导师
    prof_day2 = []
    other_day2 = []

    # 筛选出教授与其他导师
    for i in tutorInfo:
        if i.preDay1 == 1:
            if i.title == "教授":
                prof_day1.append(i)
            else:
                other_day1.append(i)
        if i.preDay2 == 1:
            if i.title == "教授":
                prof_day2.append(i)
            else:
                other_day2.append(i)

    # 打乱排序用于随机分配
    random.shuffle(prof_day1)
    random.shuffle(other_day1)

    random.shuffle(prof_day2)
    random.shuffle(other_day2)

    group_day1 = []
    group_day2 = []

    # group_number = 6  # 每天进行答辩的组数
    teacher_num_day1 = len(other_day1) // group_number
    teacher_num_day2 = len(other_day2) // group_number
    # teacher_num_day1 = 3  # 每个组的非正教授老师数量
    student_num = len(studentInfo) // (2 * group_number)  # 每组学生数量
    remainder = len(studentInfo) % (2 * group_number)  # 无法平均分配的多余学生数量，需要在某些组多安排1个学生

    print(len(prof_day1), len(prof_day2), len(other_day1), len(other_day2), teacher_num_day1, teacher_num_day2,
          student_num, remainder)

    # 分配第一天预答辩各组
    for i in range(group_number):
        temp_member = []
        temp_student = []
        for j in range(teacher_num_day1):
            temp_member.append(other_day1[i * teacher_num_day1 + j])
        if remainder != 0:
            for k in range(len(studentInfo)):
                if (studentInfo[k].tutorName != prof_day1[i]) & (studentInfo[k].tutorName not in temp_member):
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    remainder -= 1
                    break

        for j in range(student_num):
            for k in range(len(studentInfo)):
                if (studentInfo[k].tutorName != prof_day1[i]) & (studentInfo[k].tutorName not in temp_member):
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    break

        # for k in range(len(studentInfo)):
        #     studentInfo[k].print_info()
        temp = PreGroup(prof_day1[i], temp_member, temp_student)
        group_day1.append(temp)

    for i in range(group_number):
        temp_member = []
        temp_student = []
        for j in range(teacher_num_day2):
            temp_member.append(other_day2[i * teacher_num_day2 + j])
        if remainder != 0:
            for k in range(len(studentInfo)):
                if (studentInfo[k].tutorName != prof_day2[i]) & (studentInfo[k].tutorName not in temp_member):
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    remainder -= 1
                    break

        for j in range(student_num):
            for k in range(len(studentInfo)):
                if (studentInfo[k].tutorName != prof_day2[i]) & (studentInfo[k].tutorName not in temp_member):
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    break
        # for k in range(len(studentInfo)):
        #     studentInfo[k].print_info()
        temp = PreGroup(prof_day2[i], temp_member, temp_student)
        group_day2.append(temp)

    for i in group_day1:
        print(i.group_leader.tutorName)

    for i in group_day1:
        i.print_group()
    for i in group_day2:
        i.print_group()

    return group_day1, group_day2
