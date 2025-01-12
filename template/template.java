import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

    }

    public static InputSpace readInput() throws IOException {
        // Write input logic in here
        return new InputSpace();
    }

    public static boolean writeOutput(OutputSpace output) {
        try {
            // Write output logic in here
            writer.newLine();
            writer.flush();
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    public static class InputSpace {
        // Write input structure in here
    }

    public static class OutputSpace {
        // Write output structure in here
    }

}