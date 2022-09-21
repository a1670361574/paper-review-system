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
        input.init(sl,tl);
        for (int i = 0; i < tl.size(); i++) {
            System.out.println(tl.get(i));
        }
        access.start(sl,tl);
        for (int i = 0; i < sl.size(); i++) {
            System.out.println(sl.get(i));
        }
        for (int i = 0; i < tl.size(); i++) {
            System.out.println(tl.get(i));
        }
        output.createExcel("D:\\file\\输出.xls",sl);
    }
}
