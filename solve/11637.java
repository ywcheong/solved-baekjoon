import java.io.*;
import java.util.*;

@SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        // Write input handling here
        int testcaseSize = Integer.parseInt(reader.readLine());

        // Write your logic here
        for (int testCaseId = 0; testCaseId < testcaseSize; testCaseId++) {
            int candidateSize = Integer.parseInt(reader.readLine());

            int[] voteCount = new int[candidateSize];
            int totalCount = 0;
            ArrayList<Integer> winners = new ArrayList<>();

            for (int candidateId = 0; candidateId < candidateSize; candidateId++) {
                int thisVote = Integer.parseInt(reader.readLine());

                voteCount[candidateId] += thisVote;
                totalCount += thisVote;

                if (candidateId == 0) {
                    winners.add(0);
                    continue;
                }

                if (thisVote > voteCount[winners.get(0)]) {
                    winners.clear();
                    winners.add(candidateId);
                } else if (thisVote == voteCount[winners.get(0)]) {
                    winners.add(candidateId);
                }
            }

            if (winners.size() > 1) {
                writer.write("no winner");
            } else {
                int winner = winners.get(0);
                if (2 * voteCount[winner] > totalCount) {
                    writer.write("majority winner " + String.valueOf(winner + 1));
                } else {
                    writer.write("minority winner " + String.valueOf(winner + 1));
                }
            }

            writer.newLine();
        }

        // Write output handling here
        writer.newLine();
        writer.flush();
    }
}
