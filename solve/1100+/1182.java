import java.io.*;
import java.util.*;

// @SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int size = Integer.parseInt(tokenizer.nextToken());
        int goal = Integer.parseInt(tokenizer.nextToken());

        int[] nums = new int[size];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(tokenizer.nextToken());
        }

        int result = solve(nums, goal);
        writer.write(String.valueOf(result));
        writer.newLine();
        writer.flush();
    }

    private static int solve(int[] nums, int goal) {
        int result = solve(nums, goal, 0, 0);
        // 빈 수열 1개를 제외
        if (goal == 0)
            return result - 1;
        return result;
    }

    private static int solve(int[] nums, int goal, int currentIndex, int currentSum) {
        if (currentIndex == nums.length) {
            return currentSum == goal ? 1 : 0;
        }

        int caseIfInclude = solve(nums, goal, currentIndex + 1, currentSum + nums[currentIndex]);
        int caseIfExclude = solve(nums, goal, currentIndex + 1, currentSum);

        return caseIfInclude + caseIfExclude;
    }
}
