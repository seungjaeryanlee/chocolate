import inspect


def _get_subdict(original_dict, subdict_keys):
    return {k:v for k,v in original_dict.items() if k in subdict_keys}

def filter_args(all_kwargs, func):
    args = inspect.getfullargspec(func).args
    filtered_kwargs = _get_subdict(all_kwargs, args)
    return filtered_kwargs
