package longestpalindrome;

class Solution {
    public String longestPalindrome(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            String strAt = expand(s, s.substring(i,i+1), i - 1, i + 1);
            String strPrev = expand(s, "", i - 1, i);
            if (strAt.length() > result.length()) {
                result = strAt;
            } else if (strPrev.length() > result.length()) {
                result = strPrev;
            }
        }
        return result;
    }

    public String expand(String in, String substring, int left, int right) {
        if (left >= 0 && right < in.length())
        {
            char c = in.charAt(left);
            if (in.charAt(right) == c) {
                return expand(in, c + substring + c, left - 1, right + 1);
            }
        }
        return substring;
    }
}
