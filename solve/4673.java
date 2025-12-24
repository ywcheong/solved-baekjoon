import java.io.*;
import java.util.*;

// @SuppressWarnings("unused")
public class Main {
    // private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        boolean[] isConstructable = new boolean[10001];
        for (int start = 1; start <= 10000; start++) {
            int x = getD(start);
            while(x <= 10000 && !isConstructable[x]) {
                isConstructable[x] = true;
                x = getD(x);
            }
        }

        for (int x = 1; x <= 10000; x++) {
            if (!isConstructable[x]){
                writer.write(String.valueOf(x));
                writer.newLine();
            }
        }

        writer.flush();
    }

    public static int getD(int num) {
        int result = num;
        while (num > 0) {
            result += num % 10;
            num /= 10;
        }
        return result;
    }

}
