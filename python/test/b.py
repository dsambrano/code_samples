import inspect
import os

print(poss)

def test():
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    return(filename)


print(os.path.basename(test()))
