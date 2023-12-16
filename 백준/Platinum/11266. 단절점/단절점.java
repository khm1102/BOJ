import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int V, E;
    static List<Integer>[] adj;
    static int cnt = 0;
    static int[] discovered;
    static boolean[] isCutVertex;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        V = sc.nextInt();
        E = sc.nextInt();
        adj = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) {
            adj[i] = new ArrayList<>();
        }
        discovered = new int[V + 1];
        isCutVertex = new boolean[V + 1];

        int u, v;
        for (int i = 0; i < E; i++) {
            u = sc.nextInt();
            v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }

        Arrays.fill(discovered, -1);

        for (int i = 1; i <= V; i++) {
            if (discovered[i] == -1) {
                findCutVertex(i, true);
            }
        }

        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= V; i++) {
            if (isCutVertex[i]) {
                res.add(i);
            }
        }

        System.out.println(res.size());
        for (int w : res) {
            System.out.print(w + " ");
        }
    }

    static int findCutVertex(int now, boolean isroot) {
        discovered[now] = cnt++;
        int ret = discovered[now];

        int child = 0;
        for (int next : adj[now]) {
            if (discovered[next] == -1) {
                child++;
                int subtree = findCutVertex(next, false);

                if (!isroot && subtree >= discovered[now]) {
                    isCutVertex[now] = true;
                }
                ret = Math.min(ret, subtree);
            } else {
                ret = Math.min(ret, discovered[next]);
            }
        }

        if (isroot && child >= 2) {
            isCutVertex[now] = true;
        }
        return ret;
    }
}
