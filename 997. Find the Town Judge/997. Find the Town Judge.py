# first idea: scan x-axis and y-axis separately
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        fin = [[0 for j in range(N)] for i in range(N)]
        tmp = []
        for i in trust:
            fin[i[0] - 1][i[1] - 1] = 1

        for i in range(N):
            count = 0
            for j in range(N):
                count += fin[j][i]
            if count == N - 1:
                tmp.append(i)

        tmp1 = []
        for i in tmp:
            count = 0
            for j in range(N):
                count += fin[i][j]
            if count == 0:
                tmp1.append(i)

        if len(tmp1) == 1:
            return tmp1[0] + 1
        else:
            return -1


# Update
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        tmp = [0 for i in range(N)]
        for (a, b) in trust:
            tmp[a - 1] -= 1
            tmp[b - 1] += 1

        tmp1 = []
        for i in range(N):
            if tmp[i] == N - 1:
                return i + 1
        return -1