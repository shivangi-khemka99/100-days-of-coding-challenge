# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def distributeCoins(self, root: Optional[TreeNode]) -> int:
#         self.res = 0
#         def dfs(cur):
#             if not cur:
#                 return [0,0] #[tree size, number of coins]
#             lsize, lcoins = dfs(cur.left)
#             rsize, rcoins = dfs(cur.right)
#             size = 1 + lsize + rsize
#             coins = cur.val + lcoins + rcoins
#             self.res += abs(size-coins)
#             return [size,coins]
#         dfs(root)
#         return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur):
            if not cur:
                return 0
            lextra = dfs(cur.left)
            rextra = dfs(cur.right)
            extra_coins = (cur.val-1) + lextra + rextra
            self.res += abs(extra_coins)
            return extra_coins
        dfs(root)
        return self.res