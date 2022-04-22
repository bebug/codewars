package longestsubstring;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = 0;
        int start = 0;
        Map<Integer, Integer> positions = new HashMap<>();
        for(int i=0; i < s.length(); i++) {
            int currentChar = s.codePointAt(i);
            int lastappearance = positions.getOrDefault(currentChar, -1);

            if (lastappearance != -1) {
                length = Math.max(length, i - Math.max(start, lastappearance + 1) + 1);
                start = Math.max(start, lastappearance) + 1;

            }
            else {
                length = Math.max(length, i - start + 1);
            }
            positions.put(currentChar, i);
        }
        return length;
    }

}