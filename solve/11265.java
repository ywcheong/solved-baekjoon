import java.io.*;
import java.util.StringTokenizer;

class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    static class Query {
        public int start;
        public int end;
        public int timeLimit;

        public Query(int start, int end, int timeLimit) {
            this.start = start;
            this.end = end;
            this.timeLimit = timeLimit;
        }
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int size = Integer.parseInt(tokenizer.nextToken());
        int querySize = Integer.parseInt(tokenizer.nextToken());

        int[][] weight = new int[size][size];
        for (int i = 0; i < size; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 0; j < size; j++) {
                weight[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        Query[] queryList = new Query[querySize];
        for (int i = 0; i < querySize; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            int start = Integer.parseInt(tokenizer.nextToken()) - 1;
            int end = Integer.parseInt(tokenizer.nextToken()) - 1;
            int timeLimit = Integer.parseInt(tokenizer.nextToken());

            queryList[i] = new Query(start, end, timeLimit);
        }

        long[][] distance = computeShortestDistance(weight);
        for (Query q : queryList) {
            if (distance[q.start][q.end] > q.timeLimit) {
                writer.write("Stay here");
            } else {
                writer.write("Enjoy other party");
            }
            writer.newLine();
        }

        writer.flush();
    }

    private static long[][] computeShortestDistance(int[][] weight) {
        int size = weight.length;
        long[][] distance = new long[size][size];

        for (int start = 0; start < size; start++) {
            for (int end = 0; end < size; end++) {
                distance[start][end] = weight[start][end];
            }
        }

        for (int mid = 0; mid < size; mid++) {
            for (int start = 0; start < size; start++) {
                for (int end = 0; end < size; end++) {
                    distance[start][end] = Math.min(
                            distance[start][end],
                            ((long) distance[start][mid]) + distance[mid][end]
                    );
                }
            }
        }

        return distance;
    }
}