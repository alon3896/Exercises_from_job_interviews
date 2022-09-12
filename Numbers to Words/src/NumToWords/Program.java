package NumToWords;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("choose a number between 1 to 999 to convert to the name of the number");
        int number = scan.nextInt();
        ToWord convert = new ToWord(number); // initialize the converting instance, requires to send value of number to convert
        System.out.println(convert.convert());



    }

}
