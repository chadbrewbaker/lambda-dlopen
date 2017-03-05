# lambda-dlopen
Passing programs over the wire for execution on AWS Lambda.



How to rename a function in a shared object file without recompiling:
```bash
objcopy --redefine-sym old=new  libold.so libnew.so
``` 
