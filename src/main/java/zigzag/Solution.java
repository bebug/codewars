package zigzag;

class Solution {
    public String convert(String s, int numRows) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < numRows; i++) {
            for(int j = 0; j+i < s.length() + numRows * 2 -1; j += Math.max(1,2*numRows-2)) {
                int ipj = i+j;
                if (j > 0 && i%numRows != 0 && i%numRows != numRows-1) {
                    int ipj2i = ipj-(2*i);
                    if (ipj2i < s.length())
                    sb.append(s.charAt(ipj2i));
                }
                if (ipj < s.length())
                sb.append(s.charAt(ipj));
            }
        }
        return sb.toString();
    }
}