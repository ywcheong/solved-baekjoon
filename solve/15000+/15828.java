import java.io.*;
import java.util.ArrayDeque;

// @SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int bufferSize = Integer.parseInt(reader.readLine());

        ArrayDeque<Integer> router = new ArrayDeque<>();

        while (true) {
            int input = Integer.parseInt(reader.readLine());

            // 입력값이 -1인 경우 라우터 작동 중단
            if (input == -1) {
                break;
            }

            if (input == 0) {
                router.removeFirst();
            } else if (router.size() < bufferSize) {
                router.addLast(input);
            }
        }

        // 라우터 미처리 내용물 출력
        if (router.size() == 0) {
            writer.write("empty");
        } else {
            writer.write(String.join(" ",
                    router.stream().map(String::valueOf).toArray(String[]::new)));
        }

        writer.write('\n');
        writer.flush();
    }
}
