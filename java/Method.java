package javastudy;

public class Method {
    // 메소드 - 객체의 행동(클래스가 가지고 있는 기능), 입력값: 매개변수, 결과값: 리턴값

    public static void main(String[] args){

//        public 리턴타입 메소드명 (매개변수 들) {구현}
        //case1 리턴타입이 없음
        public void method1 (){
            System.out.println("m1이 실행됨..");
        }

        //case2 인풋 정수는 있는데 리턴을 안 함
        public void method2 (int x){
            System.out.println(x + "를 이용한 m2가 실행됨");
        }

        //case3 인풋 없고 출력값은 리턴함
        public int method3(){
            System.out.println("m3 실행");
            return 10;
        }

        //case4 입력값이 두개 이상, 리턴 안 함
        public void method4(int x, int y){
            System.out.println(x + y +"method4 실행");
        }

        //case5 입력있고 리턴도 있음
        public int method5(int y){
            System.out.println(y + "이용한 m5 실행");
            return y * 2;
        }

    }

}
