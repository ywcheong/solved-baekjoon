import java.io.*;

/*
(String board) |-> (String Result)

String board;

StringBuilder result
int pos <-> 움직이며 추적

AAAA, 안 되면 BB, 안 되면 -1
For trial, (String board, int pos) |-> (MovementType result)
 */

// @SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static enum MovementType {
        A(4, "AAAA"),
        B(2, "BB"),
        JUMP(1, "."),
        CANNOT_FILL(-1, "");

        private final int movement;
        private final String text;

        MovementType(int movement, String text) {
            this.movement = movement;
            this.text = text;
        }

        public int getMovement() {
            return this.movement;
        }

        public String getText() {
            return this.text;
        }
    }

    public static MovementType getMovementType(String board, int pos) {
        if (pos + 4 <= board.length() && board.substring(pos, pos + 4).equals("XXXX")) {
            return MovementType.A;
        }

        if (pos + 2 <= board.length() && board.substring(pos, pos + 2).equals("XX")) {
            return MovementType.B;
        }

        if (pos + 1 <= board.length() && board.substring(pos, pos + 1).equals(".")) {
            return MovementType.JUMP;
        }

        return MovementType.CANNOT_FILL;
    }

    public static String solve(String board) {
        StringBuilder result = new StringBuilder();
        int pos = 0;

        while (pos < board.length()) {
            MovementType type = getMovementType(board, pos);
            if (type == MovementType.CANNOT_FILL) {
                return "-1";
            }

            pos += type.getMovement();
            result.append(type.getText());
        }

        return result.toString();
    }

    public static void main(String[] args) throws IOException {
        String board = reader.readLine();
        String answer = solve(board);
        writer.write(answer);
        writer.write('\n');
        writer.flush();
    }
}
