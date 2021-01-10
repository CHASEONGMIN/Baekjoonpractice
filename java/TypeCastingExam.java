public class TypeCastingExam {
    public static void main(String[] args){
        int x = 50000;
        long y = x;

        long x2 = 5;
//        int y2 = x2;   에러 발생
        int y2 = (int) x2;

        System.out.println(y2);

    }
}
