import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final double PI = 3.14159265;

    public static double getRadius(double x) {
        return x * PI / 180;
    }

    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while ((line = br.readLine()) != null && !line.isEmpty()) {
            StringTokenizer st = new StringTokenizer(line);
            double r = Double.parseDouble(st.nextToken());
            double h = Double.parseDouble(st.nextToken());
            double d1 = Double.parseDouble(st.nextToken());
            double A1 = Double.parseDouble(st.nextToken());
            double d2 = Double.parseDouble(st.nextToken());
            double A2 = Double.parseDouble(st.nextToken());

            double R = Math.sqrt(h * h + r * r);
            double T = 2 * PI * r / R;

            A2 = Math.abs(A1 - A2);
            if (A2 > 180) {
                A2 = 360 - A2;
            }

            double ret = Math.sqrt(
                    (d1 * d1 + d2 * d2) - 2 * d1 * d2 * Math.cos(getRadius(A2) * T / 2 / PI)
            );

            System.out.printf("%.2f%n", ret);
        }
    }
    public static void main(String[] args) throws IOException {
        solution();
    }
}
