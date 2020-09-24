import time

class BenchmarkMeta(type):
    def __init__(cls, classname, bases, cls_dct):
        super().__init__(classname, bases, cls_dct)
        for name, attr in cls_dct.items():
            if not name.startswith("__") and callable(attr):
                setattr(cls, name, benchmark(attr))


def benchmark(f):
    def _benchmark(*args, **kwargs):
        print("Called method: {}".format(f.__name__)) 

        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()

        print("Execution time: {}s\n".format(end_time - start_time)) 
        return res

    return _benchmark

