import java.io.*;
import java.math.BigInteger;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static BigInteger ZERO = BigInteger.ZERO;
    private static BigInteger ONE = BigInteger.ONE;

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        BigInteger start = new BigInteger(tokenizer.nextToken());
        BigInteger end = new BigInteger(tokenizer.nextToken());

        BigInteger partialUntilStart;
        if (start.compareTo(ZERO) == 0) {
            partialUntilStart = ZERO;
        } else {
            partialUntilStart = partialSum(start.subtract(ONE));
        }

        BigInteger partialUntilEnd = partialSum(end);
        BigInteger result = partialUntilEnd.subtract(partialUntilStart);
        
        writer.write(result.toString());
        writer.newLine();
        writer.flush();
    }

    public static BigInteger partialSum(BigInteger num) {
        // S(0) = 0, S(1) = 1
        if (num.compareTo(ONE) == 0 || num.compareTo(ZERO) == 0) {
            return num;
        }

        // S(1[A...]) := (#[A...] + 1) + S(1 << len([A...]) - 1) + S([A...])
        // When len([A...]) = k, S(1 << len([A...]) - 1) == k * (1 << (k - 1))
        int length = num.bitLength();
        BigInteger tailMask = ONE.shiftLeft(length - 1).subtract(ONE);
        BigInteger tail = num.and(tailMask);
        // System.out.println("""
        //     S(%s): tail = %s""".formatted(num.toString(), tail.toString()));

        // (#[A...] + 1)
        BigInteger result = tail.add(ONE);
        
        // k * (1 << (k - 1))
        int k = length - 1;
        BigInteger temp = BigInteger.valueOf(k).multiply(
            ONE.shiftLeft(k - 1)
        );
        result = result.add(temp);

        // System.out.println("""
        //     S(%s): k = %d, k * (1 << (k-1)) = %s""".formatted(num.toString(), k, temp.toString()));

        // S([A...])
        result = result.add(partialSum(tail));

        // ... that is S(1[A...])
        // System.out.println("""
        //     S(%s): result = %s""".formatted(num.toString(), result.toString()));
        return result;
    }

}
