package equalsidesofanarray;

public class Kata {
    public static int findEvenIndex(int[] arr) {
        int left= 0, right = 0;

        for (int i = 1; i < arr.length; i++) {
            right += arr[i];
        }
        if (left == right) return 0;

        for (int i = 1; i < arr.length; i++) {
            right -= arr[i];
            left += arr[i-1];
            if (left == right) return i;
        }

        return -1;
    }
}