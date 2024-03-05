class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        Map<Integer, Set<Integer>> serverToTime = new HashMap<>();
        
        for(int i = 1; i <= n; i++) {
            serverToTime.put(i, new HashSet<>());
        }
        
        for(int i = 0; i< logs.length; i++) {
            serverToTime.get(logs[i][0]).add(logs[i][1]);
        }
        
        int[] ret = new int[queries.length];
        
        for(int i = 0; i < queries.length; i++) {
            int left = queries[i] - x;
            int right = queries[i];
            int count = 0;
            
            for(Set<Integer> timings: serverToTime.values()) {
                boolean found = false;
                for(Integer time: timings) {
                    if(left <= time && right >= time) {
                        found = true;
                        break;
                    }
                }
                if(!found) {
                    count++;
                }
            }
            ret[i] = count;
        }
        return ret;
    }
}
