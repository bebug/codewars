package jumpgame2;

class Solution {
    public int jump(int[] nums) {
        int r = 0;
        int l = 0;
        int steps = 0;
        while(r < nums.length - 1) {
            int oldR = r;
            for(int i = l; i<=oldR; i++) {
                r = Math.max(r, Math.min(i + nums[i], nums.length));
            }
            l = oldR + 1;
            steps++;
        }
        return steps;
    }
}
