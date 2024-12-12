# leetcode array representation of tree
# 
# [2,1,3]
# 
#     -> 3
# -> 2
#     -> 1
# 
# [4,2,7,1,3,6,9]
# 
#         -> 9
#     -> 7
#         -> 6
# -> 4
#         -> 3
#     -> 2
#         -> 1
# 
# [4,2,7,1,3,6,9]
# 
#         -> 9
#     -> 7
#         -> 6
# -> 4
#         -> 3
#     -> 2
#         -> 1

class TreeNode(object):

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def array_to_binary_tree(arr):
  if not arr:
    return None

  root = TreeNode(arr[0])
  queue = [root]
  i = 1

  while queue and i < len(arr):
    node = queue.pop(0)  # popping off first elem

    if i < len(arr):
      if arr[i] is not None:
        node.left = TreeNode(arr[i])
        queue.append(node.left)
      i += 1

    if i < len(arr):
      if arr[i] is not None:
        node.right = TreeNode(arr[i])
        queue.append(node.right)
      i += 1

  return root

def dfs(root):
    if root == None: return
    # inorder traversal
    dfs(root.left)
    print(root.val)
    dfs(root.right)

def dfs_with_loop(root):
    pass
    #TODO

def bfs(root):
    nodes = [root]
    while nodes:
      foo = []
      for node in nodes:
        if node:
          print(node.val)
          foo.append(node.left)
          foo.append(node.right)
      nodes = foo

def main():

# [2,1,3]
#                   -> None
#            -> 3  
#                   -> None
# root    -> 2
#                   -> None
#            -> 1
#                   -> None

  # dfs(array_to_binary_tree([2,1,3]))

# [4,2,7,1,3,6,9]
# 
#         -> 9
#     -> 7
#         -> 6
# -> 4
#         -> 3
#     -> 2
#         -> 1
  bfs(array_to_binary_tree([4,2,7,1,3,6,9]))

main()