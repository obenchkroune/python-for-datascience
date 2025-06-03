def NULL_not_found(object: any) -> int: # type: ignore
    null_types = {
        None: 'Nothing',
        float('NaN'): 'Cheese',
        0: 'Zero',
        '': 'Empty',
        False: 'Fake'
    }

    found_type = null_types.get(object)
    if found_type is None:
        print("Type not Found")
        return 1
    else:
        data = [ s for s in [str(object), str(type(object))] if len(s)]
        print(f"{found_type}: {' '.join(data)}")
        return 0
