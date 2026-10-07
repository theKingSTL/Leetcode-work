class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        memo = {}

        def check(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            key = (id(a), id(b))
            if key in memo:
                return memo[key]

            result = a.val == b.val and check(a.left, b.left) and check(a.right, b.right)
            memo[key] = result
            return result

        return check(p, q)