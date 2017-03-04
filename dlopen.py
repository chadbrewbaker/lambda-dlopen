import ctypes
libc = ctypes.cdll.LoadLibrary("/usr/lib/libc.dylib")
print libc.div(9,3)
