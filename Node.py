class Node(object):
    def __init__(self, marker, children, parent):
        self.marker = marker
        self.children = children
        self.parent = parent

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    @staticmethod
    def from_token(token, children):
        return Node(token, children, None)
