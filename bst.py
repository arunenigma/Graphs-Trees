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

    def delNoneNodes(self, x, tree, d):
        pass
        '''
        edge_nodes = tree.edges(d.keys()[d.values().index(x)])
        print edge_nodes
        if len(edge_nodes) == 3:
            for edge in edge_nodes:
                for node in edge:
                    if int(node) > len(d.keys()):
                        tree.remove_node(node)
        '''

    def checkDuplicateEdges(self, x, e):
        edges = tree.edges(d.keys()[d.values().index(x)])
        rev_edges = []
        for edge in edges:
            edge = (list(edge))
            edge = [int(item) for item in edge][::-1]
            edge = tuple(edge)
            rev_edges.append(edge)
        if e in rev_edges:
            return True

    def removeSelfLoop(self, e, step, d):
        k_list = []
        for k, v in d.iteritems():
            if v == step:
                k_list.append(k)
        print str(e[0]) + 'arun'
        if e[0] in k_list:
            k_list.remove(e[0])
            return k_list

    def drawTree(self, tree, filename, d):
        print self.insertion_step
        ind = len(d.keys()) + 1

        for step in self.insertion_step:
            print step[0], step[1], step[2]

            if (step[0] is None) and not (step[2] is None):
                tree.add_node(ind, style='filled', label=step[0])
                tree.add_edge(d.keys()[d.values().index(step[1])], ind, style='filled')
                ind += 1
                e = (d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[2])])
                edg = tree.edges(d.keys()[d.values().index(step[2])])
                if len(edg) > 1:
                    del d[d.keys()[d.values().index(step[2])]]
                if self.checkDuplicateEdges(step[2], e):
                    del d[d.keys()[d.values().index(step[2])]]
                if not d.keys()[d.values().index(step[1])] == d.keys()[d.values().index(step[2])]:
                    tree.add_edge(d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[2])],
                                  color='sienna',
                                  style='filled')
                else:
                    fixed_edge_node = self.removeSelfLoop(e, step[2], d)
                    if fixed_edge_node:
                        tree.add_edge(d.keys()[d.values().index(step[1])], fixed_edge_node[0],
                                      color='sienna',
                                      style='filled')
            if not (step[0] is None) and (step[2] is None):

                e = (d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[0])])
                print e
                edg = tree.edges(d.keys()[d.values().index(step[0])])
                if len(edg) > 1:
                    del d[d.keys()[d.values().index(step[0])]]
                if self.checkDuplicateEdges(step[0], e):
                    del d[d.keys()[d.values().index(step[0])]]
                if not d.keys()[d.values().index(step[1])] == d.keys()[d.values().index(step[0])]:
                    tree.add_edge(d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[0])],
                                  color='sienna',
                                  style='filled')
                else:
                    fixed_edge_node = self.removeSelfLoop(e, step[0], d)
                    if fixed_edge_node:
                        tree.add_edge(d.keys()[d.values().index(step[1])], fixed_edge_node[0],
                                      color='sienna',
                                      style='filled')
                tree.add_node(ind, style='filled', label=step[2])
                tree.add_edge(d.keys()[d.values().index(step[1])], ind, style='filled')
                ind += 1

            if not (step[0] is None) and not (step[2] is None):
                e = (d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[0])])
                print
                print d.keys()[d.values().index(step[0])]
                print e

                edg = tree.edges(d.keys()[d.values().index(step[0])])
                if len(edg) > 1:
                    del d[d.keys()[d.values().index(step[0])]]

                if self.checkDuplicateEdges(step[0], e):
                    del d[d.keys()[d.values().index(step[0])]]
                if not d.keys()[d.values().index(step[1])] == d.keys()[d.values().index(step[0])]:
                    tree.add_edge(d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[0])],
                                  color='sienna',
                                  style='filled')
                else:
                    fixed_edge_node = self.removeSelfLoop(e, step[0], d)
                    if fixed_edge_node:
                        tree.add_edge(d.keys()[d.values().index(step[1])], fixed_edge_node[0],
                                      color='sienna',
                                      style='filled')

                e = (d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[2])])
                edg = tree.edges(d.keys()[d.values().index(step[2])])
                if len(edg) > 1:
                    del d[d.keys()[d.values().index(step[2])]]
                if self.checkDuplicateEdges(step[2], e):
                    del d[d.keys()[d.values().index(step[2])]]
                if not d.keys()[d.values().index(step[1])] == d.keys()[d.values().index(step[2])]:
                    tree.add_edge(d.keys()[d.values().index(step[1])], d.keys()[d.values().index(step[2])],
                                  color='sienna',
                                  style='filled')
                else:
                    fixed_edge_node = self.removeSelfLoop(e, step[2], d)
                    if fixed_edge_node:
                        tree.add_edge(d.keys()[d.values().index(step[1])], fixed_edge_node[0],
                                      color='sienna',
                                      style='filled')
            print

            self.delNoneNodes(step[1], tree, d)
            if not step[0] is None:
                self.delNoneNodes(step[0], tree, d)
            else:
                edge_nodes = tree.edges(step[0])
                if len(edge_nodes) > 0:
                    two_edge_node = [n[1] for n in edge_nodes]
                    node_count = dict((i, two_edge_node.count(i)) for i in two_edge_node)
                    if node_count.values()[0] > 1:
                        tree.remove_node(node_count.keys()[0])

            if not step[2] is None:
                self.delNoneNodes(step[2], tree, d)
            else:
                edge_nodes = tree.edges(step[2])
                if len(edge_nodes) > 0:
                    two_edge_node = [n[1] for n in edge_nodes]
                    node_count = dict((i, two_edge_node.count(i)) for i in two_edge_node)
                    if node_count.values()[0] > 1:
                        tree.remove_node(node_count.keys()[0])

        tree.write(filename)
        img = pgv.AGraph(filename)
        img.layout()
        img.draw(filename.split('.')[0] + '.pdf')
        img.close()


if __name__ == '__main__':
    tree = pgv.AGraph(directed=True, strict=True)
    filename = 'tree.dot'
    lst = [random.randint(1, 9) for i in range(5)]
    #lst = [8, 9, 2, 4, 5, 4, 5, 9, 1, 3, 5, 7, 1, 3, 7]
    #lst = [5, 9, 6, 8, 5]
    print lst
    d = {}
    for i in range(len(lst)):
        d[i + 1] = lst[i]
        tree.add_node(i + 1, color='goldenrod2', style='filled', label=lst[i], shape='circle')
    print d
    n = Node(lst[0])
    n.printSubtree()
    for num in lst[1:]:
        n.addNode(num)
    n.drawTree(tree, filename, d)

