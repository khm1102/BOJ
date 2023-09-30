import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {
    static class Circle {
        int id, x, y, r;

        Circle(int id, int x, int y, int r) {
            this.id = id;
            this.x = x;
            this.y = y;
            this.r = r;
        }
    }

    static int[] p;
    static List<Integer>[] graph;
    static int answer;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        Circle[] circles = new Circle[N + 1];
        circles[0] = new Circle(0, 0, 0, 0);

        for (int i = 1; i <= N; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int r = scanner.nextInt();
            circles[i] = new Circle(i, x, y, r);
        }

        Arrays.sort(circles, new Comparator<Circle>() {
            @Override
            public int compare(Circle o1, Circle o2) {
                return Integer.compare(o1.r, o2.r);
            }
        });

        p = new int[N + 1];
        graph = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        List<Integer> endNodes = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            Circle ci = circles[i];
            for (int j = i + 1; j <= N; j++) {
                Circle cj = circles[j];
                double d = Math.sqrt(Math.pow(ci.x - cj.x, 2) + Math.pow(ci.y - cj.y, 2));
                if (d < Math.abs(cj.r - ci.r)) {
                    graph[ci.id].add(cj.id);
                    graph[cj.id].add(ci.id);
                    p[ci.id] = cj.id;
                    break;
                }
            }
            if (p[ci.id] == 0) {
                graph[ci.id].add(0);
                graph[0].add(ci.id);
            }
            if (graph[ci.id].size() == 1) {
                endNodes.add(ci.id);
            }
        }

        answer = 0;

        for (int s : endNodes) {
            boolean[] visited = new boolean[N + 1];
            dfs(s, 0, visited);
        }

        System.out.println(answer);
    }

    static void dfs(int node, int depth, boolean[] visited) {
        visited[node] = true;
        for (int n : graph[node]) {
            if (!visited[n]) {
                dfs(n, depth + 1, visited);
            }
        }
        answer = Math.max(answer, depth);
    }
}
