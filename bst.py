import pygraphviz as pgv
import random


class Node:
    insertion_step = []

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.printSubtree()
            else:
                self.left.addNode(data)  # recursively calling addNode method
        else:
            if self.right is None:
                self.right = Node(data)
                self.printSubtree()
            else:
                self.right.addNode(data)

    def printSubtree(self):
        if not (self.left is None or self.right is None):
            print self.left.data, self.data, self.right.data
            self.insertion_step.append((self.left.data, self.data, self.right.data))

        elif self.left is None and not self.right is None:
            print None, self.data, self.right.data
            self.insertion_step.append((None, self.data, self.right.data))

        elif not self.left is None and self.right is None:
            print self.left.data, self.data, None
            self.insertion_step.append((self.left.data, self.data, None))

        else:
            print None, self.data, None
            self.insertion_step.append((None, self.data, None))

    def drawTree(self, tree, filename):
        ind = 0
        nodes = [(None, self)]  # queue with nodes to process

        while nodes:
            parent, node = nodes.pop(0)
            tree.add_node(ind, label=node.data, color='goldenrod2', style='filled', shape='circle')
            if parent is not None:
                tree.add_edge(parent, ind, color='sienna', style='filled')

            if node.left is not None:
                nodes.append((ind, node.left))
            else:
                none_ind = '{}_left_none'.format(ind)
                tree.add_node(none_ind, label='', color='goldenrod2', style='filled', shape='box')
                tree.add_edge(ind, none_ind, color='sienna', style='filled')

            if node.right is not None:
                nodes.append((ind, node.right))
            else:
                none_ind = '{}_right_none'.format(ind)
                tree.add_node(none_ind, label='', color='goldenrod2', style='filled', shape='box')
                tree.add_edge(ind, none_ind, color='sienna', style='filled')

            ind += 1

        tree.write(filename)
        img = pgv.AGraph(filename)
        img.layout(prog='dot')
        img.draw(filename.split('.')[0] + '.pdf')
        img.close()


if __name__ == '__main__':
    tree = pgv.AGraph(directed=True, strict=True)
    filename = 'tree.dot'
    lst = [random.randint(1, 99) for i in range(50)]
    print lst
    n = Node(lst[0])
    n.printSubtree()
    for num in lst[1:]:
        n.addNode(num)
    n.drawTree(tree, filename)

