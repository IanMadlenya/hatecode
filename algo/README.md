Algorithm questions, usually given a real problem, and you need to figure out an optimal solution, and code it up - it is usually not bounded to any programming language.

### How to prepare
You should mimic the real interview scenario as much as possible:
* Do practice e on paper - interview are usually done on paper or whiteboard, not computer.
* Do it within a limited time, like 15 minutes, or 20 minutes - as a real interview is usually time bounded, and you maybe nervous..
* Get your hands on with following coding tactics
* Try real interviews for your non-favorite position first - the experience would be very valuable.

### Common coding tatics 
There are some useful tactics you need to be familiar with, they are very commonly used when you solve coding problems, they are patterns, they are building blocks
* Operate pointers in an array
* Operate pointers in a list - it is always useful to maintain `pre, cur, next` pointers when you solve certain problems
* Operate index in an array - rotate: (start + 1) % 5; (start + 4) % 5;  binary search
* recursive (how to recursive, when recursion ends?) - it could solve a lot of tree/binary related problem, although at the very first, it is not that clear.
* iterative(loop)
* stack (isvalid('()[]{}')
* queue (BFS, traverse a tree by level)
* list: reverse a single linked list
* tree: LCT, traverse
* graph: DFS, BFS(queue), adjcent list, adjcent matrix

### Algorithm design
* Divide and Conquer
* Dynamic Programming
* Greedy

### Interview tips
* Finish the main workflow first, and then check the edge case to correct.
* Think through your solution, or dicuss it before rush to coding
* Draw some diagram to help you better analyze the solution, which could also be used to explain your idea to interviewer.
* Write your code with large interval - so you could insert code late when you see bugs
* Put `{` at the end of the previous line, rather than on a new line - you don't have enough space, like:

```
for(auto& s: sets) {
    s.erase(val)
}
```

### Reference
* [LeetCode](https://leetcode.com)
* [LeetCode - Clean Code Handbook](https://leetcode.com/book/)
* [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/)

### Example questions
* Remove a char from a string (O(n))
* Remove all duplicated chars from a string (O(n))
