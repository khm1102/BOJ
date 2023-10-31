import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

class Point {
    long X, Y;

    public Point(long X, long Y) {
        this.X = X;
        this.Y = Y;
    }
}

public class Main {
    static long INF = (long) 2e9;
    static long maxD;
    static long X1, Y1, X2, Y2;
    static Point Center;
    static ArrayList<Point> Point;
    static ArrayList<Point> CV;

    static void init() {
        maxD = 0;
        X1 = X2 = Y1 = Y2 = 0;
        Center = new Point(0, 0);
        Point = new ArrayList<>();
        CV = new ArrayList<>();
    }

    static long distance(Point A, Point B) {
        return (A.X - B.X) * (A.X - B.X) + (A.Y - B.Y) * (A.Y - B.Y);
    }

    static long CCW(Point A, Point B, Point C) {
        long OP = ((A.X * B.Y) + (B.X * C.Y) + (C.X * A.Y));
        OP -= ((A.Y * B.X) + (B.Y * C.X) + (C.Y * A.X));
        return OP;
    }

    static boolean Comp(Point A, Point B) {
        long NowCCW = CCW(Point.get(0), A, B);
        if (NowCCW > 0) {
            return true;
        } else if (NowCCW < 0) {
            return false;
        }
        if (A.X != B.X) {
            return (A.X < B.X);
        }
        return (A.Y < B.Y);
    }

    static void grahamScan() {
        long minX = INF;
        long minY = INF;
        int First = 0;

        for (int i = 0; i < Point.size(); i++) {
            if ((minX > Point.get(i).X) || ((minX == Point.get(i).X) && (minY > Point.get(i).Y))) {
                minX = Point.get(i).X;
                minY = Point.get(i).Y;
                First = i;
            }
        }
        Collections.swap(Point, 0, First);
        Collections.sort(Point.subList(1, Point.size()), new Comparator<Point>() {
            @Override
            public int compare(Point A, Point B) {
                long NowCCW = CCW(Point.get(0), A, B);
                if (NowCCW > 0) {
                    return -1;
                } else if (NowCCW < 0) {
                    return 1;
                }
                if (A.X != B.X) {
                    return Long.compare(A.X, B.X);
                }
                return Long.compare(A.Y, B.Y);
            }
        });

        for (int i = 0; i < Point.size(); i++) {
            while ((CV.size() >= 2) && (CCW(Point.get(i), CV.get(CV.size() - 2), CV.get(CV.size() - 1)) <= 0)) {
                CV.remove(CV.size() - 1);
            }
            CV.add(Point.get(i));
        }
    }

    static void rotatingCalipers() {
        int Left = 0;
        int Right = 0;

        for (int i = 0; i < CV.size(); i++) {
            if (CV.get(i).X < CV.get(Left).X) {
                Left = i;
            } else if (CV.get(i).X > CV.get(Right).X) {
                Right = i;
            }
        }
        maxD = distance(CV.get(Left), CV.get(Right));
        X1 = CV.get(Left).X;
        Y1 = CV.get(Left).Y;
        X2 = CV.get(Right).X;
        Y2 = CV.get(Right).Y;

        for (int i = 0; i < CV.size(); i++) {
            Point Prev = new Point(CV.get((Left + 1) % CV.size()).X - CV.get(Left).X, CV.get((Left + 1) % CV.size()).Y - CV.get(Left).Y);
            Point Next = new Point(CV.get(Right).X - CV.get((Right + 1) % CV.size()).X, CV.get(Right).Y - CV.get((Right + 1) % CV.size()).Y);

            if (CCW(Center, Prev, Next) > 0) {
                Left = (Left + 1) % CV.size();
            } else {
                Right = (Right + 1) % CV.size();
            }

            if (maxD < distance(CV.get(Left), CV.get(Right))) {
                maxD = distance(CV.get(Left), CV.get(Right));
                X1 = CV.get(Left).X;
                Y1 = CV.get(Left).Y;
                X2 = CV.get(Right).X;
                Y2 = CV.get(Right).Y;
            }
        }
    }

    static void settings() {
        grahamScan();
        rotatingCalipers();
    }

    static void findAnswer() {
        System.out.println(X1 + " " + Y1 + " " + X2 + " " + Y2);
    }

    static void input() {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        while (T-- > 0) {
            init();
            int N = scanner.nextInt();
            for (int i = 0; i < N; i++) {
                long X = scanner.nextLong();
                long Y = scanner.nextLong();
                Point Tmp = new Point(X, Y);
                Point.add(Tmp);
            }
            settings();
            findAnswer();
        }
    }

    public static void main(String[] args) {
        input();
    }
}
