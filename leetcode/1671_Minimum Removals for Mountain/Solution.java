class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int[] lis = new int[nums.length];
        int[] lds = new int[nums.length];
        int remove = Integer.MAX_VALUE;

        for(int i = 0; i < nums.length; i ++) {
            lis[i] = 1;
            lds[i] = 1;
        }

        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    lis[i] = Math.max(lis[i], 1 + lis[j]);
                }
            }
        }

        for(int i = nums.length - 1; i >= 0; i--) {
            for(int j = nums.length - 1; j > i; j--){
                if (nums[j] < nums[i]) {
                    lds[i] = Math.max(lds[i], 1 + lds[j]);
                }
            }
        }

        for(int i = 0; i < nums.length; i++) {
            if(lis[i] == 1 || lds[i] == 1) {
                continue;
            } else {
                remove = Math.min(remove, nums.length - lis[i] - lds[i] + 1);
            }
        }
        return remove;
    }
}