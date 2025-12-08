class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # Union by size (larger set becomes parent)
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_size(self, x):
        return self.size[self.find(x)]

    def components(self):
        """Return a list of lists: each component as a list of items."""
        comps = {}
        for x in self.parent:
            r = self.find(x)
            comps.setdefault(r, []).append(x)
        return list(comps.values())

