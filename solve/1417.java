import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        putOutput(solve(getInput()));
    }

    public static List<Integer> getInput() throws IOException {
        int size = Integer.parseInt(reader.readLine());
        List<Integer> vote = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            vote.add(Integer.parseInt(reader.readLine()));
        }
        return vote;
    }

    public static int solve(List<Integer> vote) {
        int count = 0;
        while (true) {
            int winningCandidate = getWinningCandidate(vote);
            if (winningCandidate == 0) {
                return count;
            }

            vote.set(winningCandidate, vote.get(winningCandidate) - 1);
            vote.set(0, vote.get(0) + 1);
            count++;
        }
    }

    public static int getWinningCandidate(List<Integer> vote) {
        int winningCandidate = 0;
        for (int candidate = 0; candidate < vote.size(); candidate++) {
            if (vote.get(candidate) >= vote.get(winningCandidate)) {
                winningCandidate = candidate;
            }
        }
        return winningCandidate;
    }

    public static void putOutput(int result) throws IOException {
        writer.write(String.valueOf(result));
        writer.newLine();
        writer.flush();
    }
}