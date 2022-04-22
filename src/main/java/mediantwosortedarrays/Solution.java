package mediantwosortedarrays;

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int target = ((nums1.length + nums2.length)) / 2;
        int pt1 = 0;
        int pt2 = 0;
        double lastValue = 0d;
        double lastLastValue = 0d;
        while(target >= 0) {
            if (pt1 >= nums1.length) {
                lastLastValue = lastValue;
                lastValue = nums2[pt2];
                pt2++;
            } else if (pt2 >= nums2.length) {
                lastLastValue = lastValue;
                lastValue = nums1[pt1];
                pt1++;
            } else if (nums1[pt1] > nums2[pt2]) {
                lastLastValue = lastValue;
                lastValue = nums2[pt2];
                pt2++;
            } else {
                lastLastValue = lastValue;
                lastValue = nums1[pt1];
                pt1++;
            }
            target--;
        }
        return (nums1.length + nums2.length)%2 == 0 ? (lastValue + lastLastValue) / 2 : lastValue;
    }
}
