import java.io.*;
import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) throws IOException {
        BigDecimal a, b, c;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] input = reader.readLine().split(" ");
        
        a = new BigDecimal(input[0]);
        b = new BigDecimal(input[1]);
        c = new BigDecimal(input[2]);
        
        BigDecimal pi = new BigDecimal("3.1415926535897932384626433832795028841971693993751058209749445923078164");

        BigDecimal left = c.divide(a, 50, BigDecimal.ROUND_HALF_UP).subtract(BigDecimal.ONE);
        BigDecimal right = c.divide(a, 50, BigDecimal.ROUND_HALF_UP).add(BigDecimal.ONE);

        while (right.subtract(left).compareTo(new BigDecimal("1e-20")) > 0) {
            BigDecimal mid = left.add(right).divide(new BigDecimal("2"), 50, BigDecimal.ROUND_HALF_UP);
            BigDecimal f_mid = a.multiply(mid).add(b.multiply(sin(mid))).subtract(c);

            if (f_mid.compareTo(BigDecimal.ZERO) > 0) {
                right = mid;
            } else if (f_mid.compareTo(BigDecimal.ZERO) < 0) {
                left = mid;
            } else {
                break;
            }
        }
        
        writer.write(String.format("%.6f%n", left.add(right).divide(new BigDecimal("2"), 6, BigDecimal.ROUND_HALF_UP)));
        writer.flush();
    }
    public static BigDecimal sin(BigDecimal x) {
        BigDecimal pi = new BigDecimal("3.1415926535897932384626433832795028841971693993751058209749445923078164");
        
        if (x.compareTo(pi.negate()) >= 0 && x.compareTo(pi) <= 0) {
            BigDecimal i = new BigDecimal("1");
            BigDecimal lasts = new BigDecimal("0");
            BigDecimal s = x;
            BigDecimal fact = new BigDecimal("1");
            BigDecimal num = x;
            BigDecimal sign = new BigDecimal("1");

            while (s.compareTo(lasts) != 0) {
                lasts = s;
                i = i.add(new BigDecimal("2"));
                fact = fact.multiply(i).multiply(i.subtract(BigDecimal.ONE));
                num = num.multiply(x).multiply(x);
                sign = sign.multiply(new BigDecimal("-1"));
                s = s.add(num.divide(fact, 50, BigDecimal.ROUND_HALF_UP).multiply(sign));
            }
            return s;
        } else if (x.compareTo(pi) > 0) {
            while (x.compareTo(pi) > 0) {
                x = x.subtract(pi.multiply(new BigDecimal("2")));
            }
            return sin(x);
        } else {
            while (x.compareTo(pi.negate()) < 0) {
                x = x.add(pi.multiply(new BigDecimal("2")));
            }
            return sin(x);
        }
    }
}