from typing import List


class UnionFind:
    """
    Disjoint Set Union (Union-Find) data structure with
    union by size and path compression.

    Time complexity (amortized):
    - find(x)  -> O(α(n))   where α is the inverse Ackermann function,
                             which grows so slowly that it is treated
                             as a constant in practice (≈ O(1)).
    - union(x, y) -> O(α(n)), because it performs a constant number of finds.
    - get_size(x) -> O(α(n)), due to the internal find.

    Space complexity:
    - O(n) additional space to store the parent and size arrays
      (each of length n).
    """
    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x: int, y: int) -> None:
        rep_x, rep_y = self.find(x), self.find(y)

        if rep_x != rep_y:
            # if rep_x belongs to a larger community , add rep_y comuunity to it
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
    
    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        # path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]


class MergingCommunities:
    def __init__(self, n: int):
        self.uf = UnionFind(n)

    def connect(self, x: int, y: int) -> None:
        self.uf.union(x, y)

    def get_community_size(self, x: int) -> int:
        return self.uf.get_size(x)
    
    def get_parent(self) -> List[int]:
        return self.uf.parent
    
    def get_size(self) -> List[int]:
        return self.uf.size


def main() -> None:
    """
    Simple test case for the Union-Find / MergingCommunities implementation.

    We create 5 people (0..4), merge some of them into communities and
    then print the sizes of each person's community.
    """
    n = 5
    mc = MergingCommunities(n)

    # Initially each person is in their own community of size 1
    print("Initial community sizes:")
    for i in range(n):
        print(f"Person {i}: size {mc.get_community_size(i)}")

    # Merge some communities
    mc.connect(0, 1)  # community {0,1}
    mc.connect(2, 3)  # community {2,3}
    mc.connect(1, 2)  # now {0,1,2,3}

    print("\nAfter merging (0-1), (2-3), (1-2):")
    for i in range(n):
        print(f"Person {i}: size {mc.get_community_size(i)}")

    # Expected:
    # persons 0,1,2,3 -> size 4
    # person 4 -> size 1

    print("parent", mc.get_parent())
    print("size", mc.get_size())


if __name__ == "__main__":
    main()