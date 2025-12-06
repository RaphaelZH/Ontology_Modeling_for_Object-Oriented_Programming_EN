class A1 {
    private String a1 = "";

    public String getA1() {
        return a1;
    }

    public void setA1(String value) {
        this.a1 = value;
    }
}

public class Main {
    public static void main(String[] args) {

        A1 d = new A1();
        d.setA1("example");
        System.out.println(d.getA1());
    }
}