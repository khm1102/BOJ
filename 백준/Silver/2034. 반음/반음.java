import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int[] arr = new int[10001];
        char[] piano = { 'C', 'X', 'D', 'X', 'E', 'F', 'X', 'G', 'X', 'A', 'X', 'B' };

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
            arr[i] %= 12;
        }
        
        for (char c = 'A'; c <= 'G'; c++) {
            int idx = 0;
            char last = ' ';
            
            for (int i = 0; i < 12; i++) {
                if (piano[i] == c) {
                    idx = i;
                    break;
                }
            }
            
            boolean chk = true;
            for (int i = 0; i < n; i++) {
                idx += arr[i];
                idx %= 12;
                if (idx < 0) idx += 12;
                
                if (piano[idx] == 'X') {
                    chk = false;
                    break;
                }
                last = piano[idx];
            }
            
            if (chk) {
                System.out.println(c + " " + last);
            }
        }
    }
}
