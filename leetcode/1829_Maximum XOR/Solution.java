class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int[] ret = new int[nums.length];

        int xorVal = 0;
        int maxBitValue = (1 << maximumBit) - 1;
        for(int i = 0; i < nums.length; i++) {
            xorVal = xorVal ^ nums[i];
            int notXor = ~xorVal;
            ret[i] = notXor & maxBitValue;
        }

        return ret;
    }
}
