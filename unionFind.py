# refered from https://at274.hatenablog.com/entry/2018/02/02/173000
# [0, 1, 1]の時、1は根で、2の親が1であることを示す。
# つまりそのnodeが根ならpar[i] == i

class UnionFind:
    def __init__(self, n):
        # 木の親要素を管理するリスト
        self.par = [i for i in range(n+1)] 
        # ?
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            # 再起により走査していく過程で親を書き換えている、根でなかった場合に最後に見つかった根がそれぞれの親に入る
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        #　低い方を高い方に繋げる
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x

    def isSame(self, x, y):
        return self.find(x) == self.find(y)
