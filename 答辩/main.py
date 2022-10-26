# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import openpyxl
from reply import *
from Experts import *
from Student import *
from Tutor import *
from output import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input1 = openpyxl.load_workbook('student.xlsx')
    student = input1.get_sheet_by_name("全日制分配总表（25人外审）")

    input2 = openpyxl.load_workbook('teacher.xlsx')
    tutor = input2.get_sheet_by_name("硕博导师总表")
    expert = input2.get_sheet_by_name("校外专家池")

    group_day1, group_day2 = reply(student, tutor, expert)
    output(group_day1, group_day2)