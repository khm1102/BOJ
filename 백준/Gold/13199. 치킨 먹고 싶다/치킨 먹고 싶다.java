import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int f = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            int d = 0;
            int n = 0;
            n = (m / p) + ((m / p) * c) / f;
            d = (m / p);
            int res = (m / p) * c;
            if (res >= f) {
                d += (res - f) / (f - c) + 1;
            }
            bw.write((d - n) + "\n");
        }

        br.close();
        bw.close();
    }
}
