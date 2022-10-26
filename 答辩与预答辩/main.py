
import xlrd

from main.pre_reply import pre_reply
# from main.formal_reply import formal_reply
from src.student import Student
from src.tutor import Tutor
from src.expert import Expert
from main.output import output


def read_excel(path):
    workBook = xlrd.open_workbook(path)
    return workBook


if __name__ == '__main__':

    # 读取xls文件
    input1 = xlrd.open_workbook('file/数据-输入1：答辩学生信息表.xls')
    # input1 = xlrd.open_workbook('file/数据-输入1：答辩学生信息表.xlsx')

    # 读取文件中的sheet，向分配函数传入的是sheet，而非xls文件
    student_sheet = input1.sheet_by_index(0)

    # 读取xls文件
    input2 = read_excel('file/数据-输入2：硕博导师和校外专家池.xls')

    # 读取两个sheet，分别为校内导师信息与校外专家信息
    tutor_sheet = input2.sheet_by_index(0)
    expert_sheet = input2.sheet_by_index(1)

    # 将读取的表格与分配的组数传入分配函数
    group_day1, group_day2 = pre_reply(student_sheet, tutor_sheet, 4)

    # formal_group_day1, formal_group_day2 = formal_reply(student_sheet, tutor_sheet, expert_sheet)

    # 输出分配好的表格
    # output(group_day1, group_day2)
    # output(formal_group_day1, formal_group_day2)

    # print(sheet1.row_values(1))

    # for i in range(student.nrows - 1):
    #     studentInfo[i].print_info()
    # pre_oral_defence(studentInfo)

    # for i in range(tutor.nrows - 2):
    #     tutorInfo[i].print_info()
