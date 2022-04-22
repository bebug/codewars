package mediantwosortedarrays;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {

    @Test
    public void test() {
        Solution sol = new Solution();
        Assert.assertEquals(2.5d, sol.findMedianSortedArrays(new int[] {1,2}, new int[] {3,4}), 0.001d);
        Assert.assertEquals(2d, sol.findMedianSortedArrays(new int[] {1,3}, new int[] {2}), 0.001d);
    }
}
