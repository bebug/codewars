package zigzag;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void test() {
        Solution sol = new Solution();
        Assert.assertEquals("PAYPALGINSIHRI", sol.convert("PAYPALISHIRING", 10));
        Assert.assertEquals("PAHNAPLSIIGYIR", sol.convert("PAYPALISHIRING", 3));

        Assert.assertEquals("ABCDEF", sol.convert("ABCDFE", 5));
        Assert.assertEquals("AB", sol.convert("AB", 1));
        Assert.assertEquals("A", sol.convert("A", 1));
    }
}
