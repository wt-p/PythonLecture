# from .module3 import myfunc3
# from ..subdir import module3
# from .. import module1
from ..module1 import myfunc as module1_func
def myfunc():
    print("This is myfunc from module2")

def myfunc2():
    print("This is myfunc2 from module2")
    # myfunc3()
    # module3.myfunc3()
    module1_func()