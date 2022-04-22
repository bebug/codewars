package jumpgame2;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void test() {
        Solution sol = new Solution();
        Assert.assertEquals(2, sol.jump(new int[] {2,3,0,1,4}));
        Assert.assertEquals(0, sol.jump(new int[] {0}));
        Assert.assertEquals(2, sol.jump(new int[] {2,3,1,1,4}));
    }
}
