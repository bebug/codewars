package regularexpressionmatching;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void test() {
        Solution solution = new Solution();

        Assert.assertEquals(true, solution.isMatch("aaa", "a*a"));
        Assert.assertEquals(false, solution.isMatch("ab", ".*c"));
        Assert.assertEquals(false, solution.isMatch("mississippi", "mis*is*p*."));
        Assert.assertEquals(true, solution.isMatch("ab", ".*"));
    }
}
