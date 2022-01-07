# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        if root == None:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

if __name__ == '__main__':
    one = TreeNode(val=1)
    two = TreeNode(val=2)
    three = TreeNode(val=3)
    four = TreeNode(val=4)
    seven = TreeNode(val=7)
    
    four.left = two
    four.right = seven

    two.left = one
    two.right = three
    
    sol = Solution()
    print(sol.searchBST(four, 10))
