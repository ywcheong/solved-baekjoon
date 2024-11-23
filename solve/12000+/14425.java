import java.io.*;
import java.util.*;

public class Main {

    private static class Reader {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        public int readInt() throws IOException {
            String line = this.reader.readLine();
            return Integer.parseInt(line);
        }

        public String readString() throws IOException {
            return this.reader.readLine();
        }

        public int[] readIntList(String delim) throws IOException {
            StringTokenizer tokenizer = new StringTokenizer(this.reader.readLine(), delim);
            int[] intList = new int[tokenizer.countTokens()];

            for (int i = 0; tokenizer.hasMoreTokens(); i++) {
                intList[i] = Integer.parseInt(tokenizer.nextToken());
            }

            return intList;
        }

        public int[] readIntList() throws IOException {
            return this.readIntList(" ");
        }

        public String[] readStringList() throws IOException {
            StringTokenizer tokenizer = new StringTokenizer(this.reader.readLine(), " ");
            String[] stringList = new String[tokenizer.countTokens()];

            for (int i = 0; tokenizer.hasMoreTokens(); i++) {
                stringList[i] = tokenizer.nextToken();
            }

            return stringList;
        }
    }

    private static class Writer {
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        private <T> void writeln(T line) throws IOException {
            writer.write(line.toString());
            writer.write('\n');
        }

        private void print() throws IOException {
            writer.flush();
        }
    }

    public static void main(String[] args) throws IOException {
        /* reader input */
        Reader reader = new Reader();
        Writer writer = new Writer();

        /* Write your code here */
        int[] sizeList = reader.readIntList();
        int setSize = sizeList[0];
        int targetSize = sizeList[1];

        HashSet<String> stringSet = new HashSet<>();
        for (int i = 0; i < setSize; i++) {
            stringSet.add(reader.readString());
        }

        int counter = 0;
        for (int i = 0; i < targetSize; i++) {
            if(stringSet.contains(reader.readString())){
                counter++;
            }
        }

        writer.writeln(counter);

        /* stream flush */
        writer.print();
    }
}
