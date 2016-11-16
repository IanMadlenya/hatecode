Questions:
* How to create a link? (soft, hard, inode?)
* How you check the status of the system? (uptime, top)
* How to print line 3 - 6 of a file
* How to list all files that is name contains "foo", and content contains "bar"
* How to print the first column of output of "ls -l"
* List all unique dependencies of all binaries under directory foo (find ./foo -perm -g+x | xargs ldd | awk '{print $1}' | sort | uniq)
* What you do when a command hangs? (CTRL+C, SIGINT; IO/syscall/ignored by process/sigal not sent), how to handle it? (CTRL+Z; jobs -l; kill -9 $pid)
* How to trouble shoot the hanging command/failed silient?


### Reference
* https://github.com/chassing/linux-sysadmin-interview-questions
