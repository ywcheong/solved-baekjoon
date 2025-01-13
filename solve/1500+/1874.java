import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int size = Integer.parseInt(reader.readLine());
        int[] nums = new int[size];
        for (int i = 0; i < size; i++) {
            nums[i] = Integer.parseInt(reader.readLine());
        }

        writer.write(solve(nums));
        writer.flush();
    }

    public static String solve(int[] nums) {
        int next_push = 1;
        StringBuilder builder = new StringBuilder();

        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int x : nums) {
            while (next_push <= x) {
                stack.addLast(next_push++);
                builder.append("+\n");
            }
            // already-pushed
            if (stack.isEmpty() || stack.getLast() != x) {
                return "NO\n";
            }
            stack.removeLast();
            builder.append("-\n");
        }

        return builder.toString();
    }
}
