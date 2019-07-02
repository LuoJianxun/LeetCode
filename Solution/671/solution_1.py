# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def generate(node, temp = []):
            temp.append(node.val)
            if node.left:
                generate(node.left, temp)
                generate(node.right, temp)
            return temp
        left = generate(root.left) if root.left else []
        right = generate(root.right) if root.right else []
        res = left + [root.val] + right
        result = sorted(set(res))
        return -1 if len(result) == 1 else result[1]
