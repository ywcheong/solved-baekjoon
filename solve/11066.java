import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int testcaseSize = Integer.parseInt(reader.readLine());
        for (int testcaseId = 0; testcaseId < testcaseSize; testcaseId++) {
            singleTestcase();
        }

        writer.flush();
    }

    public static void singleTestcase() throws IOException {
        int size = Integer.parseInt(reader.readLine());
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        
        int[] nums = new int[size];
        for (int i = 0; i < size; i++) {
            nums[i] = Integer.parseInt(tokenizer.nextToken());
        }

        int result = solve(nums);
        writer.write(String.valueOf(result));
        writer.newLine();
    }

    public static int solve(int[] nums) {
        int size = nums.length;
        int[] partialSum = getPartialSum(nums);
        int[][] cost = new int[size][size];
        
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                cost[i][j] = 1_987_654_321;
            }
        }

        for (int end = 0; end < size; end++) {
            cost[end][end] = 0;
            for (int start = end - 1; start >= 0; start--) {
                for (int mid = start; mid < end; mid++) {
                    cost[start][end] = Math.min(cost[start][end], cost[start][mid] + cost[mid+1][end] + getMergeCost(partialSum, start, end));
                }
            }
        }

        return cost[0][size - 1];
    }

    public static int[] getPartialSum(int[] nums) {
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        for (int i = 1; i < sum.length; i++) {
            sum[i] = sum[i - 1] + nums[i];
        }
        return sum;
    }

    public static int getMergeCost(int[] partialSum, int start, int end){
        // nums[start, start+1, ..., end]
        if (start == 0)
            return partialSum[end];
        return partialSum[end] - partialSum[start - 1];
    }
}
