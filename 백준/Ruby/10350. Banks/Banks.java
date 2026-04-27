import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[30010];
        long[] b = new long[30010];
        long s = 0, res = 0;
        for (int i = 0; i < n; i++) {
            // 입력
            a[i] = sc.nextLong();
        }
        for (int i = 0; i < n; i++) {
            // 누적합
            a[i+n] = a[i];
            s += a[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // 더하기
                b[j + 1] = b[j] + a[i + j];
                if (b[j + 1] < 0) {
                    // 절댓값
                    res += (Math.abs(b[j + 1]) + s - 1) / s;
                }
            }
        }
        System.out.print(res);
    }
}
