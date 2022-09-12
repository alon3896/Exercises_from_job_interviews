package NumToWords;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        int number = 30;
        ToWord convert = new ToWord(number);
        System.out.println(convert.convert());



    }

}
