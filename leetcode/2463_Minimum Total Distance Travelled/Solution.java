class Solution {
    Map<Key, Long> cache = new HashMap<>();

    class Key {
        int robot;
        int factory;
        int slots;

        Key(int r, int f, int s) {
            this.robot = r;
            this.factory = f;
            this.slots = s;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Key other = (Key) o;
            return robot == other.robot && factory == other.factory && slots == other.slots;
        }

        @Override
        public int hashCode() {
            return Objects.hash(robot, factory, slots);
        }
    }

    public long minDist(List<Integer> robot, int[][] factory, int r_ind, int f_ind, int slots) {
        Key curr = new Key(r_ind, f_ind, slots);
        if (r_ind < 0) return 0;
        if (f_ind < 0) return Long.MAX_VALUE;

        if (this.cache.containsKey(curr)) {
            return this.cache.get(curr);
        }

        // Option 1: Exclude this factory and move to the previous factory, resetting slots if within bounds
        long exclude = this.minDist(robot, factory, r_ind, f_ind - 1, f_ind > 0 ? factory[f_ind - 1][1] : 0);

        // Option 2: Include this factory and decrease slot count
        long include = Long.MAX_VALUE;
        if (slots > 0) {
            include = this.minDist(robot, factory, r_ind - 1, f_ind, slots - 1);
            long includeDist = Math.abs(robot.get(r_ind).longValue() - factory[f_ind][0]);
            if (include != Long.MAX_VALUE) {
                include += includeDist;
            }
        }

        long dist = Math.min(exclude, include);
        this.cache.put(curr, dist);
        return dist;
    }

    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory, Comparator.comparingInt(a -> a[0]));

        return this.minDist(robot, factory, robot.size() - 1, factory.length - 1, factory[factory.length - 1][1]);
    }
}
