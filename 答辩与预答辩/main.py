import xlrd

from main.pre_reply import pre_reply
from src.student import Student
from src.tutor import Tutor
from src.expert import Expert
from main.pre_reply import*


def read_excel(path):
    workBook = xlrd.open_workbook(path)
    return workBook


# def pre_oral_defence(student_info, tutor_info):


if __name__ == '__main__':
    input1 = read_excel('data/数据-输入1：答辩学生信息表.xlsx')
    student = input1.sheet_by_index(0)

    input2 = read_excel('data/数据-输入2：硕博导师和校外专家池.xlsx')
    tutor = input2.sheet_by_index(0)
    expert = input2.sheet_by_index(1)

    pre_reply(student, tutor)

    # print(sheet1.row_values(1))

    # for i in range(student.nrows - 1):
    #     studentInfo[i].print_info()
    # pre_oral_defence(studentInfo)

    # for i in range(tutor.nrows - 2):
    #     tutorInfo[i].print_info()
