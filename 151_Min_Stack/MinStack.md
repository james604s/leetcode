# 151 Easy: Min Stack
>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
+ MinStack() initializes the stack object.
+ void push(val) pushes the element val onto the stack.
+ void pop() removes the element on the top of the stack.
+ int top() gets the top element of the stack.
+ int getMin() retrieves the minimum element in the stack.
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## **解題:**
實作一個 stack 但是可以支援找到當前 stack 中最小值的功能。

### **作法1:**
用py內建函數, 直接用append, pop 實作, getMin函式則用min()。

### **作法2:** 
**空間換取時間**

**當 stack 是 [3] 的時候最小元素是 3。
當再 push 2 到 stack 中，stack 是 [3, 2] 的時候最小元素是 2。
當再 push 3 到 stack 中，stack 是 [3, 2, 3] 的時候最小元素是 2。
上述最小元素分別是3, 2, 2, 存起來後呼叫getMin時可以直接回傳。**