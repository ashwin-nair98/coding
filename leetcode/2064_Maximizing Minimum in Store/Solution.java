class Solution {
    public boolean canDistribute(int k, int n, int[] qty) {
        int i = 0;
        while(i < qty.length && n > 0) {
            if(qty[i] >= k) {
                if(qty[i] % k != 0){
                    n--;
                }
                n -= qty[i]/k;
            } else {
                n--;
            }
            i++;
        }
        if(i == qty.length && n >= 0) {
            return true;
        }
        return false;
    } 
    public int minimizedMaximum(int n, int[] quantities) {
        int kMax = Integer.MIN_VALUE;

        for(int i: quantities) {
            kMax = Math.max(kMax, i);
        }

        int l = 1, r = kMax;
        while (l <= r) {
            int k = l + (r - l)/2;
            if(this.canDistribute(k, n, quantities)) {
                r = k - 1;
            } else {
                l = k + 1;
            }
        }
        return l;
    }
}