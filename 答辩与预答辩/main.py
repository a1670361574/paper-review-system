
import xlrd

from main.pre_reply import pre_reply
from main.formal_reply import formal_reply
from src.student import Student
from src.tutor import Tutor
from src.expert import Expert
from main.output import output


def read_excel(path):
    workBook = xlrd.open_workbook(path)
    return workBook


if __name__ == '__main__':
    input1 = read_excel('file/数据-输入1：答辩学生信息表.xlsx')
    student_sheet = input1.sheet_by_index(0)

    input2 = read_excel('file/数据-输入2：硕博导师和校外专家池.xlsx')
    tutor_sheet = input2.sheet_by_index(0)
    expert_sheet = input2.sheet_by_index(1)

    group_day1, group_day2 = pre_reply(student_sheet, tutor_sheet)
    # formal_group_day1, formal_group_day2 = formal_reply(student_sheet, tutor_sheet, expert_sheet)
    output(group_day1, group_day2)
    # output(formal_group_day1, formal_group_day2)

    # print(sheet1.row_values(1))

    # for i in range(student.nrows - 1):
    #     studentInfo[i].print_info()
    # pre_oral_defence(studentInfo)

    # for i in range(tutor.nrows - 2):
    #     tutorInfo[i].print_info()
