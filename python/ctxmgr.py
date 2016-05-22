#!/bin/python

import contextlib
import os
import copy

@contextlib.contextmanager
def environ_switcher(env_name, value):
	try:
		orig_environ = copy.deepcopy(os.environ)
		os.environ[env_name] = value
		yield
	finally:
		os.environ = orig_environ


print os.getenv("TESTING_ENV")
with environ_switcher('TESTING_ENV', 'hello, world'):
	print os.getenv("TESTING_ENV")
print os.getenv("TESTING_ENV")