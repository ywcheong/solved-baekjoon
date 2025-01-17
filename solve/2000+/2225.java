import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int k = Integer.parseInt(tokenizer.nextToken());

        writer.write(String.valueOf(solve(n, k)));
        writer.newLine();
        writer.flush();
    }

    public static int solve(int n, int k) {
        int[][] memo = new int[n+1][k+1];
        for (int a = 0; a <= n; a++) {
            memo[a][1] = 1;
        }

        for (int b = 2; b <= k; b++) {
            memo[0][b] = memo[0][b-1];
            for (int a = 1; a <= n; a++) {
                memo[a][b] = (memo[a][b-1] + memo[a-1][b]) % 1_000_000_000;
                // P(n, k) = P(n, k-1) + ... + P(0, k-1)
                //         = P(n, k-1) + P(n-1, k)
            }
        }

        return memo[n][k];
    }
}
