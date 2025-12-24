import java.io.*;
import java.util.*;

// @SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int size = Integer.parseInt(reader.readLine());
        
        int[] distances = new int[size - 1];
        StringTokenizer distanceTokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < size - 1; i++) {
            distances[i] = Integer.parseInt(distanceTokenizer.nextToken());
        }

        int[] prices = new int[size];
        StringTokenizer priceTokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < size; i++) {
            prices[i] = Integer.parseInt(priceTokenizer.nextToken());
        }

        long result = solve(distances, prices);
        writer.write(String.valueOf(result));
        writer.newLine();
        writer.flush();
    }

    public static long solve(int[] distances, int[] prices) {
        // i번 주유소와 i+1번 주유소를 연결하는 i번 도로에서 쓰는 기름의 출처는: 
        // 0번, ..., i번 주유소 중 가장 싼 기름임!

        long result = 0;
        long minPrice = 987_654_321_987_654_321L;
        for (int road = 0; road < distances.length; road++) {
            minPrice = Math.min(minPrice, prices[road]);
            result += distances[road] * minPrice;
        }

        return result;
    }

}
