import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int l = scanner.nextInt();

        Point[] buildings = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            buildings[i] = new Point(x, y);
        }

        Point[] convexHull = monotoneChain(buildings);
        double s = 0;

        for (int i = 0; i < convexHull.length; i++) {
            int prevIndex = (i == 0) ? convexHull.length - 1 : i - 1;
            s += getDist(convexHull[prevIndex], convexHull[i]);
        }

        s += 2 * Math.PI * l;
        System.out.printf("%.10f\n", s);
    }

    static double round(double n) {
        return Math.round(n * 100.0) / 100.0;
    }

    static double ccw(Point p1, Point p2, Point p3) {
        return p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y);
    }

    static Point[] monotoneChain(Point[] dots) {
        Arrays.sort(dots);
        if (dots.length <= 1) {
            return dots;
        }

        ArrayList<Point> lower = new ArrayList<>();
        for (Point d : dots) {
            while (lower.size() >= 2 && ccw(lower.get(lower.size() - 2), lower.get(lower.size() - 1), d) <= 0) {
                lower.remove(lower.size() - 1);
            }
            lower.add(d);
        }

        ArrayList<Point> upper = new ArrayList<>();
        for (int i = dots.length - 1; i >= 0; i--) {
            Point d = dots[i];
            while (upper.size() >= 2 && ccw(upper.get(upper.size() - 2), upper.get(upper.size() - 1), d) <= 0) {
                upper.remove(upper.size() - 1);
            }
            upper.add(d);
        }

        lower.remove(lower.size() - 1);
        upper.remove(upper.size() - 1);
        lower.addAll(upper);

        return lower.toArray(new Point[0]);
    }

    static double getDist(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    }

    static class Point implements Comparable<Point> {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Point other) {
            if (this.x == other.x) {
                return Integer.compare(this.y, other.y);
            }
            return Integer.compare(this.x, other.x);
        }
    }
}
