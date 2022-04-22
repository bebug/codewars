package dividetwointegers;

class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == 1) return Integer.MIN_VALUE;
        if (dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;

        boolean negative = dividend < 0 ^ divisor < 0;
        dividend = dividend < 0 ? dividend : -dividend;
        divisor = divisor < 0 ? divisor : -divisor;

        int result = 0;
        while(dividend <= divisor) {
            int j = -1;
            int div = divisor;
            while(dividend - div <= div) {
                div = div << 1;
                j = j << 1;
            }
            dividend -= div;
            result += j;
        }

        return negative ? result : result == Integer.MIN_VALUE ? Integer.MAX_VALUE : -result;
    }
}