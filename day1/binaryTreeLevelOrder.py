# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        result = []

        while queue:
            level=[]
            queueLen=len(queue)

            for i in range(queueLen):
                node=queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if level:
                result.append(level)


        return result