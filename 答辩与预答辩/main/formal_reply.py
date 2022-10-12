from src.student import Student
from src.tutor import Tutor
from src.pre_group import PreGroup
from src.expert import Expert
import random


def formal_reply(student_sheet, tutor_sheet, expert_sheet):
    """
    预答辩安排
    :param student_sheet: 包含学生信息的sheet表格
    :param tutor_sheet: 导师信息sheet表格
    :param expert_sheet: 校外专家sheet表格
    :return: 分配好的两天预答辩的各个组
    """
    group_number = 5

    # 从表中读取学生信息
    studentInfo = []
    for i in range(1, student_sheet.nrows):
        temp = Student(student_sheet.cell_value(i, 0), student_sheet.cell_value(i, 1), student_sheet.cell_value(i, 2),
                       student_sheet.cell_value(i, 3), student_sheet.cell_value(i, 4))
        studentInfo.append(temp)

    # 从表中读取导师信息
    tutorInfo = []
    for i in range(2, tutor_sheet.nrows):
        temp = Tutor(tutor_sheet.cell_value(i, 0), tutor_sheet.cell_value(i, 1), tutor_sheet.cell_value(i, 5),
                     tutor_sheet.cell_value(i, 6), tutor_sheet.cell_value(i, 8), tutor_sheet.cell_value(i, 9),
                     tutor_sheet.cell_value(i, 10), tutor_sheet.cell_value(i, 11), tutor_sheet.cell_value(i, 12))
        tutorInfo.append(temp)

    # 读取校外专家信息
    expertInfo = []
    for i in range(2, expert_sheet.nrows):
        temp = Expert(expert_sheet.cell_value(i, 0), expert_sheet.cell_value(i, 1), expert_sheet.cell_value(i, 4))

    # 参加第一天预答辩的教授与其他导师
    prof_day1 = []
    other_day1 = []

    prof_day2 = []
    other_day2 = []

    # 筛选出教授与其他导师
    for i in tutorInfo:
        if i.firstDay == 1:
            if i.title == "教授":
                prof_day1.append(i)
            else:
                other_day1.append(i)
        if i.secondDay == 1:
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

    teacher_num = len(other_day1) // group_number
    student_num = len(studentInfo) // (2 * group_number)
    remainder = len(studentInfo) % (2 * group_number)

    for i in range(group_number):
        temp_member = []
        temp_student = []
        for j in range(teacher_num):
            temp_member.append(other_day1[i * teacher_num + j])
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

        for k in range(len(studentInfo)):
            studentInfo[k].print_info()
        temp = PreGroup(prof_day1[i], temp_member, temp_student)
        group_day1.append(temp)

    for i in range(group_number):
        temp_member = []
        temp_student = []
        for j in range(teacher_num):
            temp_member.append(other_day2[i * teacher_num + j])
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
        for k in range(len(studentInfo)):
            studentInfo[k].print_info()
        temp = PreGroup(prof_day2[group_number + i], temp_member, temp_student)
        group_day2.append(temp)

    for i in group_day1:
        i.print_group()
    for i in group_day2:
        i.print_group()

    return group_day1, group_day2
