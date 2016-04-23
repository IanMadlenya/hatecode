algorithm, usually gives you a problem, and you need to find out a solution, and code it up, it is not bounded to any programming language.

### Coding tips
You should mimic the real interview scenario as much as possible:
* Do it on paper, within a limited time, like 15 minutes, or 20 minutes - as a real interview is usually done on white board, or on a paper, rather than on computer, and it is time bounded.
* Draw some diagram to help you better analyze the solution, which could also be used to explain your idea to interviewer.
* Write your code with large interval - so you could insert code late when you see bugs
* Put `{` at the end of the previous line, rather than on a new line - you don't have enough space, like:

```
for(auto s: sets) {
    s.erase(val)
}
```

### Common coding tatics 
There are some useful tactics you need to be familiar with, they are very commonly used when you solve coding problems, they are patterns, they are building blocks
* Operate pointers in an array
* Operate pointers in a list - it is always useful to maintain `pre, cur, next` pointers when you solve certain problems
* Operate index in an array - rotate: (start + 1) % 5; (start + 4) % 5
* recursive (how to recursive, when recursion ends?)
* iterative(loop)
* list: reverse a single linked list
* tree: LCT, traverse
* graph: DFS, BFS(queue), adjcent list, adjcent matrix

### Algorithm design
* Divide and Conquer


### Example questions
* Remove a char from a string (O(n))
