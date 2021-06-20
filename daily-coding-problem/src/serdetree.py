from ast import literal_eval

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(tree: Node) -> str:
    if tree is None:
        return str({'val': None, 'left': None, 'right': None})
    else:
        return str({'val': tree.val, 'left': serialize(tree.left),
                'right': serialize(tree.right)
                })


def deserialize(tree: str) -> Node:
    if tree:
        parsed = literal_eval(tree)
        if not (parsed['left'] and parsed['right']):
            return Node(parsed['val'], None, None)
        else:
            return Node(parsed['val'], deserialize(parsed['left']),
                    deserialize(parsed['right']))
    else:
        return None

serialized = serialize(tree)
deserialized = deserialize(serialized)

print(serialized, type(serialized))
print(deserialized, type(deserialized))
