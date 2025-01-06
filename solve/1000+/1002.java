import java.io.*;
import java.util.*;

/*
(x - L)2 + y2 = a2
x2 + y2 = b2

-2xL + L2 = a2 - b2
L2 - a2 + b2 = 2Lx

x = (L2 - a2 + b2) / 2L

4L2 * b2 - (L2 - a2 + b2)2 > 0


if y2 > 0 -> 2
if y2 == 0 -> 1
if y2 < 0 -> 0
 */

public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        // Write input handling here
        int testcaseSize = Integer.parseInt(reader.readLine());

        // Write your logic here    
        for (int testcaseId = 0; testcaseId < testcaseSize; testcaseId++) {
            int x1, y1, r1, x2, y2, r2;
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            x1 = Integer.parseInt(tokenizer.nextToken());
            y1 = Integer.parseInt(tokenizer.nextToken());
            r1 = Integer.parseInt(tokenizer.nextToken());
            x2 = Integer.parseInt(tokenizer.nextToken());
            y2 = Integer.parseInt(tokenizer.nextToken());
            r2 = Integer.parseInt(tokenizer.nextToken());

            double deltax = (x1 - x2);
            double deltay = (y1 - y2);

            double l2 = deltax * deltax + deltay * deltay;
            double a2 = r1 * r1;
            double b2 = r2 * r2;

            writer.write(String.valueOf(solve(l2, a2, b2)));
            writer.newLine();
        }

        writer.flush();
    }

    public static int solve(double l2, double a2, double b2) {
        if (l2 == 0) {
            if (a2 == b2)
                return -1;
            else
                return 0;
        }

        // 4L2 * b2 - (L2 - a2 + b2)2 > 0
        double temp = (l2 - a2 + b2);
        double cond = 4 * l2 * b2 - temp * temp;
        
        if (cond > 0)
            return 2;
        if (cond == 0)
            return 1;
        if (cond < 0)
            return 0;

        throw new AssertionError("unreachable");
    }
}
