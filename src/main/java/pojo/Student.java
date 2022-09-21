package pojo;

public class Student {
    private int num;
    private String sId;
    private String sName;
    private String tutorName;
    private String centerName;
    private String firstTutor;
    private String secondTutor;

    public Student() {
    }

    public Student(int num, String sId, String sName, String tutorName, String centerName) {
        this.num = num;
        this.sId = sId;
        this.sName = sName;
        this.tutorName = tutorName;
        this.centerName = centerName;
    }

    @Override
    public String toString() {
        return "Student{" +
                "num=" + num +
                ", sId=" + sId +
                //", sName='" + sName + '\'' +
                //", tutorName='" + tutorName + '\'' +
                //", centerName='" + centerName + '\'' +
                ", firstTutor=" + firstTutor +
                ", secondTutor=" + secondTutor+
                //", systemTutor=" + systemTutor +
                '}';
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public String getsId() {
        return sId;
    }

    public void setsId(String sId) {
        this.sId = sId;
    }

    public String getsName() {
        return sName;
    }

    public void setsName(String sName) {
        this.sName = sName;
    }

    public String getTutorName() {
        return tutorName;
    }

    public void setTutorName(String tutorName) {
        this.tutorName = tutorName;
    }

    public String getCenterName() {
        return centerName;
    }

    public void setCenterName(String centerName) {
        this.centerName = centerName;
    }

    public String getFirstTutor() {
        return firstTutor;
    }

    public void setFirstTutor(String firstTutor) {
        this.firstTutor = firstTutor;
    }

    public String getSecondTutor() {
        return secondTutor;
    }

    public void setSecondTutor(String secondTutor) {
        this.secondTutor = secondTutor;
    }

    public String[] toArray() {
        String[] res = new String[8];
        res[0] = String.valueOf(this.num);
        res[1] = this.sId;
        res[2] = this.sName;
        res[3] = this.tutorName;
        res[4] = this.centerName;
        res[5] = this.firstTutor;
        res[6] = this.secondTutor;
        res[7] = this.firstTutor;
        return res;
    }
}
