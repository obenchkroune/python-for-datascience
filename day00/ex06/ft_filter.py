def ft_filter(func, iterable):
    """
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    for it in iterable:
        if func is not None and func(it):
            yield it
        elif func is None and it:
            yield it