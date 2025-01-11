import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final int PINF = 987_654_321;

    public static class Word {
        private static final int aIndex = (int) 'a';

        private String word;
        private int[] countMap = new int[26];

        public Word(String word) {
            this.word = word;
            for (char c : word.toCharArray()) {
                countMap[c - aIndex]++;
            }
        }

        public int getCost(String otherWord, int startIndex) {
            if (startIndex + word.length() > otherWord.length())
                return -1;

            int[] otherCountMap = Arrays.copyOf(countMap, countMap.length);
            int cost = 0;
            for (int i = 0; i < word.length(); i++) {
                char thisChar = word.charAt(i);
                char otherChar = otherWord.charAt(startIndex + i);

                if (thisChar != otherChar)
                    cost++;
                if (--otherCountMap[otherChar - aIndex] < 0)
                    return -1;
            }
            return cost;
        }

        public int getLength() {
            return word.length();
        }
    }

    public static void main(String[] args) throws IOException {
        String sentence = reader.readLine();
        int size = Integer.parseInt(reader.readLine());

        List<Word> words = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            words.add(new Word(reader.readLine()));
        }

        int result = solve(sentence, words);
        writer.write(String.valueOf(result));
        writer.newLine();
        writer.flush();
    }

    public static int solve(String sentence, List<Word> words) throws IOException {
        int[] memo = new int[sentence.length() + 1];
        Arrays.fill(memo, PINF);
        memo[memo.length - 1] = 0;
        
        for (int i = sentence.length() - 1; i >= 0; i--) {
            for (Word word : words) {
                int cost = word.getCost(sentence, i);
                if (cost >= 0) {
                    memo[i] = Math.min(memo[i], cost + memo[i + word.getLength()]);
                }
            }
        }

        if (memo[0] == PINF)
            return -1;
        return memo[0];
    }
}
