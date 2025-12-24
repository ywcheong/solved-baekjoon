import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

// @SuppressWarnings("unused")
public class Main {
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

    private static List<String> stringToToken(String givenString) {
        if (givenString.charAt(0) == ':')
            givenString = '0' + givenString;
        if (givenString.charAt(givenString.length() - 1) == ':')
            givenString = givenString + '0';

        String[] tokens = givenString.split(":", -1);
        int numSkipZero = 9 - tokens.length;
        List<String> result = new ArrayList<>();

        // 1. ::1 -> token=3, numSkipZero=6 -> 0x6::1 -> 0!
        // 2. 1::1 -> token=3, numSkipZero=6 -> 1:0x6:1
        // 3. 1:: -> token=3, numSkipZero=6 -> 1:0x6:0

        for (String token : tokens) {
            if ("".equals(token)) {
                while (numSkipZero > 0) {
                    result.add("0000");
                    numSkipZero -= 1;
                }
            } else {
                result.add(token);
            }
        }

        return result;
    }

    private static String formatToken(String givenToken) {
        while (givenToken.length() < 4) {
            givenToken = "0" + givenToken;
        }
        return givenToken;
    }

    private static String tokenToString(List<String> givenTokens) {
        var result = new StringBuilder();
        for (int i = 0; i < 8; i++) {
            result.append(givenTokens.get(i));
            if (i != 7) {
                result.append(":");
            }
        }
        return result.toString();
    }

    public static void main(String[] args) throws IOException {
        String givenIpString = reader.readLine();
        List<String> givenIpTokens = stringToToken(givenIpString);

        List<String> formattedIpTokens = givenIpTokens.stream()
                .map(Main::formatToken)
                .collect(Collectors.toList());

        String formattedIpString = tokenToString(formattedIpTokens);
        writer.write(formattedIpString);
        writer.write('\n');
        writer.flush();
    }
}
