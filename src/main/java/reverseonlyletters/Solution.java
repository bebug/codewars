package reverseonlyletters;

public class Solution {
    public String reverseOnlyLetters(String s) {
        byte[] bytes = s.getBytes();
        int start = 0;
        int end = bytes.length - 1;

        while(start < end) {
            while(!validCharacter(bytes[start]) && start < end) {
                start++;
            }
            while(!validCharacter(bytes[end]) && start < end) {
                end--;
            }
            if (start < end) {
                bytes[start] = (byte)((int)(bytes[start]) ^ (int)(bytes[end]));
                bytes[end] = (byte)((int)bytes[start] ^ (int)bytes[end]);
                bytes[start] = (byte)((int)bytes[start] ^ (int)bytes[end]);
            }
            start++;
            end--;

        }
        return new String(bytes);
    }

    boolean validCharacter(int chr) {
        return chr >= (int)'A' && chr <= (int)'Z' ||
                chr >= (int)'a' && chr <= (int)'z';
    }
}
