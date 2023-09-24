import data_structure as ds
import random

node_list = []

# linked list데이터 생성
for i in range(5):
    node_list.append(ds.Node(random.randint(1, 10000)))

print(node_list)

for idx in range(1, len(node_list)): # data와 link부분 연결
    node_list[idx - 1] + node_list[idx]
    print(node_list[idx - 1] + node_list[idx])

print(node_list[0].next)

a = node_list[0]
print(a)

# # treverse(링크작업)
# cur_node = a
# while cur_node is not None:
#     print(cur_node.data)
#     cur_node = cur_node.next
# else:
#     print("End of List")