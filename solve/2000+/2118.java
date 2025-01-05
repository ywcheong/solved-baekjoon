import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int size;

    // distance.get(i) == (i ~ i+1)
    private static List<Integer> distance = new ArrayList<>();

    // partialSumDistance.get(i) = (0 ~ i)
    private static List<Integer> partialSumDistance = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        size = Integer.parseInt(reader.readLine());

        partialSumDistance.add(0);
        for (int i = 0; i < size; i++) {
            int nextDistance = Integer.parseInt(reader.readLine());
            distance.add(nextDistance);
            partialSumDistance.add(partialSumDistance.get(partialSumDistance.size() - 1) + nextDistance);
        }

        int result = maxDiameter();
        writer.write(String.valueOf(result));

        writer.newLine();
        writer.flush();
    }

    public static int maxDiameter() {
        int endPoint = 0;
        int result = 0;

        for (int startPoint = 0; startPoint < size; startPoint++) {
            endPoint = findFarthest(startPoint, endPoint);
            result = Math.max(result, getDiameter(startPoint, endPoint));
        }

        return result;
    }

    public static int findFarthest(int startPoint, int endPoint) {
        while (getDiameter(startPoint, endPoint) <= getDiameter(startPoint, getNextPoint(endPoint))) {
            endPoint = getNextPoint(endPoint);
        }

        return endPoint;
    }

    public static int getNextPoint(int point) {
        if (point == size - 1)
            return 0;
        return point + 1;
    }

    public static int getDiameter(int startPoint, int endPoint) {
        if (startPoint > endPoint) {
            return getDiameter(endPoint, startPoint);
        }

        int totalLength = partialSumDistance.get(partialSumDistance.size() - 1);
        int innerLength = partialSumDistance.get(endPoint) - partialSumDistance.get(startPoint);
        int outerLength = totalLength - innerLength;

        return Math.min(innerLength, outerLength);
    }

}
