import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;
import java.util.StringTokenizer;

public class Main {
    static class FastIO {
        BufferedReader br;
        StringTokenizer st;

        FastIO() {
            br = new BufferedReader(new InputStreamReader(System.in));
            st = null;
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

    static class Rand {
        Random rg;
        Random rd;

        Rand() {
            rg = new Random();
            rd = new Random(rg.nextLong());
        }

        int nextInt(int l, int r) {
            return rd.nextInt(r - l + 1) + l;
        }
    }

    public static void main(String[] args) {
        FastIO io = new FastIO();
        Rand rnd = new Rand();

        long n, pp, f = 0;
        long[] x, y;

        n = io.nextLong();
        pp = io.nextLong();
        if (n == 1) {
            System.out.println("possible");
            return;
        }

        x = new long[101010];
        y = new long[101010];
        for (int i = 1; i <= n; i++) {
            x[i] = io.nextLong();
            y[i] = io.nextLong();
        }

        for (int t = 1; t <= 150; t++) {
            long p = rnd.nextInt(1, (int) (n - 1));
            long q = rnd.nextInt((int) (p + 1), (int) n);
            long a = y[(int) p] - y[(int) q];
            long b = x[(int) p] - x[(int) q];
            long cnt = 0;

            for (int i = 1; i <= n; i++) {
                if (a * (x[i] - x[(int) p]) == b * (y[i] - y[(int) p])) {
                    cnt++;
                }
            }

            if (cnt >= (n * pp + 99) / 100) {
                f = 1;
                break;
            }
        }

        if (f == 1) {
            System.out.println("possible");
        } else {
            System.out.println("impossible");
        }
    }
}