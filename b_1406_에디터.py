import sys

text = sys.stdin.readline()
N = int(sys.stdin.readline())
commands = []

for _ in range(N):
    t = sys.stdin.readline().rstrip()
    commands.append(t)

################################################################

class Node:
    def __init__(self, char):
        self.char = char
        self.prev = None
        self.next = None
        self.is_first = False
        self.is_end = False

print(commands)

dummy = Node('')
dummy.is_first = True
prev = dummy

for c in text:
    new_node = Node(c)
    dummy.next = new_node
    new_node.prev = prev
    prev = new_node

last_dummy = Node('')
last_dummy.is_end = True
prev.next = last_dummy

###################################

cur = prev

for command in commands:
    if command[0] == 'L':
        if cur.is_first is False:
            cur = cur.prev
    elif command[0] == 'D':
        if cur.is_end is False:
            cur = cur.next
    elif command[0] == 'B':
        if cur.is_first is True:
            continue

        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur = cur.prev

    elif command[0] == 'P':
        insert_char = command[-1]
        new_node = Node(insert_char)

        cur.next.prev = new_node
        cur.next = new_node

        new_node.next = cur.next
        new_node.prev = cur
        cur = new_node

result = ''

point = dummy.next
while point.is_end is False:
    print(point.char)
    result += point.char
    point = point.next

print(result)
    







