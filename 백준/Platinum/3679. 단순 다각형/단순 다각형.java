import java.util.*;

class P implements Comparable<P> {
    long x, y, i;

    public P(long x, long y, long i) {
        this.x = x;
        this.y = y;
        this.i = i;
    }

    @Override
    public int compareTo(P t) {
        if (x != t.x) {
            return Long.compare(x, t.x);
        }
        return Long.compare(y, t.y);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        P p = (P) o;
        return x == p.x && y == p.y;
    }
}

public class Main {
    static int c(P a, P b, P c) {
        long r = a.x * b.y + b.x * c.y + c.x * a.y;
        r -= b.x * a.y + c.x * b.y + a.x * c.y;
        if (r > 0)
            return 1;
        if (r < 0)
            return -1;
        return 0;
    }

    static long d(P a, P b) {
        long x = a.x - b.x;
        long y = a.y - b.y;
        return x * x + y * y;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        while (t-- > 0) {
            int n = s.nextInt();
            List<P> v = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                long x = s.nextLong();
                long y = s.nextLong();
                v.add(new P(x, y, i));
            }
            Collections.sort(v);
            Collections.swap(v, 0, v.indexOf(Collections.min(v, Comparator.comparing(p -> p.x))));
            v.subList(1, v.size()).sort((a, b) -> {
                int k = c(v.get(0), a, b);
                if (k != 0)
                    return k > 0 ? 1 : -1;
                return Long.compare(d(v.get(0), a), d(v.get(0), b));
            });

            int p = v.size() - 1;
            for (int i = v.size() - 1; i >= 1; i--) {
                if (c(v.get(0), v.get(p), v.get(p - 1)) == 0) {
                    p--;
                } else {
                    break;
                }
            }
            Collections.reverse(v.subList(p, v.size()));
            for (P o : v) {
                System.out.print(o.i + " ");
            }
            System.out.println();
        }
        s.close();
    }
}
