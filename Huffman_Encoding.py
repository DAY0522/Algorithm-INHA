from queue import PriorityQueue

class nodetype:
    def __init__ (self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.code = ''

    def __lt__(self, other): # 객체간 대소비교가 가능하도록 추가함
        return self.freq < other.freq # freq를 기준으로 정렬 기준을 정의

def huffman(n: int, PQ: PriorityQueue):
    for _ in range(1, n):
        p = PQ.get()[1] # 우선순위(freq)가 낮은 걸 꺼냄
        q = PQ.get()[1]
        r = nodetype(None, p.freq + q.freq) # 두 node를 합친 새로운 node를 생성
        r.left = p
        r.right = q
        PQ.put((r.freq, r))
    return PQ.get()[1]

def huffman_encode(node, x):
    if node: # 노드가 비어있지 않으면
        huffman_encode(node.left, x + "0") # 왼쪽자식이면 0
        node.code += x
        if node.symbol: # node의 symbol이 존재할 때만 code 출력
            print(node.symbol, node.code)
        huffman_encode(node.right, x + "1")  # 오른쪽자식이면 1

'''# 각 노드 생성 EX1
node1 = nodetype('r', 27)
node2 = nodetype('A', 15)
node3 = nodetype('B', 12)
node4 = nodetype('C', 9)
node5 = nodetype('D', 5)
node6 = nodetype('E', 10)
node7 = nodetype('F', 11)
'''

# 각 노드 생성 EX2
node1 = nodetype("ROOT", 27)
node2 = nodetype("ABC", 12)
node3 = nodetype("ABCC", 7)
node4 = nodetype("AB", 19)
node5 = nodetype("A", 35)
node6 = nodetype("B", 40)
node7 = nodetype("BABA", 15)


# PQ 생성 후 PQ에 각 노드 삽입
que = PriorityQueue()
que.put((node1.freq, node1))
que.put((node2.freq, node2))
que.put((node3.freq, node3))
que.put((node4.freq, node4))
que.put((node5.freq, node5))
que.put((node6.freq, node6))
que.put((node7.freq, node7))

parentNode = huffman(7, que) # huffman tree 생성
huffman_encode(parentNode, '') # inorder traversal을 이용해 출력