class Solution {
    public int minChanges(String s) {
        char curr = s.charAt(0);
        boolean odd = true;
        int count = 0;

        for(int i = 1; i < s.length(); i++) {
            if(curr != s.charAt(i)) {
                if(odd) {
                    count++;
                } else {
                    curr = s.charAt(i);
                }
            }
            odd = !odd;
        }

        return count;
    }
}