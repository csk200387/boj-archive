import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long result = fac(n);
        System.out.println(result);
    }
    public static long fac(long n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * fac(n-1);
    }
}