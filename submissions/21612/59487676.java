import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = n*5-400;
        System.out.println(i);
        if (n == i) System.out.println("0");
        else if (n > i) System.out.println("1");
        else System.out.println("-1");
        sc.close();
    }
}