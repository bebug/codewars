package dividetwointegers;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void test() {
        Solution sol = new Solution();
        Assert.assertEquals(3, sol.divide(10, 3));
        Assert.assertEquals(715827882, sol.divide(2147483647, 3));
    }
}
