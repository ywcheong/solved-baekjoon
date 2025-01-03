import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static final int NOT_VISITED = -1;

    public static void main(String[] args) throws IOException {
        // Write input handling here
        int testcaseSize = Integer.parseInt(reader.readLine());

        for (int testcaseId = 0; testcaseId < testcaseSize; testcaseId++) {
            int givenSize = Integer.parseInt(reader.readLine());
            int[] givenNext = new int[givenSize];
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
            for (int i = 0; i < givenSize; i++) {
                // 1-index를 0-index로 변환함에 주의
                givenNext[i] = Integer.parseInt(tokenizer.nextToken()) - 1;
            }

            writer.write(String.valueOf(computeSolo(givenNext)));
            writer.newLine();
        }

        // Write output handling here
        writer.flush();
    }

    public static int computeSolo(int[] next) {
        int size = next.length;
        int[] visited = new int[size];
        int[] depth = new int[size];

        for (int student = 0; student < size; student++) {
            visited[student] = NOT_VISITED;
        }

        // Counter 방법: 아직 방문하지 않은 학생(노드)이 있으면, 그 학생부터 시작해 아직 팀에 포함되지 않은 학생 수를 계산
        int result = 0;
        for (int student = 0; student < size; student++) {
            if (visited[student] == NOT_VISITED) {
                result += computeSoloWhenStartingFrom(next, visited, depth, student);
            }
        }

        return result;
    }

    public static int computeSoloWhenStartingFrom(int[] next, int[] visited, int[] depth, int student) {
        int currentStudent = student;
        visited[currentStudent] = currentStudent;
        depth[currentStudent] = 1;

        while (true) {
            int nextStudent = next[currentStudent];

            if (visited[nextStudent] != NOT_VISITED) {
                if (visited[nextStudent] == visited[currentStudent]) {
                    // 이번 StartingFrom에서 이미 탐색되었던 적 있는 노드
                    return depth[nextStudent] - 1;
                } else {
                    // 다른 StartingFrom에서 이미 탐색되었던 적 있는 노드
                    return depth[currentStudent];
                }
            }

            // 한 번도 방문한 적 없는 노드
            visited[nextStudent] = visited[currentStudent];
            depth[nextStudent] = depth[currentStudent] + 1;
            currentStudent = nextStudent;
        }
    }
}
