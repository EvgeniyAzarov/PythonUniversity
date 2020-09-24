import time

def benchmark(f):
    def _benchmark(*args, **kwargs):
        print("Called method: {}".format(f.__name__)) 

        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()

        print("Execution time: {}s\n".format(end_time - start_time)) 
        return res

    return _benchmark

def benchmark_class(cls):
    for name, method in cls.__dict__.items():
        if not name.startswith("__"):
            setattr(cls, name, benchmark(method))
    return cls
        
