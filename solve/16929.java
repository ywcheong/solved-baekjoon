import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int NOT_VISITED = -1;
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int xsize, ysize;
        xsize = Integer.parseInt(tokenizer.nextToken());
        ysize = Integer.parseInt(tokenizer.nextToken());

        char[][] board = new char[xsize][ysize];
        for (int x = 0; x < xsize; x++) {
            board[x] = reader.readLine().toCharArray();
        }

        if (isCycleExists(board)) {
            writer.write("Yes");
        } else {
            writer.write("No");
        }

        writer.write('\n');
        writer.flush();
    }

    public static boolean isCycleExists(char[][] board) throws IOException {
        int xsize = board.length;
        int ysize = board[0].length;

        ArrayDeque<Pos> toVisit = new ArrayDeque<>();
        int[][] visited = new int[xsize][ysize];
        for (int x = 0; x < xsize; x++) {
            for (int y = 0; y < ysize; y++) {
                visited[x][y] = NOT_VISITED;
            }
        }

        for (int x = 0; x < xsize; x++) {
            for (int y = 0; y < ysize; y++) {
                if (visited[x][y] == NOT_VISITED) {
                    visited[x][y] = 1;
                    toVisit.addLast(new Pos(x, y));
                    if (checkCycleWithDFS(board, toVisit, visited))
                        return true;
                }
            }
        }

        return false;
    }

    public static boolean checkCycleWithDFS(char[][] board, ArrayDeque<Pos> toVisit, int[][] visited) throws IOException {
        int xsize = board.length;
        int ysize = board[0].length;
        Pos[][] parent = new Pos[xsize][ysize];

        while (!toVisit.isEmpty()) {
            Pos v = toVisit.removeFirst();
            for (Pos w : nextPos(board, v, xsize, ysize)) {
                if (visited[w.x][w.y] == NOT_VISITED) {
                    parent[w.x][w.y] = v;
                    toVisit.add(w);
                    visited[w.x][w.y] = visited[v.x][v.y] + 1;
                } else if (parent[v.x][v.y] != null && !parent[v.x][v.y].equals(w)){
//                    for (int[] row : visited) {
//                        writer.write(Arrays.toString(row));
//                    }
                    return true;
                }
            }
        }

        return false;
    }

    public static ArrayList<Pos> nextPos(char[][] board, Pos v, int xsize, int ysize) {
        int x = v.x;
        int y = v.y;
        ArrayList<Pos> result = new ArrayList<>();

        for (int[] delta : new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}) {
            int nx = x + delta[0];
            int ny = y + delta[1];
            if (0 <= nx && nx < xsize && 0 <= ny && ny < ysize && board[x][y] == board[nx][ny])
                result.add(new Pos(nx, ny));
        }

        return result;
    }

    public static final class Pos {
        public int x;
        public int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public boolean equals(Pos other){
            return this.x == other.x && this.y == other.y;
        }
    }
}