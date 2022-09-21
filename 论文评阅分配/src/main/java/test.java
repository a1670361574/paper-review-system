import pojo.Student;
import pojo.Tutor;
import service.access;
import service.input;
import service.output;

import java.util.List;

public class test {
    public static void main(String[] args) throws Exception{
        List<Student> sl = input.ReadStudent("D:\\file\\输入1：答辩学生信息表.xls");
        List<Tutor> tl = input.ReadTutor("D:\\file\\输入2：硕博导师和校外专家池.xls");
        input.init(sl,tl);  //处理输入
        for (int i = 0; i < tl.size(); i++) {
            System.out.println(tl.get(i));  //每个导师分配的任务数量
        }
        access.start(sl,tl); // 进行分配
        for (int i = 0; i < sl.size(); i++) {
            System.out.println(sl.get(i));  //每个学生被分配后的状态
        }
        for (int i = 0; i < tl.size(); i++) {
            System.out.println(tl.get(i));  //每个导师分配后的状态
        }
        output.createExcel("D:\\file\\输出.xls",sl);  //输出结果为excel文件
    }
}
