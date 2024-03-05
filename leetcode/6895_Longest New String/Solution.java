class Solution {
    public int longestString(int x, int y, int z) {
        
        String[] adders = new String[3];
        adders[0] = "AA";
        adders[1] = "BB";
        adders[2] = "AB";
        
        StringBuilder sb = new StringBuilder();
        
        if(x >= y) {
            // Number of AA is more than or equal to BB, then start with AB appends and alternate AA, BB
            while (z > 0){
                sb.append(adders[2]);
                z--;
            }
            boolean noForward = false;
            while((x > 0 || y > 0) && (!noForward)) {
                if(y >= 1 && x >= 1) {
                    sb.append(adders[0]);
                    sb.append(adders[1]);
                    x --;
                    y --;
                } else if (y >= 1) {
                    sb.append(adders[0]);
                    noForward = true;
                } else {
                    noForward = true;
                }
            }
        } else {
            // Number of BB is more than or equal to AA, then start with BB, alternate till BB and append AB (end with BB important)
            boolean noForward = false;
            while((x > 0 || y > 0) && (!noForward)) {
                if(y >= 2 && x >=1) {
                    sb.append(adders[1]);
                    sb.append(adders[0]);
                    sb.append(adders[1]);
                    y -= 2;
                    x --;
                } else {
                    noForward = true;
                }
            }
            while (z > 0) {
                sb.append(adders[2]);
                z--;
            }
        }
        
        return sb.length();
        
    }
}
