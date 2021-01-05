package javastudy;

public class StringExam {

    public static void main(String[] args){
        //String 클래스 문자열을 표현하는 자바에서 가장 많이 씀, new없이도 인스턴스 만들 수 있음!!!
        String str1 = "hello";  //문자열이 상수가 저장되는 곳에 저장됨 str1,str2에서는
        String str2 = "hello";   //상수영역에 있는것을 가리킴 str1과 str2는 같은 인스턴스를 참조함
        String str3 = new String("hello"); //hello를 str3,4 모두 heap영역에 만들고 그걸 참조
        String str4 = new String("hello");

        if(str1 == str2) //주소가 같은지 비교

            System.out.println("str1과 str2는 같은 레퍼런스이다.");

        if(str1 == str3)
            System.out.println("str1과 str3는 같은 레퍼런스이다");

        if(str3 == str4)
            System.out.println("str3과 str4는 같은 레퍼런스이다");

        System.out.println(str1);
        System.out.println(str1.substring(3)); //자른 후에도 스트링은 변하지 않음!

        System.out.println(str1); //한 번 만들어진 스트링의 값은 변하지 않음!

    }
}
