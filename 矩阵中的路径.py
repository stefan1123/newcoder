"""
题目描述
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵
    中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经
    过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这
    样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第
    一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
代码情况：accepted
"""

class Solution:  
     def hasPath(self, matrix, rows, cols, path):
        # 参数校验
        if len(matrix) == 0 or len(matrix) != rows * cols or len(path) == 0:
            return False
        visited = [False] * len(matrix)
        pathlength = 0
        for i in range(rows):
            for j in range(cols):
                # 以矩阵中每一个位置作为起点进行搜索
                if self.haspath(matrix, rows, cols, path, j, i, visited, pathlength):
                    return True
        return False
    
     # 判断矩阵位置（x,y）的字符能否加入已找到的路径中
     def haspath(self, matrix, rows, cols, path, x, y, visited, pathlength):

        if pathlength == len(path):
            return True
        curhaspath = False
        # 参数校验：1、位置坐标不超过行列数 2、当前位置字符等于路径中对应位置的字符 3、当前位置未存在于当前已找到的路径中
        if 0 <= x < cols and 0 <= y < rows \
                and matrix[y * cols + x] == path[pathlength] \
                and not visited[y * cols + x]:
            # === note1: 先变为符合要求的 ===
            visited[y * cols + x] = True
            pathlength += 1
            # 分别向左，向右，向上，向下移动一个格子，任一方向能够继续往下走均可
            curhaspath = self.haspath(matrix, rows, cols, path, x - 1, y, visited, pathlength) \
                         or self.haspath(matrix, rows, cols, path, x, y - 1,visited, pathlength) \
                         or self.haspath(matrix, rows, cols, path, x + 1, y, visited, pathlength) \
                         or self.haspath(matrix, rows, cols, path, x, y + 1, visited,pathlength)
            # === note2: 根据对该位置的上下左右进行查询判断，确定该位置是否真的符合要求 ===
            # 如果在path中还有待查询的字母，但是该矩阵位置的左右上下位置均不符合要求，则需要把该位置更改为不符合要求。
            if not curhaspath:
                pathlength -= 1
                visited[y * cols + x] = False
        # 如果找到路径中的字母就返回True，否则返回False
        return curhaspath
        
if __name__ == "__main__":
    s = Solution()
    # matrix
    # a b c c
    # s f c s
    # a d e e
    m = ['a','b','c','c','s','f','c','s','a','d','e','e']
    p = 'bcced'
    res = s.hasPath(m,3,4,p)
