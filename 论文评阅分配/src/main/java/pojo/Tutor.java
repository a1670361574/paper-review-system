package pojo;

public class Tutor {
    private int num;
    private String tName;
    private int type;//硕博导or校外
    private String centerName;
    private int assesCount;
    private int checkCount;
    private int isAssess;
    private int isCheck;
    private boolean inputAssess;
    private boolean inputCheck;
    private boolean Out;
    public Tutor() {
    }

    public boolean isInputAssess() {
        return inputAssess;
    }

    public void setInputAssess(boolean inputAssess) {
        this.inputAssess = inputAssess;
    }

    public boolean isInputCheck() {
        return inputCheck;
    }

    public void setInputCheck(boolean inputCheck) {
        this.inputCheck = inputCheck;
    }

    public Tutor(int num, String tName, int type, String centerName, int assesCount, int checkCount) {
        this.num = num;
        this.tName = tName;
        this.type = type;
        this.centerName = centerName;
        this.assesCount = assesCount;
        this.checkCount = checkCount;
    }

    @Override
    public String toString() {
        return "Tutor{" +
                "num=" + num +
                ", tName='" + tName + '\'' +
                ", type=" + type +
                ", centerName='" + centerName + '\'' +
                ", assesCount=" + assesCount +
                ", checkCount=" + checkCount +
                ", isAssess=" + isAssess +
                ", isCheck=" + isCheck +
                ", inputAssess=" + inputAssess +
                ", inputCheck=" + inputCheck +
                '}';
    }

    public int getIsAssess() {
        return isAssess;
    }

    public void setIsAssess(int isAssess) {
        this.isAssess = isAssess;
    }

    public int getIsCheck() {
        return isCheck;
    }

    public void setIsCheck(int isCheck) {
        this.isCheck = isCheck;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public String gettName() {
        if(tName == null) return "null";
        return tName;
    }

    public void settName(String tName) {
        this.tName = tName;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public String getCenterName() {
        return centerName;
    }

    public void setCenterName(String centerName) {
        this.centerName = centerName;
    }

    public int getAssesCount() {
        return assesCount;
    }

    public void setAssesCount(int assesCount) {
        this.assesCount = assesCount;
    }

    public int getCheckCount() {
        return checkCount;
    }

    public void setCheckCount(int checkCount) {
        this.checkCount = checkCount;
    }
}
