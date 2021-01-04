package javastudy;

public class ForExam {

    public  static  void main(String[] args) {

        int total = 0;
//        for(int i = 1; i <= 100; i++){
//            total = total + i;
//        }

        for(int i = 1; i <= 100; i++) {
//            if (i % 2 != 0) {
//                continue;
//            }
            if(i == 50){
                break;
            }
            total = total + i;  //짝수만 누적
        }
        System.out.println(total);
    }
}
