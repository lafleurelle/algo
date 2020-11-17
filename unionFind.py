class DisjointSet:
    def __init__(self):
        self.leader = {}
        self.group = {}

    def add(self, a, b):
        leader_a = self.leader.get(a)
        leader_b = self.leader.get(b)
        if leader_a is not None:
            if leader_b is not None:
                if leader_a == leader_b: return
                group_a = self.group[leader_a]
                group_b = self.group[leader_b]
                if len(group_a) < len(group_b):
                    a, leader_a, group_a, b, leader_b, group_b = b, leader_b, group_b, a, leader_a, group_a
                group_a |= group_b
                del self.group[leader_b]
                for k in group_b:
                    self.leader[k] = leader_a
            else:
                self.group[leader_a].add(b)
                self.leader[b] = leader_a
        else:
            if leader_b is not None:
                self.group[leader_b].add(a)
                self.leader[a] = leader_b
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])
