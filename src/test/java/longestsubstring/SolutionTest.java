package longestsubstring;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void test() {
        Solution sol = new Solution();
        sol.lengthOfLongestSubstring("aabaab!bb");
        sol.lengthOfLongestSubstring("aabba");
        sol.lengthOfLongestSubstring("pwwkew");
        sol.lengthOfLongestSubstring("aab");

    }
}
