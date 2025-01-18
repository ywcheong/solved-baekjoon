import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        double monkeyHeight = Double.parseDouble(tokenizer.nextToken());
        double dogHeight = Double.parseDouble(tokenizer.nextToken());

        writer.write(String.valueOf((int) solve(dogHeight - monkeyHeight)));
        writer.newLine();
        writer.flush();
    }

    public static double solve(double delta) {
        int peak = (int) Math.pow(delta, 0.5);

        if (delta == 0) {
            return 0;
        }

        if (peak * peak == delta) {
            return 2 * peak - 1;
        }

        if (peak * peak < delta && delta <= peak * peak + peak) {
            return 2 * peak;
        }

        return (2 * peak + 1);
    }
}
