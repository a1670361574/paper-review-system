from src.student import Student
from src.tutor import Tutor
from src.pre_group import PreGroup
import random


def pre_reply(student_info, tutor_info):
    group_number = 5

    studentInfo = []
    for i in range(1, student_info.nrows):
        temp = Student(student_info.cell_value(i, 0), student_info.cell_value(i, 1), student_info.cell_value(i, 2),
                       student_info.cell_value(i, 3), student_info.cell_value(i, 4))
        studentInfo.append(temp)

    tutorInfo = []
    for i in range(2, tutor_info.nrows):
        temp = Tutor(tutor_info.cell_value(i, 0), tutor_info.cell_value(i, 1), tutor_info.cell_value(i, 5),
                     tutor_info.cell_value(i, 6), tutor_info.cell_value(i, 8), tutor_info.cell_value(i, 9),
                     tutor_info.cell_value(i, 10), tutor_info.cell_value(i, 11), tutor_info.cell_value(i, 12))
        tutorInfo.append(temp)
    pre1 = []
    pre2 = []
    prof_day1 = []
    other_day1 = []

    prof_day2 = []
    other_day2 = []

    for i in tutorInfo:
        # if i.title == "教授":
        #     i.print_info()
        if i.preDay1 == 1:
            if i.title == "教授":
                prof_day1.append(i.tutorName)
            else:
                other_day1.append(i.tutorName)
        if i.preDay2 == 1:
            if i.title == "教授":
                prof_day2.append(i.tutorName)
            else:
                other_day2.append(i.tutorName)
    random.shuffle(prof_day1)
    random.shuffle(other_day1)

    random.shuffle(prof_day2)
    random.shuffle(other_day2)

    # print(prof_day1, other_day1)
    # for i in tutorInfo:
    #     if (i.title == "教授") & (i.preDay1 == 1):
    #         i.print_info()
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
                    temp_student.append(studentInfo[k].sName)
                    del studentInfo[k]
                    remainder -= 1
                    break

        for j in range(student_num):
            # if (studentInfo[i * student_num + j].tutorName != prof_day1[i]) | (
            #         studentInfo[i * student_num + j].tutorName not in other_day1):
            #     temp_student.append(studentInfo[i * student_num + j].sName)
            for k in range(len(studentInfo)):
                if (studentInfo[k].tutorName != prof_day1[i]) & (studentInfo[k].tutorName not in temp_member):
                    temp_student.append(studentInfo[k].sName)
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
                    temp_student.append(studentInfo[k].sName)
                    del studentInfo[k]
                    remainder -= 1
                    break

        for j in range(student_num):
            for k in range(len(studentInfo)):
                if (studentInfo[k].tutorName != prof_day2[i]) & (studentInfo[k].tutorName not in temp_member):
                    temp_student.append(studentInfo[k].sName)
                    del studentInfo[k]
                    break
        for k in range(len(studentInfo)):
            studentInfo[k].print_info()
        temp = PreGroup(prof_day2[group_number+i], temp_member, temp_student)
        group_day2.append(temp)

    for i in group_day1:
        i.print_group()
    for i in group_day2:
        i.print_group()

    return group_day1, group_day2
