class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return (f'Node(val: {self.val},'
                f'left: {self.left if self.left else None},'
                f'right: {self.right if self.right else None})')

    def __repr__(self):
        return (f'Node(val: {self.val},'
                f'left: {self.left if self.left else None},'
                f'right: {self.right if self.right else None})')


def univals(tree: Node) -> int:
    if tree is None:
        return 0

    elif tree.right or tree.left:
        return sum(
                    [
                        univals(tree.left) + 1 if tree.left.val == tree.val else
                        univals(tree.left),
                        univals(tree.right) + 1 if tree.right.val == tree.val
                        else univals(tree.right)
                    ]
                )

    else:
        return 0

tree = Node(0, left=Node(1),
        right=Node(0,
            left=Node(1,
                left=Node(1),
                right=Node(1)
                ),
            right=Node(0)
            )
        )

print(univals(tree))
