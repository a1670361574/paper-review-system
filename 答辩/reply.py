# wht
# 2022/10/10 20:36


from Group import *
from Experts import *
from Student import *
from Tutor import *
import random

def reply(student_info, tutor_info, expert_info):
    group_number = 5

    studentInfo = []
    for i in range(2, student_info.max_row):
        temp = Student(student_info.cell(i, 1).value, student_info.cell(i, 2).value,
                       student_info.cell(i, 3).value, student_info.cell(i, 4).value,
                       student_info.cell(i, 5).value)
        studentInfo.append(temp)

    tutorInfo = []
    for i in range(3, tutor_info.max_row):
        if tutor_info.cell(i, 6).value != None:
            temp = Tutor(tutor_info.cell(i, 1).value, tutor_info.cell(i, 2).value, tutor_info.cell(i, 6).value,
                         tutor_info.cell(i, 7).value, tutor_info.cell(i, 9).value, tutor_info.cell(i, 10).value,
                         tutor_info.cell(i, 11).value, tutor_info.cell(i, 12).value, tutor_info.cell(i, 13).value)
            tutorInfo.append(temp)

    expertInfo = []
    for i in range(3, expert_info.max_row):
        if expert_info.cell(i, 5).value != None:
            temp = Expert(expert_info.cell(i, 1).value, expert_info.cell(i, 2).value, expert_info.cell(i, 5).value)
            expertInfo.append(temp)

    tutor_day1 = []
    tutor_day2 = []
    expert_pro = []

    for i in tutorInfo:
        if i.firstDay == 1:
            tutor_day1.append(i)
        if i.secondDay == 1:
            tutor_day2.append(i)

    for i in expertInfo:
        if i.title == "教授":
            expert_pro.append(i)

    random.shuffle(tutor_day1)
    random.shuffle(tutor_day2)
    random.shuffle(expert_pro)

    group_day1 = []
    group_day2 = []

    student_num = len(studentInfo) // (2 * group_number)
    student_remainder = len(studentInfo) % (2 * group_number)

    teacher_num = len(tutor_day1) // group_number
    teacher_remainder = len(tutor_day1) % group_number

    for i in range(group_number):
        temp_chairman = []
        temp_teacher = []
        temp_teacher_name = []
        temp_student = []
        flag = 0
        # 主席，委员，学生

        if teacher_remainder != 0:
            temp_teacher.append(tutor_day1[0])
            temp_teacher_name.append(tutor_day1[0].tutorName)
            del tutor_day1[0]
            teacher_remainder -= 1

        for j in range(teacher_num):
            temp_teacher.append(tutor_day1[i * teacher_num + j])
            temp_teacher_name.append(tutor_day1[i * teacher_num + j].tutorName)

        temp_chairman.append(expert_pro[1])
        del expert_pro[1]
        # 主席

        if student_remainder != 0:
            for k in range(len(studentInfo)):
                if studentInfo[k].tutorName in temp_teacher_name:
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    student_remainder -= 1
                    flag = 1
                    break

        for j in range(student_num):
            for k in range(len(studentInfo)):
                if studentInfo[k].tutorName in temp_teacher_name:
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    break

        if flag == 1:
            if (len(temp_student) - 1) < student_num:
                for j in range(student_num + 1 - len(temp_student)):
                    temp_student.append(studentInfo[0])
                    del studentInfo[0]

        else:
            if len(temp_student) < student_num:
                for j in range(student_num - len(temp_student)):
                    temp_student.append(studentInfo[0])
                    del studentInfo[0]

        temp_group = Group(temp_chairman[0], temp_teacher, temp_teacher[-1], temp_student)
        group_day1.append(temp_group)

    teacher_num = len(tutor_day2) // group_number
    teacher_remainder = len(tutor_day2) % group_number
    for i in range(group_number):
        temp_chairman = []
        temp_teacher = []
        temp_teacher_name = []
        temp_student = []
        flag = 0
        # 主席，委员，学生

        if teacher_remainder != 0:
            temp_teacher.append(tutor_day2[0])
            temp_teacher_name.append(tutor_day2[0].tutorName)
            del tutor_day2[0]
            teacher_remainder -= 1

        for j in range(teacher_num):
            temp_teacher.append(tutor_day2[i * teacher_num + j])
            temp_teacher_name.append(tutor_day2[i * teacher_num + j].tutorName)

        temp_chairman.append(expert_pro[1])
        del expert_pro[1]
        # 主席

        if student_remainder != 0:
            for k in range(len(studentInfo)):
                if studentInfo[k].tutorName in temp_teacher_name:
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    student_remainder -= 1
                    flag = 1
                    break

        for j in range(student_num):
            for k in range(len(studentInfo)):
                if studentInfo[k].tutorName in temp_teacher_name:
                    temp_student.append(studentInfo[k])
                    del studentInfo[k]
                    break

        if flag == 1:
            if (len(temp_student) - 1) < student_num:
                for j in range(student_num - 1 - len(temp_student)):
                    temp_student.append(studentInfo[0])
                    del studentInfo[0]

        else:
            if len(temp_student) < student_num:
                for j in range(student_num - len(temp_student)):
                    temp_student.append(studentInfo[0])
                    del studentInfo[0]

        temp_group = Group(temp_chairman[0], temp_teacher, temp_teacher[-1], temp_student)
        group_day2.append(temp_group)

    for i in group_day1:
        i.print_group()
    for i in group_day2:
        i.print_group()

    return group_day1, group_day2