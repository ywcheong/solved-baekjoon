import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static final int[][][] blockListForType = {
            {{0}, {0, 0, 0, 0}}, // Type 1
            {{0, 0}}, // Type 2
            {{0, 0, 1}, {0, -1}}, // Type 3
            {{0, -1, -1}, {0, 1}}, // Type 4
            {{0, 0, 0}, {0, -1}, {0, 1}, {0, -1, 0}}, // Type 5
            {{0, 0, 0}, {0, -2}, {0, 1, 1}, {0, 0}}, // Type 6
            {{0, 0, 0}, {0, 0}, {0, 0, -1}, {0, 2}}, // Type 7
    };

    public static void main(String[] args) throws IOException {
        InputSpace inputSpace = readInput();
        OutputSpace outputSpace = solve(inputSpace);
        writeOutput(outputSpace);
    }

    public static OutputSpace solve(InputSpace input) {
        int counter = 0;
        for (int column = 0; column < input.heights.length; column++) {
            counter += countApplicableBlocks(input.heights, blockListForType[input.blockType], column);
        }
        return new OutputSpace(counter);
    }

    public static int countApplicableBlocks(int[] heights, int[][] blockList, int column) {
        int counter = 0;
        for (int[] block : blockList) {
            if (isApplicableBlock(heights, block, column))
                counter++;
        }
        return counter;
    }

    public static boolean isApplicableBlock(int[] heights, int[] block, int column) {
//        System.out.print("For block " + Arrays.toString(block) + " in column " + String.valueOf(column) + " it does ");
        if (column + block.length > heights.length) {
//            System.out.println(false);
            return false;
        }

        for (int i = 0; i < block.length; i++) {
            if (heights[column] + block[i] != heights[column + i]) {
//                System.out.println(false);
                return false;
            }
        }

//        System.out.println(true);
        return true;
    }

    public static InputSpace readInput() throws IOException {
        // Write input logic in here
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int size = Integer.parseInt(tokenizer.nextToken());
        int blockType = Integer.parseInt(tokenizer.nextToken()) - 1;

        int[] heights = new int[size];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < size; i++) {
            heights[i] = Integer.parseInt(tokenizer.nextToken());
        }

        return new InputSpace(blockType, heights);
    }

    public static boolean writeOutput(OutputSpace output) {
        try {
            // Write output logic in here
            writer.write(String.valueOf(output.counter));
            writer.newLine();
            writer.flush();
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    /* INPUT LOGIC BLOCK */
    public static class InputSpace {
        // Write input structure in here
        int blockType;
        int[] heights;

        public InputSpace(int blockType, int[] heights) {
            this.blockType = blockType;
            this.heights = heights;
        }
    }

    /* OUTPUT LOGIC BLOCK */
    public static class OutputSpace {
        // Write output structure in here
        int counter;

        public OutputSpace(int counter) {
            this.counter = counter;
        }
    }

}