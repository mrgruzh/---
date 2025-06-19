import sys

class Node(object):
    def __init__(self):
        super().__init__()
        self.value = 0.0
        self.childs = []
        self.parent = None

    def addChild(self, obj):
        self.childs.append(obj)

    def isLeaf(self):
        return len(self.childs) == 0

    def setValue(self, value):
        self.value = value


class Tree(object):
    def __init__(self):
        super().__init__()
        self.root = None
        self.nodes = []
        self.nodeRadius = 30
        self.x_spacing = 35
        self.y_spacing = 70
        self.minimaxMoves = {}
        self.alphaBetaMoves = {}

    def addNode(self, parent=None, value=0.0):
        newNode = Node()
        newNode.setValue(value)
        if parent:
            parent.addChild(newNode)
            newNode.parent = parent
        self.nodes.append(newNode)
        if not self.root:
            self.root = newNode
        return newNode

    def minimax(self, node, depth, maximizingPlayer):
        if depth == 0 or node.isLeaf():
            return node.value

        if maximizingPlayer:
            bestValue = float("-inf")
            for child in node.childs:
                v = self.minimax(child, depth - 1, False)
                if v > bestValue:
                    self.minimaxMoves[node] = child
                bestValue = max(bestValue, v)
            node.value = bestValue
            return bestValue
        else:
            bestValue = float("inf")
            for child in node.childs:
                v = self.minimax(child, depth - 1, True)
                if v < bestValue:
                    self.minimaxMoves[node] = child
                bestValue = min(bestValue, v)
            node.value = bestValue
            return bestValue

    def alphaBeta(self, node, depth, alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True):
        if depth == 0 or node.isLeaf():
            return node.value

        if maximizingPlayer:
            value = float("-inf")
            for child in node.childs:
                v = self.alphaBeta(child, depth - 1, alpha, beta, False)
                if v > value:
                    self.alphaBetaMoves[node] = child
                value = max(value, v)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break  # Бета-отсечение
            node.value = value
            return value
        else:
            value = float("inf")
            for child in node.childs:
                v = self.alphaBeta(child, depth - 1, alpha, beta, True)
                if v < value:
                    self.alphaBetaMoves[node] = child
                value = min(value, v)
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Альфа-отсечение
            node.value = value
            return value
def depth(self, node):
    max_depth = 0
    for child in node.childs:
        max_depth = max(max_depth, self.depth(child))
    return max_depth + 1

def calculateNodesPostion(self):
    x_spacing = self.x_spacing
    y_spacing = self.y_spacing
    leaf_x = 100
    y = 100

    def calculatePosition(node):
        def nodeLevel(node):
            level = 0
            while node.parent:
                level += 1
                node = node.parent
            return level

        nonlocal y, x_spacing, leaf_x

        for child in node.childs:
            calculatePosition(child)

        y = (1 + nodeLevel(node)) * y_spacing

        if not node.isLeaf():
            childCount = len(node.childs)
            node.position = {
                'x': int((node.childs[0].position['x'] + node.childs[childCount - 1].position['x']) / 2),
                'y': y
            }
        else:
            node.position = {
                'x': leaf_x,
                'y': y
            }
            leaf_x += x_spacing

    if self.root:
        calculatePosition(self.root)

def drawNodes(self, qp):
    r = self.nodeRadius
    # Отображаем линии связи
    for node in self.nodes:
        x1, y1 = node.position['x'], node.position['y']
        if node.parent:
            x2, y2 = node.parent.position['x'], node.parent.position['y']
            qp.drawLine(x1, y1, x2, y2)
    # Отображаем узлы
    for node in self.nodes:
        x, y = node.position['x'], node.position['y']
        qp.drawEllipse(x - int(r / 2), y - int(r / 2), r, r)

def drawNodesValues(self, qp):
    r = self.nodeRadius
    fm = qp.fontMetrics()
    for node in self.nodes:
        x, y = node.position['x'], node.position['y']
        s = str(node.value)
        w = fm.width(s)
        h = fm.height()
        qp.drawText(x - int(w / 2), y + int(h / 2), s)

def drawMoveLines(self, qp, maximizingPlayer=True):
    x_spacing = self.x_spacing
    y_spacing = self.y_spacing
    x = 50
    y = self.y_spacing
    rest = 1 if maximizingPlayer else 0
    i = 1
    fm = qp.fontMetrics()
    depth = self.depth(self.root) + 1

    while i < depth:
        s = 'MAX' if i % 2 == rest else 'MIN'
        w = fm.width(s)
        h = fm.height()
        qp.drawText(x - int(w / 2), y + int(h / 2), s)
        i += 1
        y += self.y_spacing

# Пример создания дерева
tree = Tree()
A = tree.addNode()
B1 = tree.addNode(A)
B2 = tree.addNode(A)
B3 = tree.addNode(A)
C1 = tree.addNode(B1)
C2 = tree.addNode(B1)
C3 = tree.addNode(B2)
C4 = tree.addNode(B2)
C5 = tree.addNode(B2)
C6 = tree.addNode(B3)
C7 = tree.addNode(B3)
D1 = tree.addNode(C1)
D2 = tree.addNode(C1)
D3 = tree.addNode(C1)
D4 = tree.addNode(C2)
D5 = tree.addNode(C2)
D6 = tree.addNode(C2)
D7 = tree.addNode(C3)
D8 = tree.addNode(C3)
D9 = tree.addNode(C4)
D10 = tree.addNode(C4)
D11 = tree.addNode(C5)
D12 = tree.addNode(C5)
D13 = tree.addNode(C6)
D14 = tree.addNode(C6)
D15 = tree.addNode(C7)

tree.calculateNodesPostion()
