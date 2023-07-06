class Solution {
    
    public static int counter = 0;
    
    public static int minimizeConcatenatedLength(String[] words) {
        return minimizer(words, 0, "");
    }
    
    public static int minimizer(String[] words, int i, String current) {
        if(i >= words.length) {
            return current.length();
        }
        
        String order = concater(current, words[i]);
        String orderRev = concater(words[i], current);
        System.out.println("Counter: " + counter++);
        
        return Math.min(minimizer(words, i+1, order), minimizer(words, i+1, orderRev));
    }
    
    public static String concater(String left, String right) {
        StringBuilder sb = new StringBuilder();
        sb.append(left);
        if(left.length() > 0 && right.length() > 0 && left.charAt(left.length() - 1) == right.charAt(0)) {
            sb.deleteCharAt(sb.length() - 1);
        }
        sb.append(right);
        return sb.toString();
    }
    
}
