import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int xsize;
    private static int ysize;
    private static char[][] board;

    private static ArrayDeque<Pos> toVisit = new ArrayDeque<>();
    private static int[][] visited;

    private static final int NOT_VISITED = -1;
    private static final char EMPTY = '0';
    private static final char BLOCK = '1';
    private static final char AGENT = '2';
    private static final char GOAL1 = '3';
    private static final char GOAL2 = '4';
    private static final char GOAL3 = '5';

    public static void main(String[] args) throws IOException {
        // Write input handling here
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        xsize = Integer.parseInt(tokenizer.nextToken());
        ysize = Integer.parseInt(tokenizer.nextToken());
        board = new char[xsize][ysize];

        for (int x = 0; x < xsize; x++) {
            board[x] = reader.readLine().toCharArray();
        }

        int result = computeMinDistance();
        if (result == -1) {
            writer.write("NIE");
            writer.newLine();
        } else {
            writer.write("TAK");
            writer.newLine();
            writer.write(String.valueOf(result));
            writer.newLine();
        }

        writer.flush();
    }

    public static int computeMinDistance() {
        Pos startPos = computeStartPos();

        initMarkAsNotVisited();
        toVisit.addLast(startPos);
        visited[startPos.x][startPos.y] = 0;

        while (!toVisit.isEmpty()) {
            Pos v = toVisit.removeFirst();

            for (Pos w : v.nextPos()) {
                if (isGoal(w)) {
                    return visited[v.x][v.y] + 1;
                }

                if (visited[w.x][w.y] == NOT_VISITED) {
                    toVisit.add(w);
                    visited[w.x][w.y] = visited[v.x][v.y] + 1;
                }
            }
        }

        return -1;
    }

    public static boolean isGoal(Pos pos) {
        char value = board[pos.x][pos.y];
        return value == GOAL1 || value == GOAL2 || value == GOAL3;
    }

    public static Pos computeStartPos() {
        for (int x = 0; x < xsize; x++) {
            for (int y = 0; y < ysize; y++) {
                if (board[x][y] == AGENT) {
                    return new Pos(x, y);
                }
            }
        }

        return null;
    }

    public static void initMarkAsNotVisited() {
        visited = new int[xsize][ysize];
        for (int x = 0; x < xsize; x++) {
            Arrays.fill(visited[x], NOT_VISITED);
        }
    }

    public static class Pos {
        public int x;
        public int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public ArrayList<Pos> nextPos() {
            ArrayList<Pos> result = new ArrayList<>();

            for (int[] delta : new int[][] { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } }) {
                int nx = x + delta[0];
                int ny = y + delta[1];

                if (0 <= nx && nx < xsize && 0 <= ny && ny < ysize && board[nx][ny] != BLOCK) {
                    result.add(new Pos(nx, ny));
                }
            }

            return result;
        }

        public boolean equals(Pos other) {
            return this.x == other.x && this.y == other.y;
        }
    }
}
