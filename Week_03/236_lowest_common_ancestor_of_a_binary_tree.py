# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 原始思路，recursion，再一路往上返回三个变量，又臭又长， 而且花了很长时间
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, _, LCA_node = self.nodeHasPandQ(root, p, q)
        return LCA_node

    # Function would return hasP, hasQ, LCA Node
    def nodeHasPandQ(self, node, p, q):
        if node is None:
            return False, False, None

        if node.left is None and node.right is None:
            return node is p, node is q, None
        elif node.left is None or node.right is None:
            nc_has_p, nc_has_q, lca_node = self.nodeHasPandQ(node.right, p, q) if node.left is None else self.nodeHasPandQ(node.left, p, q)

            if lca_node is not None: return nc_has_p, nc_has_q, lca_node 

            if node is p:
                n_has_p = True
                n_has_q = nc_has_q
                lca_node = node if nc_has_q else None
            elif node is q:
                n_has_p = nc_has_p
                n_has_q = True
                lca_node = node if nc_has_p else None
            else:
                n_has_p = nc_has_p
                n_has_q = nc_has_q
                lca_node = None
            return n_has_p, n_has_q, lca_node
        else:
            ncl_has_p, ncl_has_q, l_lca_node = self.nodeHasPandQ(node.left, p, q)
            ncr_has_p, ncr_has_q, r_lca_node = self.nodeHasPandQ(node.right, p, q)

            if l_lca_node is not None or r_lca_node is not None:
                lca_node = l_lca_node if l_lca_node else r_lca_node
                return True, True, lca_node

            if (ncl_has_p and ncr_has_q) or (ncl_has_q and ncr_has_p):
                return True, True, node
            elif ncr_has_p or ncl_has_p:
                lca_node = node if node is q else None
                return True, node is q, lca_node
            elif ncr_has_q or ncl_has_q:
                lca_node = node if node is p else None
                return node is p, True, lca_node
            else:
                return node is p, node is q, None

# Leetcode国际站
# 看了官方解法，采用回溯
# The approach is pretty intuitive.
# Traverse the tree in a depth first manner. The moment you encounter either of the nodes p or q, return some boolean flag.
# The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be
# the node for which both the subtree recursions return a True flag. It can also be the node which itself is one of p or q 
# and for which one of the subtree recursions returns a True flag.
#
# 看了光头哥的解法，很巧妙的用了None，并且在探到p或者q的时候马上返回，本质上是对官方的优化。
