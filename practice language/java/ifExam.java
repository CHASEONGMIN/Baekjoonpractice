public class ifExam {

    public static void main(String[] args){

        int x = 50;
        int y = 60;

        if(x > y){
            System.out.println("x는 y보다 작습니다");
            System.out.println("test");
        }

        if(x > y)
            System.out.println("x와 y는 같다");  //{가 없으면 한줄만 if문 처리
             System.out.println("test");

        if(x == y){
            System.out.println("x는 y와 같다.");}
        else if(x > y){
            System.out.println("x는 y보다 크다.");
        }
        else{
            System.out.println("x는 y보다 작다");
        }
    }
}
