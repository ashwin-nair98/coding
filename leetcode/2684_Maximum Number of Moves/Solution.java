class Solution {
    int[][] DIR = {
        {-1, 1},
        {0, 1},
        {1, 1}
    };
    class Cell {
        int row;
        int col;
        int hashCode;
        Cell(int row, int col) {
            this.row = row;
            this.col = col;
            this.hashCode = Objects.hash(row, col);
        }
        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            Cell that = (Cell) o;
            return this.row == that.row && this.col == that.col;
        }

        @Override
        public int hashCode() {
            return this.hashCode;
        }
    }

    Map<Cell, Integer> cache = new HashMap<>();
    public int maxMoves(int[][] grid) {
        int maxMoves = 0;
        for (int row = 0; row < grid.length; row++) {
            maxMoves = Math.max(maxMoves, this.maxMoves(grid, row, 0));
            if (maxMoves == grid[row].length - 1) {
                return maxMoves;
            }
        }
        return maxMoves;
    }
    public int maxMoves(int[][] grid, int row, int col) {
        int maxMoves = 0;
        Cell current = new Cell(row, col);
        if(this.cache.containsKey(current)){
            return this.cache.get(current);
        }
        for(int [] dir: this.DIR) {
            if( this.isValidAccess(grid, row + dir[0], col + dir[1]) &&
                grid[row + dir[0]][col + dir[1]] > grid[row][col]) {
                maxMoves = Math.max(maxMoves, 1 + this.maxMoves(grid, row + dir[0], col + dir[1]));
                
                if (maxMoves == grid[row].length - col - 1 ) {
                    this.cache.put(current, maxMoves);
                    return maxMoves;
                }
            }
        }
        this.cache.put(current, maxMoves);
        return maxMoves;
    }

    public boolean isValidAccess(int [][] grid, int row, int col) {
        return row >= 0 && row < grid.length && col >= 0 && col < grid[0].length;
    }
}