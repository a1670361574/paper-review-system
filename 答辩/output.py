# wht
# 2022/10/16 19:03

import xlwt


# VERT_TOP    = 0x00    上端对齐
# VERT_CENTER = 0x01    居中对齐（垂直方向上）
# VERT_BOTTOM = 0x02    低端对齐
# HORZ_LEFT   = 0x01    左端对齐
# HORZ_CENTER = 0x02    居中对齐（水平方向上）
# HORZ_RIGHT  = 0x03    右端对齐

def style_head():
    style = xlwt.XFStyle()

    # 单元格格式
    al = xlwt.Alignment()
    al.vert = 0x01  # 设置垂直居中
    al.horz = 0x02  # 设置水平居中
    al.wrap = 0x01
    style.alignment = al

    # 字体
    font = xlwt.Font()
    font.name = 'Microsoft YaHei'
    font.bold = True
    font.height = 20 * 11
    style.font = font

    return style


def style_content():
    style = xlwt.XFStyle()

    # 单元格格式
    al = xlwt.Alignment()
    al.vert = 0x01  # 设置垂直居中
    al.horz = 0x02  # 设置水平居中
    style.alignment = al

    # 字体
    font = xlwt.Font()
    font.name = 'Microsoft YaHei'
    font.height = 20 * 11
    style.font = font

    return style


def output(group_day1, group_day2):
    workBook = xlwt.Workbook(encoding='ascii')

    temp = ['排序', '学生姓名', '导师姓名', '时间', '备注']

    worksheet = workBook.add_sheet("正式答辩")

    style_title = style_head()
    style_cont = style_content()

    for j in range(5):
        for i in range(5):
            worksheet.col(j * 5 + 3).width = 5000
            worksheet.col(j * 5 + 4).width = 12000
        worksheet.write_merge(0, 0, j * 5, j * 5 + 4, '计算机学院硕士生正式答辩', style_title)
        worksheet.write_merge(1, 1, j * 5, j * 5 + 4, f'第1日 第{j + 1}组', style_title)
        worksheet.write_merge(2, 2, j * 5, j * 5 + 4, f'正式答辩委员：{group_day1[j].group_leader.name}（主席）'
                                                      f'{group_day1[j].get_members_str()}（秘书）', style_title)
        worksheet.write_merge(3, 3, j * 5, j * 5 + 4, f'正式答辩地点：', style_title)
        worksheet.write_merge(18, 18, j * 5, j * 5 + 4, '关于答辩的说明', style_title)
        worksheet.row(19).set_style(xlwt.easyxf('font:height 720'))
        worksheet.write_merge(19, 19, j * 5, j * 5 + 4, '（1）PPT陈述时间：20分钟\n（2）回答问题：10分钟', style_title)
        for k in range(5):
            worksheet.write(4, j * 5 + k, temp[k], style_content())
        for k in range(len(group_day1[j].students)):
            worksheet.write(5 + k, j * 5, k + 1, style_content())
            worksheet.write(5 + k, j * 5 + 1, group_day1[j].students[k].sName, style_content())
            worksheet.write(5 + k, j * 5 + 2, group_day1[j].students[k].tutorName, style_content())

    for j in range(5):
        for i in range(5):
            worksheet.col(j * 5 + 3).width = 5000
            worksheet.col(j * 5 + 4).width = 12000
        worksheet.write_merge(20, 20, j * 5, j * 5 + 4, '计算机学院硕士生正式答辩', style_title)
        worksheet.write_merge(21, 21, j * 5, j * 5 + 4, f'第2日 第{j + 1}组', style_title)
        worksheet.write_merge(22, 22, j * 5, j * 5 + 4, f'正式答辩委员：{group_day2[j].group_leader.name}（主席）'
                                                        f'{group_day2[j].get_members_str()}（秘书）', style_title)
        worksheet.write_merge(23, 23, j * 5, j * 5 + 4, f'正式答辩地点：', style_title)
        worksheet.write_merge(38, 38, j * 5, j * 5 + 4, '关于答辩的说明', style_title)
        worksheet.row(39).set_style(xlwt.easyxf('font:height 720'))
        worksheet.write_merge(39, 39, j * 5, j * 5 + 4, '（1）PPT陈述时间：20分钟\n（2）回答问题：10分钟', style_title)
        for k in range(5):
            worksheet.write(24, j * 5 + k, temp[k], style_content())
        for k in range(len(group_day2[j].students)):
            worksheet.write(25 + k, j * 5, k + 1, style_content())
            worksheet.write(25 + k, j * 5 + 1, group_day2[j].students[k].sName, style_content())
            worksheet.write(25 + k, j * 5 + 2, group_day2[j].students[k].tutorName, style_content())

    workBook.save("答辩.xls")
