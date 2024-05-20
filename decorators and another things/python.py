import functools
def decorator(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        b = func(*args, **kwargs)
        return b
    return wraps

@decorator
def add(new: list[str] | str, src: list | None = None) -> list[str]:
    if src is None:
        src = []
    if isinstance(new, str):
        src.append(new)
    else:
        src.extend(new)
    return src

if __name__ == '__main__':
    v = add('test')
    print(v)


