import java.util.Scanner;

public class Main {
    static char[][] stars;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        stars = new char[N][2 * N - 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 2 * N -1 ; j++){
                stars[i][j] = ' ';
            }
        }

        drawStar(N, N - 1, 0);

        for (int i = 0; i < N; i++){
            System.out.println(new String(stars[i]));
        }
    }

    static void drawStar(int N, int x, int y){
        if (N == 3){
            stars[y][x] = '*';
            stars[y + 1] [x - 1] = stars[y + 1] [x + 1] = '*';
            stars[y + 2][x - 2] = stars[y + 2][x - 1] = stars[y + 2][x] = stars[y + 2][x + 1] = stars[y + 2][x + 2] = '*';

        }else{
            drawStar(N / 2, x , y);
            drawStar(N / 2, x - N / 2, y + N / 2);
            drawStar(N / 2, x + N / 2, y + N / 2);
        }
    }
}
