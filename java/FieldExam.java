package javastudy;

public class FieldExam {// 필드 - 객체의 속성

    public static void main(String[] args){

         Field f1 = new Field();
         Field f2 = new Field();

         f1.name = "A";
         f1.number = 1234;

         f2.name = "B";
         f2.number = 1111;

        System.out.println(f1.name);
        System.out.println(f1.number);

        System.out.println(f2.name);
        System.out.println(f2.number);

    }
}
