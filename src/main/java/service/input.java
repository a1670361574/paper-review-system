package service;

import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;
import pojo.Student;
import pojo.Tutor;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class input {
    public static List<Student> ReadStudent(String url) throws Exception {
        Workbook workbook = Workbook.getWorkbook(new File(url));
        Sheet sheet = workbook.getSheet(0);
        List<Student> list = new ArrayList<>();
        int i = 1;
        while(i < sheet.getRows() && !sheet.getCell(0,i).getContents().equals("")) {
            Student s = new Student();
            for (int j = 0; j < sheet.getColumns(); j++) {
                String content = sheet.getCell(j,i).getContents();
                if(j == 0) s.setNum(Integer.valueOf(content));
                if(j == 1) s.setsId(content);
                if(j == 2) s.setsName(content);
                if(j == 3) s.setTutorName(content);
                if(j == 4) s.setCenterName(content);
            }
            list.add(s);
            i++;
        }
        return list;
    }

    public static List<Tutor> ReadTutor(String url) throws Exception {
        Workbook workbook = Workbook.getWorkbook(new File(url));
        Sheet sheet = workbook.getSheet(0);
        List<Tutor> list = new ArrayList<>();
        int i = 2;
        while(i < sheet.getRows() && !sheet.getCell(0,i).getContents().equals("")) {
            Tutor s = new Tutor();
            for (int j = 0; j < 13; j++) {
                String content = sheet.getCell(j,i).getContents();
                if(j == 0) s.setNum(Integer.valueOf(content));
                if(j == 1) s.settName(content);
                if(j == 6) {
                    if(content.equals("硕导")) s.setType(1);
                    else if(content.equals("博导")) s.setType(2);
                }
                if(j == 8) s.setCenterName(content);
                if(j == 9) s.setIsAssess(Integer.valueOf(content));
                if(j == 10) s.setIsCheck(Integer.valueOf(content));
                if(j == 11 && !content.equals("")) {
                    s.setAssesCount(Integer.valueOf(content));
                    s.setInputAssess(true);
                }
                if(j == 12 && !content.equals("")) {
                    s.setCheckCount(Integer.valueOf(content));
                    s.setInputCheck(true);
                }
            }
            list.add(s);
            i++;
        }
        Sheet s2 = workbook.getSheet(1);
        int j = 2;
        while(j < s2.getRows() && !s2.getCell(0,j).getContents().equals("")) {
            Tutor t = new Tutor();
            for(int k = 0; k < 6; k++) {
                String content = s2.getCell(k,j).getContents();
                if(k == 0) t.setNum(Integer.valueOf(content));
                if(k == 1) t.settName(content);
                if(k == 2) t.setCenterName(content);
                if(k == 5) t.setAssesCount(Integer.valueOf(content));
            }
            t.setInputAssess(true);
            t.setCheckCount(0);
            t.setInputCheck(true);
            list.add(t);
            j++;
        }
        return list;
    }

    public static void init(List<Student> sl, List<Tutor> tl) {
        int inputAssessCount = 0, inputCheckCount = 0, a = 0, c = 0;
        for(int i = 0; i < tl.size(); i++) {
            if(tl.get(i).isInputAssess()) {
                inputAssessCount += tl.get(i).getAssesCount();
                a++;
            }
            if(tl.get(i).isInputCheck()) {
                inputCheckCount += tl.get(i).getCheckCount();
                c++;
            }
        }
        int acount = (sl.size()*2-inputAssessCount)/(tl.size()-a);
        int aremain = (sl.size()*2-inputAssessCount)-(tl.size()-a)*acount;
        int ccount = (sl.size()-inputCheckCount)/(tl.size()-c);
        int cremain = (sl.size()-inputCheckCount)-(tl.size()-c)*ccount;
        for (int i = 0; i < tl.size(); i++) {
            Tutor t = tl.get(i);
            if(!t.isInputAssess() && t.getIsAssess() != 0) t.setAssesCount(acount);
            if(!t.isInputCheck() && t.getIsCheck() != 0) t.setCheckCount(ccount);
        }
        while(cremain > 0){
            for(int i = 0; i < tl.size(); i++) {
                Tutor t = tl.get(i);
                if (!t.isInputCheck() && t.getIsCheck() != 0) {
                    t.setCheckCount(t.getCheckCount() + 1);
                    cremain--;
                }
            }
        }
        while(aremain > 0) {
            for (int i = 0; i < tl.size(); i++) {
                Tutor t = tl.get(i);
                if (!t.isInputAssess() && t.getIsAssess() != 0 && t.getCheckCount() != 0) {
                    int x = t.getAssesCount(), y = t.getCheckCount();
                    t.setAssesCount(Math.max(x + 1, y + 1));
                    if(x >= y) aremain -= 1;
                    else aremain -= (y-x+1);
                }
                else if (!t.isInputAssess() && t.getIsAssess() != 0) {
                    t.setAssesCount(t.getAssesCount() + 1);
                    aremain--;
                }

            }
        }
    }
}
