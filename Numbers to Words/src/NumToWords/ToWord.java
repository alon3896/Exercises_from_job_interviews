package NumToWords;

public class ToWord {
    public String number = "";

    //constructor convert the int into string for easy access to all the digits in the number
    public ToWord(int n){
        number = n+"";
    }

    // function that returns the name of the number using the rest of the function in the class
    public String convert(){
        int n = 0;
        if (number.equals("0")){
            return "zero";
        }
        else {
            if (number.length() == 3) {
                n = 0;
            } else if (number.length() == 2) {
                n = -1;
            } else if (number.length() == 1) {
                n = -2;
            }
            return hundreds(n) + " " + tens(n) + " " + ones(n);
        }
    }


    //function that returns string with the name of the hundreds value using switch case
    // private not meant for using outside this class
    private String hundreds(int n){
        try {
            switch (number.charAt(n)) {
                case '0':
                    return "";

                case '1':
                    return "One hundred";

                case '2':
                    return "Two hundred";

                case '3':
                    return "three hundred";

                case '4':
                    return "four hundred";

                case '5':
                    return "five hundred";

                case '6':
                    return "six hundred";

                case '7':
                    return "seven hundred";

                case '8':
                    return "eight hundred";

                case '9':
                    return "nine hundred";

                default:
                    return " ";
            }
        }
        catch (StringIndexOutOfBoundsException e){
            return "";
        }

    }
    //function that returns string with the name of the tens value using switch case
// private not meant for using outside this class
    private String tens(int n){
        try {

            switch (number.charAt(n + 1)) {
                case '0':
                    return "and";
                case '2':
                    return "Twenty";

                case '3':
                    return "thirty";

                case '4':
                    return "forty";

                case '5':
                    return "fifty";

                case '6':
                    return "sixty";

                case '7':
                    return "seventy";

                case '8':
                    return "eighty";

                case '9':
                    return "ninety";

                default:
                    return " ";
            }
        }
        catch (StringIndexOutOfBoundsException e){
            return "";
        }
    }
    //function that returns string with the name of the ones value using switch case
    // private not meant for using outside this class

    private String ones(int n){
        try {
            switch (number.charAt(n + 2)) {
                case '0':
                    return "";
                //break;
                case '1':
                    return "One";
                //  break;
                case '2':
                    return "Two";
                //  break;
                case '3':
                    return "three";
                // break;
                case '4':
                    return "four";
                // break;
                case '5':
                    return "five";
                // break;
                case '6':
                    return "six";
                //  break;
                case '7':
                    return "seven";
                //  break;
                case '8':
                    return "eight";
                //  break;
                case '9':
                    return "nine";
                //  break;
                default:
                    return " ";
            }
        }
        catch (StringIndexOutOfBoundsException e){
            return "";
        }
    }

}
