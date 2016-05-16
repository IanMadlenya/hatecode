C++ language features, and coding

### General
* inline vs. macro
* static
* extern -> extern "C" -> name mangling
* ptr vs. ref
* heap vs. stack
* struct vs. class (visibility; typename)
* Compiler generated functions? (constructor, destructor, copy constructor, assignment)
* sizeof(EmptyClass)
* casting operators (static_cast, const_cast, dynamic_cast, reinterpret_cast) -> what will happen if dynamic_cast failed?
* prefix operator vs postfix operator -> how to override?

### Object Creation & Destruction
* malloc vs. new
* initilization list -> order
* virtual destructor

### Inheritance & Polymorphism
* virtual -> vptr & vtable -> RTTI
* polymorphism vs overloading -> overload by? (args, const & volatile (cv-qualifer), template fn return type)

### Template
* complete specialization vs. partial specialization
* What is member template function -> does it need to be in a template class?
* CRTP
* SFINAE
* what are trait class? (use template specilization to dispatch in compile time(std::advance); iterator_traits; numeric_limits)
* Write a smart pointer
* Write a program to compute sum of (1..N) in compile time
* Write a program to compute the Fibbonacci numbers

### Resouce Management
* RAII

### Exception
* What happens to the stack when an exception is thrown?
* What types are throwable? (any type -> copy constructable -> not limited by exception specification)
* What does 'exception safe' mean? (no-throw, no-change, no-leak), give an example(STL containers)
* throw exception from a ctor?
* throw exception from dtor?
* why do you catch by ref? 

### STL & boost
* What are the type requirements for an STL container? (default ctor; copy ctor; assignment; dtor)
* vector vs. list
* map vs. unordered_map
* name types of iterators
* When is an iterator invalidated? (when memory it points to moves: resize, tree rebalance, rehash, remove...)
* Could we use vector<auto_ptr<T>>
* Smart pointers: shared_ptr, unique_ptr, weak_ptr
* bind???

### Multithreading
* thread vs. process
* mutex vs. semaphore
* how to debug a deadlock? (drop a stack trace: gstack; gdb:bt)
* Write a thread-safe singleton
* Write a CountDownLauch usinig mutex & contion variable
* Write a blocking queue

### Linux C++
* LD_LIBRARY_PATH
* LD_PRELOAD
* RPATH/RUNPATH
* When do you use strace? (file, system call)

### Testing
* What test framework you use?
* What is mock object? have you ever used it?


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

