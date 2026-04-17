import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long r = a*b;
        System.out.println(r/gcd(a,b));
    }

    public static long gcd(long a, long b){
        if(b == 0) {
            return a;
        }
        else {
            return gcd(b, a % b);
        }
    }
}