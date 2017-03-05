import ctypes

def lambda_handler(event, context):
    libc = ctypes.cdll.LoadLibrary("/lib64/libc.so.6")
    return { "message": libc.div(9,3) }


