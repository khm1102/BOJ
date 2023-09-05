import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> nums = new PriorityQueue<>((a, b) -> b - a);

        int n, m, answer = 0, temp = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int input = Integer.parseInt(st.nextToken());
            nums.add(input);
            temp += input;

            while (temp >= m) {
                answer++;
                temp -= nums.poll() * 2;
            }
        }

        System.out.println(answer);
    }
}
