package reverseonlyletters;

import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {
    @Test
    public void test() {
        Solution solution = new Solution();

        Assert.assertEquals("7_28]", solution.reverseOnlyLetters("7_28]"));
        Assert.assertEquals("Qedo1ct-eeLg=ntse-T!", solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"));
        Assert.assertEquals("j-Ih-gfE-dCba", solution.reverseOnlyLetters("a-bC-dEf-ghIj"));
        Assert.assertEquals("abc", solution.reverseOnlyLetters("cba"));

    }
}
