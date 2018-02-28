#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (37.92%)
# Total Accepted:    101.5K
# Total Submissions: 267.7K
# Testcase Example:  '["MyQueue","empty"]\n[[],[]]'
#
# 
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# 
# 
# pop() -- Removes the element from in front of queue.
# 
# 
# peek() -- Get the front element.
# 
# 
# empty() -- Return whether the queue is empty.
# 
# 
# Notes:
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#
class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()
        
    def peek(self):
        if(self.output == []):
            while(self.input != []):
                self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self):
        return self.input == [] and self.output == []
