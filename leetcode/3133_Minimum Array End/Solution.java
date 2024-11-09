class Solution {
    public long minEnd(int n, int x) {
        long val = (long) x;
        long num = (long) n;
        long invert = ~val;
        int rightShiftCount = 0;
        num--;
        while(num > 0) {
            long newBit = num & 1;
            num = num >> 1;
            long one = 1;
            while((invert & one) != one) {
                invert = invert >> 1;
                rightShiftCount++;
            }
            newBit = newBit << rightShiftCount;
            val = val | newBit;
            invert = invert >> 1;
            rightShiftCount++;
        }
        return val;
    }
}