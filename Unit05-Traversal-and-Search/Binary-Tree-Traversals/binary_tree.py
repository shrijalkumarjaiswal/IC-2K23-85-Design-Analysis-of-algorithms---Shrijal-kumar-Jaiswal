"""
Binary Tree Traversals - Unit 5: Traversal & Search
Recursive and iterative implementations of Preorder, Inorder, Postorder.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_sample_tree():
    """Build sample tree:
            1
           / \
          2   3
         / \   \
        4   5   6
    """
    nodes = {i: TreeNode(i) for i in range(1, 7)}
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].left, nodes[2].right = nodes[4], nodes[5]
    nodes[3].right = nodes[6]
    return nodes[1]


# RECURSIVE
def preorder_recursive(root):
    if not root: return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

def inorder_recursive(root):
    if not root: return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

def postorder_recursive(root):
    if not root: return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


# ITERATIVE
def preorder_iterative(root):
    if not root: return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return result

def inorder_iterative(root):
    stack, result, curr = [], [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

def postorder_iterative(root):
    if not root: return []
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left: stack1.append(node.left)
        if node.right: stack1.append(node.right)
    return stack2[::-1]


def run_example():
    print("=" * 60)
    print("BINARY TREE TRAVERSALS")
    print("=" * 60)

    root = build_sample_tree()

    print("Tree:")
    print("      1")
    print("     /  \\")
    print("    2    3")
    print("   / \\    \\")
    print("  4   5    6")

    print(f"\nPreorder (Root-Left-Right):")
    print(f"  Recursive: {preorder_recursive(root)}")
    print(f"  Iterative: {preorder_iterative(root)}")

    print(f"\nInorder (Left-Root-Right):")
    print(f"  Recursive: {inorder_recursive(root)}")
    print(f"  Iterative: {inorder_iterative(root)}")

    print(f"\nPostorder (Left-Right-Root):")
    print(f"  Recursive: {postorder_recursive(root)}")
    print(f"  Iterative: {postorder_iterative(root)}")

    # Verify
    assert preorder_recursive(root) == preorder_iterative(root)
    assert inorder_recursive(root) == inorder_iterative(root)
    assert postorder_recursive(root) == postorder_iterative(root)
    print("\nAll recursive == iterative PASS")


def run_tests():
    print("\n" + "=" * 60)
    print("TEST CASES")
    print("=" * 60)

    # Single node
    root = TreeNode(1)
    assert preorder_recursive(root) == [1]
    assert inorder_recursive(root) == [1]
    assert postorder_recursive(root) == [1]
    print("Single node: PASS")

    # Left skewed
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert preorder_recursive(root) == [1, 2, 3]
    assert inorder_recursive(root) == [3, 2, 1]
    assert postorder_recursive(root) == [3, 2, 1]
    print("Left skewed: PASS")

    # Right skewed
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert preorder_recursive(root) == [1, 2, 3]
    assert inorder_recursive(root) == [1, 2, 3]
    assert postorder_recursive(root) == [3, 2, 1]
    print("Right skewed: PASS")

    # Empty
    assert preorder_recursive(None) == []
    print("Empty tree: PASS")


if __name__ == "__main__":
    run_example()
    run_tests()
    print("\nLEARNING: 3 DFS traversals. Recursive O(n) time/space. Iterative uses stack.")