package validparantheses;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {
    @Test
    public void test() {
        Solution solution = new Solution();

        Assert.assertEquals(Boolean.FALSE, solution.isValid("([)]"));

    }
}
