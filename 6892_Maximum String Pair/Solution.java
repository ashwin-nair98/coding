class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        Set<String> reversals = new HashSet<>();
        int counter = 0;
        for(String st: words) {
            String rev = new StringBuilder().append(st).reverse().toString();
            if(reversals.contains(st)) {
                counter++;
            }
            reversals.add(rev);
        }
        return counter;
    }
}
