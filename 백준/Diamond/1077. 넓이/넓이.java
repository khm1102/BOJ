import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class Pair {
    double first, second;

    Pair(double first, double second) {
        this.first = first;
        this.second = second;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt();
        List<Pair> v1 = new ArrayList<>();
        List<Pair> v2 = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            v1.add(new Pair(a, b));
        }

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt(), b = sc.nextInt();
            v2.add(new Pair(a, b));
        }

        v1 = makeConvex(v1);
        v2 = makeConvex(v2);

        List<Pair> v3 = new ArrayList<>();
        for (Pair x : v1) {
            if (isInside(v2, x))
                v3.add(x);
        }
        for (Pair x : v2) {
            if (isInside(v1, x))
                v3.add(x);
        }

        for (int i = 0; i < v1.size() - 1; i++) {
            for (int j = 0; j < v2.size() - 1; j++) {
                if (cross(v1.get(i), v1.get(i + 1), v2.get(j), v2.get(j + 1))) {
                    v3.add(crossDot(v1.get(i), v1.get(i + 1), v2.get(j), v2.get(j + 1)));
                }
            }
        }
        v3 = makeConvex(v3);

        System.out.printf("%.10f\n", area(v3));
    }

    static int CCW(Pair A, Pair B, Pair C) {
        double ax = A.first, ay = A.second, bx = B.first, by = B.second, cx = C.first, cy = C.second;
        double ccw = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by);
        if (ccw < 0) return -1;
        if (ccw == 0) return 0;
        return 1;
    }

    static boolean cross(Pair A, Pair B, Pair C, Pair D) {
        if (A.first > B.first || (A.first == B.first && A.second > B.second)) {
            Pair temp = A;
            A = B;
            B = temp;
        }
        if (C.first > D.first || (C.first == D.first && C.second > D.second)) {
            Pair temp = C;
            C = D;
            D = temp;
        }

        int first_ccw = CCW(A, B, C) * CCW(A, B, D);
        int second_ccw = CCW(C, D, A) * CCW(C, D, B);
        if (first_ccw == 0 && second_ccw == 0)
            return (A.first <= D.first && A.second <= D.second) && (C.first <= B.first && C.second <= B.second);
        return first_ccw <= 0 && second_ccw <= 0;
    }

    static Pair crossDot(Pair A, Pair B, Pair C, Pair D) {
        double x1 = A.first, x2 = B.first, x3 = C.first, x4 = D.first;
        double y1 = A.second, y2 = B.second, y3 = C.second, y4 = D.second;
        double denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
        double numerator1 = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - x4 * y3);
        double numerator2 = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - x4 * y3);
        return new Pair(numerator1 / denominator, numerator2 / denominator);
    }

    static boolean isInside(List<Pair> v, Pair dot) {
        Pair dot2 = new Pair(dot.first + 1, dot.second + 2e9);
        int cnt = 0;

        int N = v.size();
        for (int i = 0; i < N - 1; i++) {
            if (cross(dot, dot2, v.get(i), v.get(i + 1)))
                cnt++;
        }
        return cnt % 2 == 1;
    }

    static double dist(Pair A, Pair B) {
        return (A.first - B.first) * (A.first - B.first) + (A.second - B.second) * (A.second - B.second);
    }

    static Pair lowDot;
    static Comparator<Pair> cmp = new Comparator<Pair>() {
        @Override
        public int compare(Pair A, Pair B) {
            int ccw = CCW(lowDot, A, B);
            if (ccw > 0) return -1;
            if (ccw == 0) return Double.compare(dist(lowDot, A), dist(lowDot, B));
            return 1;
        }
    };

    static List<Pair> makeConvex(List<Pair> v) {
        int N = v.size();
        if (N <= 2) return v;

        v.sort((A, B) -> {
            if (A.second != B.second) return Double.compare(A.second, B.second);
            return Double.compare(A.first, B.first);
        });

        lowDot = v.get(0);
        List<Pair> sortedList = v.subList(1, N);
        Collections.sort(sortedList, cmp);

        int[] stk = new int[111];
        int top = 2;
        stk[0] = 0;
        stk[1] = 1;

        for (int i = 2; i < N; i++) {
            while (top >= 2 && CCW(v.get(stk[top - 2]), v.get(stk[top - 1]), v.get(i)) <= 0) {
                top--;
            }
            stk[top++] = i;
        }

        List<Pair> ans = new ArrayList<>();
        for (int i = 0; i < top; i++)
            ans.add(v.get(stk[i]));
        ans.add(v.get(stk[0]));

        return ans;
    }

    static double area(List<Pair> v) {
        int N = v.size();
        double ans = 0;

        for (int i = 0; i < N - 1; i++) {
            ans += (v.get(i).first + v.get(i + 1).first) * (v.get(i).second - v.get(i + 1).second);
        }
        return Math.abs(ans) / 2;
    }
}
