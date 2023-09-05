import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] on = new int[4];
        int people = 0;

        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 4; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            people += b;
            people -= a;
            on[i] = people;
        }

        int maxPeople = Integer.MIN_VALUE;
        for (int i = 0; i < 4; i++) {
            if (on[i] > maxPeople) {
                maxPeople = on[i];
            }
        }

        System.out.println(maxPeople);
    }
}
