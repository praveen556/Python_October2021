#Merge k Sorted Singly Linked Lists
#Given k singly linked lists where each linked list is sorted in ascending order, merge all of them into a single sorted linked list.

#Example:
#Input: [ [1 -> 3 -> 5], [3 -> 4], [7] ].
#Output: 1 -> 3 -> 3 -> 4 -> 5 -> 7

#Notes:
#Constraints:
#0 <= k <= 104.
#0 <= Length of each linked list <= 103.
#-109 <= Node values <= 109.
#Sum of the lengths of all linked lists won’t exceed 105.
#Custom Input:
#Input Format:
#The first line contains the value of k. Then the description of the k input linked lists is given one by one in two separate lines each. The first line contains the number of nodes and the next line contains the values of the nodes in a space-separated manner.
#Input for “Example”  above would be:
#3
#3
#1 3 5
#2
#3 4
#1
#7

#Output Format:
#The output contains the node values of the returned list in a space-separated manner.
#Output for “Example” above would be:
#1 3 3 4 5 7

'''
    class SinglyLinkedListNode:
        def __init__(self, node_data):
            self.data = node_data
            self.next = None

    The function accepts an ARRAY of SinglyLinkedListNodes as input
    and is expected to return a SinglyLinkedListNode.

    Complete the function below.
'''

def merge_k_lists(lists):
    all_nodes=[]
    head=k=SinglyLinkedListNode(0)
    for i in lists:
        while i:
            all_nodes.append(i.data)
            i = i.next
    for x in sorted(all_nodes):
        k.next = SinglyLinkedListNode(x)
        k = k.next
    return head.next
