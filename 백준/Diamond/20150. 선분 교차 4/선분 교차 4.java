import java.util.*;
import java.io.*;

class Main {
    static long x_cur, k = 1000000007, t;

    static class Point implements Comparable<Point> {
        long x, y;

        @Override
        public int compareTo(Point i) {
            if (x != i.x) return Long.compare(x, i.x);
            return Long.compare(y, i.y);
        }
    }

    static class Line implements Comparable<Line> {
        Point a, b;
        int idx;

        double Eval() {
            return 1.0 * (b.y - a.y) / (b.x - a.x) * (x_cur - a.x) + a.y;
        }

        @Override
        public int compareTo(Line i) {
            double diff = Eval() - i.Eval();
            if (Math.abs(diff) > 1e-6) return Double.compare(diff, 0.0);
            return Integer.compare(idx, i.idx);
        }
    }

    static class Event implements Comparable<Event> {
        long x, y;
        int t, idx;

        public Event(long x, long y, int t, int idx) {
            this.x = x;
            this.y = y;
            this.t = t;
            this.idx = idx;
        }

        @Override
        public int compareTo(Event i) {
            if (x != i.x) return Long.compare(x, i.x);
            if (t != i.t) return Integer.compare(t, i.t);
            return Long.compare(y, i.y);
        }
    }

    static int CCW(Point a, Point b, Point c) {
        double ret = 1.0 * (b.x - a.x) * (c.y - b.y) - 1.0 * (c.x - b.x) * (b.y - a.y);
        return Math.abs(ret) > 1e-6 ? (ret > 0 ? 1 : -1) : 0;
    }

    static boolean IsCross(Line a, Line b) {
        int t1 = CCW(a.a, a.b, b.a) * CCW(a.a, a.b, b.b);
        int t2 = CCW(b.a, b.b, a.a) * CCW(b.a, b.b, a.b);
        if (t1 < 0 && t2 < 0) return true;
        if (t1 == 0 && t2 == 0) return b.a.compareTo(a.b) <= 0 && a.a.compareTo(b.b) <= 0;
        return t1 <= 0 && t2 <= 0;
    }

    static boolean Sol(List<Line> v) {
        int n = v.size();
        List<Event> E = new ArrayList<>();
        TreeSet<Line> S = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            E.add(new Event(v.get(i).a.x, v.get(i).a.y, 0, i));
            E.add(new Event(v.get(i).b.x, v.get(i).b.y, 1, i));
        }

        Collections.sort(E);

        for (Event event : E) {
            x_cur = event.x;
            if (event.t == 0) {
                Line line = v.get(event.idx);
                S.add(line);

                Line nextLine = S.higher(line);
                if (nextLine != null && IsCross(line, nextLine)) return true;

                Line prevLine = S.lower(line);
                if (prevLine != null && IsCross(line, prevLine)) return true;
            } else {
                Line line = v.get(event.idx);
                Line prevLine = S.lower(line);
                Line nextLine = S.higher(line);
                if (prevLine != null && nextLine != null && IsCross(prevLine, nextLine)) return true;
                S.remove(line);
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        List<Line> v = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            Line line = new Line();
            line.a = new Point();
            line.b = new Point();

            line.a.x = Long.parseLong(st.nextToken());
            line.a.y = Long.parseLong(st.nextToken());
            line.b.x = Long.parseLong(st.nextToken());
            line.b.y = Long.parseLong(st.nextToken());
            t = line.a.x + k * line.a.y;
            line.a.y -= k * line.a.x;
            line.a.x = t;
            t = line.b.x + k * line.b.y;
            line.b.y -= k * line.b.x;
            line.b.x = t;

            if (line.a.compareTo(line.b) > 0) {
                Point temp = line.a;
                line.a = line.b;
                line.b = temp;
            }

            line.idx = i;
            v.add(line);
        }

        if (Sol(v)) System.out.println("1");
        else System.out.println("0");
    }
}
