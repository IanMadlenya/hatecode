C++ language features, and coding

### Core Language
* casting operators (static_cast, const_cast, dynamic_cast, reinterpret_cast) -> what will happen if dynamic_cast failed?
* why const member function? (immutable object)
* static
* inline vs. macro
* extern -> extern "C" -> name mangling
* malloc vs. new (new[], delete)
* RAII
* ptr vs. ref
* heap vs. stack
* struct vs. class (visibility; typename)
* Compiler generated functions? (constructor, destructor, copy constructor, assignment)
* sizeof(EmptyClass)
* prefix operator vs postfix operator -> how to override?
* initilization list -> order
* Given a calss with 2 base classes, 2 member objects: constructor, destructor order

### Polymorphism
* virtual destructor
* virtual -> vptr & vtable -> RTTI
* pure virtual
* virtual inheritance, when, why?
* polymorphism vs overloading -> overload by? (args, const & volatile (cv-qualifer), template fn return type)

### Generic(template)
* How to force template instantiation
* Complete specialization vs. partial specialization
* What is member template function -> does it need to be in a template class?
* CRTP
* SFINAE
* what are trait class? (use template specilization to dispatch in compile time(std::advance); iterator_traits; numeric_limits)
* Write a smart pointer
* Write a program to compute sum of (1..N) in compile time
* Write a program to compute the Fibbonacci numbers
* Explain policy and trait(policy to inject behavior, like allocator, hash for std containers; traits to extract properties, like iterator_traits, numeric limits, is_integral)
* Write a is_equal template function (int, float?)

### Exception
* Explain exception(error handling, separted from core logic, performance)
* What does 'exception safe' mean? (no-throw, no-change, no-leak), give an example(STL containers)
* What happens to the stack when an exception is thrown? (steps of stack unwind)
* What types are throwable? (any type -> copy constructable -> not limited by exception specification)
* throw exception from a ctor?
* throw exception from dtor?
* why do you catch by ref?

### C++11
https://gcc.gnu.org/projects/cxx-status.html
* What C++11 features you are using?
* auto
* lambda
* rvalue reference?
* range loop

### STL & boost
* What boost libraries you have used?
* What are the type requirements for an STL container? (default ctor; copy ctor; assignment; dtor)
* vector vs. list
* what is deque
* map vs. unordered_map
* name types of iterators
* what is the default sort algo in the std?
* What is the advantage of the design of iterators? (algorithm - iterator - container)
* When is an iterator invalidated? (when memory it points to moves: resize, tree rebalance, rehash, remove...)
* Could we use vector<auto_ptr<T>>
* Smart pointers: shared_ptr, unique_ptr, weak_ptr
* std::bind, std::ref
* stack.pop() - stack.top(), why not just one.
* Write a vector of integer, then look for the first odd number in the vector? (direct indexing vs iterators; function objecvt vs pointer on function vs lambda - std::find)

### Multithreading
* thread vs. process
* mutex vs. semaphore vs. conditional variable
* What is memory order?
* how to debug a deadlock? (drop a stack trace: gstack; gdb:bt)
* Write a thread-safe singleton
* Write a CountDownLauch usinig mutex & contion variable
* Write a blocking queue
* When to use lock/condition variable/CountDownLatch?
* There are 4 threads executing a function foo(), thread 1 will send out a message A, while other thread will send out message B, implement foo() properly to make sure A is always sent out first.

### Linux C++
* LD_LIBRARY_PATH
* LD_PRELOAD
* RPATH/RUNPATH
* When do you use strace? (file, system call)
* PCH
* binutils: c++filt, nm, readelf...

### Testing
* What test framework you use?
* What is mock object? have you ever used it?

### Misc
* How to debug memory leaks (redefine new/delete; valgrind...)

### References
* [C++ Reference](http://www.cplusplus.com/reference)
* [Cpp Reference](http://en.cppreference.com/w/)
* [Cpp Core Guidelines](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md)
* [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
* [Optimizing software in C++: An optimization guide for Windows, Linux and Mac platforms](http://www.agner.org/optimize/optimizing_cpp.pdf)

### Books
* [A Tour of C++](http://techbus.safaribooksonline.com/book/programming/cplusplus/9780133549041)
* [Effective C++: 55 Specific Ways to Improve Your Programs and Designs, Third Edition](http://techbus.safaribooksonline.com/0321334876/ibk01-toc?percentage=0&reader=html)
* [Effective Modern C++](http://techbus.safaribooksonline.com/book/programming/cplusplus/9781491908419)
* [C++ Template Metaprogramming: Concepts, Tools, and Techniques from Boost and Beyond](http://techbus.safaribooksonline.com/book/programming/cplusplus/0321227255)
* 《Linux多线程服务端编程 - 使用muduo C++网络库》

