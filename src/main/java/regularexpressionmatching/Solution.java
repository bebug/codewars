package regularexpressionmatching;

import java.util.HashMap;
import java.util.Map;

class Solution {

    public boolean isMatch(String s, String p) {
        return isMatch(s, p, new HashMap<>());
    }

    public boolean isMatch(String s, String p, Map<String, Map<String, Boolean>> map) {
        boolean wildcard = false;

        if (map.containsKey(s) && map.get(s).containsKey(p))
            return map.get(s).get(p);

        int posP = 0;
        int posS = 0;

        while(posP < p.length()) {
            char character = p.charAt(posP);
            posP++;
            if (posP < p.length() && '*' == p.charAt(posP)) {
                wildcard = true;
                posP++;
            } else {
                wildcard = false;
            }

            if (wildcard) {
                while(posS < s.length() && (character == s.charAt(posS) || character == '.')) {
                    if (posP < p.length() && isMatch(s.substring(posS), p.substring(posP), map)) {
                        break;
                    }
                    posS++;
                }
            } else if (posS < s.length() && character == s.charAt(posS) || character == '.') {
                posS++;
            } else {
                return false;
            }
        }

        boolean result = posS == s.length() && posP == p.length();

        if (!map.containsKey(s)) {
            map.put(s, new HashMap<>());
        }

        if (!map.get(s).containsKey(p)) {
            map.get(s).put(p, result);
        }

        return result;
    }
}