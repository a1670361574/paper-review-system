package service;

import jxl.Workbook;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import pojo.Student;

import java.io.FileOutputStream;
import java.io.Writer;
import java.util.List;

public class output {
    public static void createExcel(String url, List<Student> list) throws Exception{
        FileOutputStream os = new FileOutputStream(url);
        WritableWorkbook wb = Workbook.createWorkbook(os);
        WritableSheet sheet = wb.createSheet("全日制分配总表",0);
        String[] head = {"序号","学号" ,"研究生姓名" ,"导师姓名", "研究中心名称", "评审人1", "评审人2", "系统检查人"};
        for(int i = 0; i < 8; i++) {
            jxl.write.Label l1 = new jxl.write.Label(i,0,head[i]);
            sheet.addCell(l1);
        }
        for(int i = 0; i < list.size(); i++) {
            for(int j = 0; j < 8; j++) {
                jxl.write.Label l1 = new jxl.write.Label(j,i+1,list.get(i).toArray()[j]);
                sheet.addCell(l1);
            }
        }
        wb.write();
        wb.close();
        os.close();
    }
}
