class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        maxes = []
        distances = []
        ones = []
        zeros = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ones.append((i, j))
                elif grid[i][j] == 0:
                    zeros.append((i, j))

        isone = True
        if len(ones) == 0:
            isone = False

        iszero = True
        if len(zeros) == 0:
            iszero = False

        if iszero and isone:
            for i in zeros:
                dist = []
                for j in ones:
                    dist.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
                distances.append(dist)

            for i in distances:
                first = i[0]
                check = True
                num = None
                for j in i:
                    if j != first:
                        check = False
                        break
                    else:
                        num = j
                if check:
                    maxes.append(num)

            maxdist = 0
            for i in maxes:
                if i > maxdist:
                    maxdist = i

            return maxdist
        else:
            return -1


test = Solution()
grid = [[0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 1]]
print(test.maxDistance(grid))
