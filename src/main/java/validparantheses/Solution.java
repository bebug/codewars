package validparantheses;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

public class Solution {
    Set<Character> openChars = new HashSet<Character>(Arrays.asList('(', '[', '{'));

    public boolean isValid(String s) {
        LinkedList list = new LinkedList();

        for(char c : s.toCharArray()) {
            if (openChars.contains(c)) {
                list.addLast(c);
            } else {
                if (list.isEmpty()) return false;

                switch(c) {
                    case ')': {
                        if ('(' != (char)list.pollLast())
                            return false;
                        break;
                    }
                    case '}': {
                        if ('{' != (char)list.pollLast())
                            return false;
                        break;
                    }
                    case ']': {
                        if ('[' != (char)list.pollLast())
                            return false;
                        break;
                    }
                }
            }
        }

        return list.isEmpty();

    }
}
