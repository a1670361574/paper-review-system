package service;

import pojo.Student;
import pojo.Tutor;

import java.util.List;
import java.util.PriorityQueue;

public class access {
    public static void start(List<Student> sl, List<Tutor> tl) {
        PriorityQueue<Tutor> pq = new PriorityQueue<>((a,b)->(b.getCheckCount()-a.getCheckCount()));
        PriorityQueue<Tutor> pq2 = new PriorityQueue<>((a,b)->(b.getAssesCount()-a.getAssesCount()));
        for (int j = 0; j < tl.size(); j++) {
            pq.offer(tl.get(j));
        }
        for (int i = 0; i < sl.size(); i++) {
            Student s = sl.get(i);
            while(s.getFirstTutor() == null && !pq.isEmpty()) {
                Tutor t = pq.poll();
                if(t.getAssesCount() > 0 && t.getCheckCount() <= 0) pq2.offer(t);
                if(t.getAssesCount() > 0 && t.getCheckCount() > 0) {
                    s.setFirstTutor(t.gettName());
                    t.setCheckCount(t.getCheckCount()-1);
                    t.setAssesCount(t.getAssesCount()-1);
                    pq.offer(t);
                }
            }
        }
        while(!pq.isEmpty()) pq2.offer(pq.poll());
        for (int i = 0; i < sl.size(); i++) {
            Student s = sl.get(i);
            Tutor temp = null;
            while(s.getSecondTutor() == null && !pq2.isEmpty()) {
                Tutor t = pq2.poll();
                if(t.gettName() == s.getFirstTutor()) {
                    temp = t;
                    continue;
                }
                if(t.getAssesCount() > 0 && t.gettName() != s.getFirstTutor()) {
                    s.setSecondTutor(t.gettName());
                    t.setAssesCount(t.getAssesCount()-1);
                    pq2.offer(t);
                }
            }
            if(temp != null) pq2.offer(temp);
        }
    }
}
