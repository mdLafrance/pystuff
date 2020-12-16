import functools

__all__ = ["memoize"]

def memoize(f):
    fcache = {}

    @functools.wraps(f)
    def memf(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in fcache:
            fcache[key] = f(*args, **kwargs)

        return fcache[key]

    memf.fcache = fcache

    return memf