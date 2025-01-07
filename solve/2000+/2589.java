import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int xsize;
    private static int ysize;

    private static char[][] board;

    private static final int NOT_VISITED = 0;
    private static int landId = 1;

    private static int treasureDistance = -1;

    public static void main(String[] args) throws IOException {
        // Write input handling here
        StringTokenizer sizeTokenizer = new StringTokenizer(reader.readLine());
        xsize = Integer.parseInt(sizeTokenizer.nextToken());
        ysize = Integer.parseInt(sizeTokenizer.nextToken());

        board = new char[xsize][ysize];

        for (int x = 0; x < xsize; x++) {
            board[x] = reader.readLine().toCharArray();
            assert (board[x].length == ysize);
        }

        // Write your logic here
        for (int x = 0; x < xsize; x++) {
            for (int y = 0; y < ysize; y++) {
                if (board[x][y] == 'L') {
                    traverseFromPos(Pos.build(x, y), landId++);
                }
            }
        }

        // Write output handling here
        writer.write(String.valueOf(treasureDistance));
        writer.newLine();
        writer.flush();
    }

    private static void traverseFromPos(Pos startPos, int landId) {
        Pos farthest = findFarthestFrom(startPos, landId);
        treasureDistance = Math.max(treasureDistance, farthest.level);
    }

    private static Pos findFarthestFrom(Pos startPos, int landId) {
        ArrayDeque<Pos> toVisit = new ArrayDeque<>();
        int[][] level = new int[xsize][ysize];

        startPos.level = 0;
        toVisit.addLast(startPos);

        level[startPos.x][startPos.y] = 1;
        Pos lastPos = startPos;

        while (!toVisit.isEmpty()) {
            Pos v = toVisit.removeFirst();

            for (Pos w : v.getNextPosList()) {
                if (level[w.x][w.y] == 0) {
                    toVisit.addLast(w);
                    level[w.x][w.y] = level[v.x][v.y] + 1;

                    lastPos = w;
                }
            }
        }

        lastPos.level = level[lastPos.x][lastPos.y] - 1;
        return lastPos;
    }

    private static class Pos {
        public int x;
        public int y;
        public int level;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        public static Pos build(int x, int y) {
            if (0 <= x && x < xsize && 0 <= y && y < ysize && board[x][y] == 'L') {
                return new Pos(x, y);
            }
            return null;
        }

        public List<Pos> getNextPosList() {
            List<Pos> result = new ArrayList<>();
            for (int[] delta : new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
                int nx = this.x + delta[0];
                int ny = this.y + delta[1];

                Pos nextPos = Pos.build(nx, ny);
                if (nextPos != null) {
                    result.add(nextPos);
                }
            }
            return result;
        }

        public boolean equals(Pos other) {
            return this.x == other.x && this.y == other.y;
        }

        public int hashCode() {
            return this.x * ysize + this.y;
        }
    }
}
