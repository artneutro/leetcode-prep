# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Variables initialization
        done = {}
        queue = []
        islands = 0
        # Iterate over the matrix items
        index_row = 0
        index_col = 0
        while index_row < len(grid) :
            while index_col < len(grid[0]) :
                # If the element is 1 then enqueue it 
                if grid[index_row][index_col] == '1' and (index_row,index_col) not in done :
                    queue.append((index_row,index_col))
                    # Enqueue all the related elements if not done
                    while len(queue) > 0 :
                        item_check = queue.pop(0)
                        # i-1, j
                        if (item_check[0]-1) in range(0, len(grid)) \
                        and (item_check[1]) in range(0, len(grid[0])): 
                            if (item_check[0]-1, item_check[1]) not in done \
                            and (item_check[0]-1, item_check[1]) not in queue :
                                if grid[item_check[0]-1][item_check[1]] == '1' :
                                    queue.append((item_check[0]-1,item_check[1]))
                        # i, j-1
                        if (item_check[0]) in range(0, len(grid)) \
                        and (item_check[1]-1) in range(0, len(grid[0])): 
                            if (item_check[0], item_check[1]-1) not in done \
                            and (item_check[0], item_check[1]-1) not in queue :
                                if grid[item_check[0]][item_check[1]-1] == '1' :
                                    queue.append((item_check[0],item_check[1]-1))
                        # i+1, j
                        if (item_check[0]+1) in range(0, len(grid)) \
                        and (item_check[1]) in range(0, len(grid[0])): 
                            if (item_check[0]+1, item_check[1]) not in done \
                            and (item_check[0]+1, item_check[1]) not in queue :
                                if grid[item_check[0]+1][item_check[1]] == '1' :
                                    queue.append((item_check[0]+1,item_check[1]))
                        # i, j+1
                        if (item_check[0]) in range(0, len(grid)) \
                        and (item_check[1]+1) in range(0, len(grid[0])): 
                            if (item_check[0], item_check[1]+1) not in done \
                            and (item_check[0], item_check[1]+1) not in queue :
                                if grid[item_check[0]][item_check[1]+1] == '1' :
                                    queue.append((item_check[0],item_check[1]+1))
                        if item_check not in done :
                            # Changed from list to dict to avoid TLE
                            done[item_check] = 1
                    # Once the queue is zero then the current island is finished
                    islands += 1
                index_col += 1
            index_row += 1
            index_col = 0
        return islands

