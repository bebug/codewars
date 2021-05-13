public class GrassHopper {
    public static char getGrade(int s1, int s2, int s3) {
        switch (((s1 + s2 + s3) /30)) {
            case 10:
            case 9:
                return 'A';
            case 8:
                return 'B';
            case 7:
                return 'C';
            case 6:
                return 'D';
            case 5:
            default:
                return 'F';
        }
    }
}
