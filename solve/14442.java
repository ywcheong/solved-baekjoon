import java.io.*;
import java.util.*;

// @SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int xsize;
    private static int ysize;
    private static int[][] board;

    private final static int[][] deltas = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        xsize = Integer.parseInt(tokenizer.nextToken());
        ysize = Integer.parseInt(tokenizer.nextToken());
        int breach = Integer.parseInt(tokenizer.nextToken());

        board = new int[xsize][ysize];
        for (int x = 0; x < xsize; x++) {
            String boardRow = reader.readLine();
            for (int y = 0; y < ysize; y++) {
                board[x][y] = boardRow.charAt(y) - '0';
            }
        }

        int result = solve(board, breach);
        writer.write(String.valueOf(result));
        writer.newLine();
        writer.flush();
    }

    public static int solve(int[][] board, int breach) {
        if (xsize == 1 && ysize == 1)
            return 1;

        int[] startState = new int[]{0, 0, breach};
        Queue<int[]> toVisit = new ArrayDeque<>();
        int[][][] visited = new int[xsize][ysize][breach+1];

        toVisit.add(startState);
        visited[0][0][breach] = 1;

        while (!toVisit.isEmpty()) {
            int[] vstate = toVisit.poll();
            int vx = vstate[0], vy = vstate[1], vb = vstate[2];

            for(int[] delta : deltas) {
                int wx = vx + delta[0], wy = vy + delta[1];

                int wb;
                if (0 <= wx && wx < xsize && 0 <= wy && wy < ysize) {
                    if (board[wx][wy] == 1 && vb > 0)
                        wb = vb - 1;
                    else if (board[wx][wy] == 0)
                        wb = vb;
                    else
                        continue;
                } else {
                    continue;
                }

                if (visited[wx][wy][wb] == 0) {
                    toVisit.add(new int[]{wx, wy, wb});
                    visited[wx][wy][wb] = visited[vx][vy][vb] + 1;

                    if (wx == xsize - 1 && wy == ysize - 1) {
                        return visited[wx][wy][wb];
                    }
                }
            }
        }
        
        return -1;
    }
}
