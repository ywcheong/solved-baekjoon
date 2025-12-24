import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static final int PINF = 987_654_321;

    private enum Decide {
        DO_TOGGLE,
        DO_NOT_TOGGLE,
        IMPOSSIBLE
    }

    public static void main(String[] args) throws IOException {
        int[] goal = readInput();
        int answer = solve(goal);
        writeOutput(answer);
    }

    public static int[] readInput() throws IOException {
        // Write input handling here
        int size = Integer.parseInt(reader.readLine());
        int[] goal = new int[size];

        String originalLine = reader.readLine();
        for (int i = 0; i < size; i++) {
            goal[i] = originalLine.charAt(i) == '1' ? 1 : 0;
        }

        String goalLine = reader.readLine();
        for (int i = 0; i < size; i++) {
            goal[i] ^= (goalLine.charAt(i) == '1' ? 1 : 0);
        }

        return goal;
    }

    public static int solve(int[] goal) {
        int result = PINF;

        for (boolean zeroIndexToggle : new boolean[]{true, false}) {
            int[] board = Arrays.copyOf(goal, goal.length);
            int currentToggleCount = 0;

            if (zeroIndexToggle) {
                toggle(board, 0);
                currentToggleCount++;
            }

            for (int i = 1; i < board.length; i++) {
                Decide decision = decideIfToggle(board, i);

                if (decision == Decide.DO_TOGGLE) {
                    toggle(board, i);
                    currentToggleCount++;
                }

                if (decision == Decide.IMPOSSIBLE) {
                    currentToggleCount = PINF;
                    break;
                }
            }

            result = Math.min(result, currentToggleCount);
        }        
        
        // return answer : process if no answer
        if (result == PINF) {
            return -1;
        }

        return result;
    }

    public static Decide decideIfToggle(int[] board, int pos) {
        if (pos == board.length - 1) {
            if (board[pos - 1] == 0 && board[pos] == 0)
                return Decide.DO_NOT_TOGGLE;
            if (board[pos - 1] == 1 && board[pos] == 1)
                return Decide.DO_TOGGLE;
            return Decide.IMPOSSIBLE;
        }

        if (board[pos - 1] == 0)
            return Decide.DO_NOT_TOGGLE;
        return Decide.DO_TOGGLE;
    }

    public static void toggle(int[] board, int pos) {
        board[pos] ^= 1;

        if (pos != 0) {
            board[pos - 1] ^= 1;
        }
        
        if (pos != board.length - 1) {
            board[pos + 1] ^= 1;
        }
    }

    public static void writeOutput(int answer) throws IOException {
        writer.write(String.valueOf(answer));
        writer.newLine();
        writer.flush();
    }

}
