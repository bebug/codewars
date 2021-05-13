public class Accumul {

    public static String accum(String s) {
        char[] strArray = s.toLowerCase().toCharArray();
        StringBuilder sb = new StringBuilder();
        for (int i=0; i < s.length(); i++) {
            for(int j=0; j <= i; j++) {
                if (j == 0) {
                    sb.append((char)(strArray[i]-32));
                }
                else {
                    sb.append(strArray[i]);
                }
            }
            if (i != s.length() - 1) {
                sb.append("-");
            }
        }
        return sb.toString();
    }
}