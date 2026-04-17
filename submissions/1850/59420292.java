import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);  
        long a = sc.nextLong();
        long b = sc.nextLong();
        while (b > 0) {
            long t = b;
            b = a % b;
            a = t;
        }
        String result = "1".repeat((int)a);
        System.out.println(result);
    }
}