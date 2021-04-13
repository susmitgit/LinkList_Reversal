class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:

  def convert_stack(self, ll: ListNode):
    stack, tmp =[], ll
    while tmp:
      stack.append(tmp.val)
      tmp = tmp.next
    print('convert_stack', stack)
    return stack
  
  def create_Node(self, stack):
    if len(stack) == 1:
      Node = ListNode(val=stack[len(stack) - 1], next=None)
    else:  
      Node = ListNode(val=stack[len(stack) - 1], next=self.create_Node(stack[0:len(stack) -1]))
    print("create_node", Node)
    return Node
  
  def make_linkedlist(self, stack):
    print("string", stack, len(stack))
    l = ListNode(val=stack[len(stack) -1], next=self.create_Node(stack[0:len(stack) -1]))
    print('make_linked_list', l)
    return l
    
  def reverse_stack_value(self, stack): # [1,2,3,4,5]
    c = 0
    final_val = 0
    # 5 4 3 2 1
    for v in stack:
      final_val = final_val + (v * 10 ** c )
      c += 1
    print('reverse_stack_value', final_val)
    return final_val

  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    converted_stack = self.convert_stack(l1)
    
    l1_val = self.reverse_stack_value(self.convert_stack(l1))
    l2_val = self.reverse_stack_value(self.convert_stack(l2))
    link_list = self.make_linkedlist(str(int(l1_val) + int(l2_val)))
    self.convert_stack(link_list)
    return link_list
   
head1 = ListNode(2, ListNode(4, ListNode(3)))
head2 = ListNode(5, ListNode(6, ListNode(4)))
Solution().addTwoNumbers(head1,head2)