# Understanding LCA: Line 33-35 Explained

## The Line in Question

```python
return left_result if left_result else right_result
```

This handles **Case 2**: Found something in only ONE subtree (not both).

---

## Visual Examples

### Example 1: Both nodes in LEFT subtree

```
        3
       / \
      5   1
     / \
    6   2
       / \
      7   4
```

**Finding LCA(6, 7):**

Let's trace the recursion at node 3:

1. **Search left subtree (node 5):**
   - This will recursively find that LCA(6,7) = 5
   - Returns: `left_result = 5`

2. **Search right subtree (node 1):**
   - Neither 6 nor 7 are here
   - Returns: `right_result = None`

3. **At node 3:**
   - `left_result = 5` (found the LCA in left subtree)
   - `right_result = None` (nothing in right subtree)
   - `left_result and right_result` → False (not both)
   - Execute: `return left_result if left_result else right_result`
   - Returns: `5` ✅

**Why return 5?** Because the LCA was already found in the left subtree!

---

### Example 2: Both nodes in RIGHT subtree

```
        3
       / \
      5   1
         / \
        0   8
```

**Finding LCA(0, 8):**

At node 3:

1. **Search left subtree (node 5):**
   - Neither 0 nor 8 are here
   - Returns: `left_result = None`

2. **Search right subtree (node 1):**
   - This will find that LCA(0,8) = 1
   - Returns: `right_result = 1`

3. **At node 3:**
   - `left_result = None`
   - `right_result = 1`
   - `left_result and right_result` → False
   - Execute: `return left_result if left_result else right_result`
   - Since `left_result` is None (falsy), return `right_result`
   - Returns: `1` ✅

---

### Example 3: One node is ancestor of the other

```
        3
       / \
      5   1
     / \
    6   2
       / \
      7   4
```

**Finding LCA(5, 4):**

At node 3:

1. **Base case at node 5:**
   - `root == p` (node 5 is one of our targets!)
   - Returns immediately: `5`
   - This becomes `left_result = 5`

2. **Search right subtree (node 1):**
   - Node 4 is not in this subtree
   - Returns: `right_result = None`

3. **At node 3:**
   - `left_result = 5` (found p itself)
   - `right_result = None`
   - Execute: `return left_result if left_result else right_result`
   - Returns: `5` ✅

**Key insight:** When we find `p` or `q`, we return it immediately. If the other node is in that subtree, it will be found deeper in the recursion. If not, we still correctly return the ancestor.

---

## Step-by-Step Trace: LCA(6, 7)

```
        3
       / \
      5   1
     / \   / \
    6   2 0   8
       / \
      7   4
```

### Call Stack Visualization:

```
lca(3, 6, 7)
├─ lca(5, 6, 7)  [left subtree of 3]
│  ├─ lca(6, 6, 7)  [left subtree of 5]
│  │  └─ return 6  [base case: found node 6]
│  │
│  ├─ lca(2, 6, 7)  [right subtree of 5]
│  │  ├─ lca(7, 6, 7)  [left subtree of 2]
│  │  │  └─ return 7  [base case: found node 7]
│  │  │
│  │  ├─ lca(4, 6, 7)  [right subtree of 2]
│  │  │  └─ return None  [neither 6 nor 7]
│  │  │
│  │  └─ At node 2:
│  │     left_result = 7, right_result = None
│  │     return 7  [Case 2: only left has result]
│  │
│  └─ At node 5:
│     left_result = 6, right_result = 7
│     return 5  [Case 1: BOTH subtrees have results → LCA!]
│
├─ lca(1, 6, 7)  [right subtree of 3]
│  └─ return None  [neither 6 nor 7]
│
└─ At node 3:
   left_result = 5, right_result = None
   return 5  [Case 2: only left has result]

FINAL ANSWER: 5 ✅
```

---

## The Three Cases Summarized

At any node, after searching both subtrees:

| left_result | right_result | What it means | Return |
|-------------|--------------|---------------|--------|
| Not None | Not None | **Case 1:** Found p in one subtree, q in other → **Current node is LCA** | `root` |
| Not None | None | **Case 2:** Both nodes in left subtree (or left is ancestor) | `left_result` |
| None | Not None | **Case 2:** Both nodes in right subtree (or right is ancestor) | `right_result` |
| None | None | Neither p nor q in this subtree | `None` |

---

## Why This Works

The beauty of this algorithm is that it **propagates information upward**:

1. When we find `p` or `q`, we return it
2. When we find **both** in different subtrees, we know current node is LCA
3. When we find something in **only one** subtree, we pass it up (it might be the LCA found deeper, or just one of the nodes)

The line `return left_result if left_result else right_result` simply says:
> "I found something in one subtree but not the other. Pass up whatever I found."

---

## Practice Question

Given this tree, trace LCA(7, 4):

```
        3
       / \
      5   1
     / \
    6   2
       / \
      7   4
```

<details>
<summary>Click to see answer</summary>

**Answer: 2**

At node 2:
- `left_result = 7` (found in left subtree)
- `right_result = 4` (found in right subtree)
- Both are not None → return node 2 (Case 1)

At node 5:
- `left_result = None` (6 is not 7 or 4)
- `right_result = 2` (LCA found in right subtree)
- Return 2 (Case 2)

At node 3:
- `left_result = 2`
- `right_result = None`
- Return 2 (Case 2)

</details>
