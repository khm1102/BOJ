import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        // 입력받은 문자열
        String str = bf.readLine();
        int[] cnt = new int[26];

        // 대소문자를 구분하여 빈도수 계산
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if ('a' <= ch && ch <= 'z') {
                cnt[ch - 'a']++;
            } else if ('A' <= ch && ch <= 'Z') {
                cnt[ch - 'A']++;
            }
        }

        // 가장 많이 사용된 알파벳의 빈도수와 인덱스 찾기
        int max = 0;
        int maxIndex = 0;
        for (int i = 0; i < cnt.length; i++) {
            if (cnt[i] > max) {
                max = cnt[i];
                maxIndex = i;
            }
        }

        // 가장 많이 사용된 알파벳이 여러 개인 경우
        int cntMax = 0;
        for (int i = 0; i < cnt.length; i++) {
            if (cnt[i] == max) {
                cntMax++;
            }
        }

        // 결과 출력
        if (cntMax > 1) {
            System.out.println("?");
        } else {
            System.out.println((char) ('A' + maxIndex));
        }
    }
}
