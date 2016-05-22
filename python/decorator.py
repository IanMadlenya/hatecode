#!/bin/python
import time

def timeit(func):
	def wrapper_func(*args, **kwargs):
		start = time.clock()
		func(*args, **kwargs)
		end = time.clock()
		print "Elapse time for function '%s': %f" % (func.func_name, end - start)

	return wrapper_func


@timeit
def say(sth):
	print sth


say("hello, world" * 10000)