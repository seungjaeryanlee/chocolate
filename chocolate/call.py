import inspect


def _get_subdict(original_dict, subdict_keys):
    return {k:v for k,v in original_dict.items() if k in subdict_keys}

def call(f, all_kwargs):
    args = inspect.getfullargspec(f).args
    sub_kwargs = _get_subdict(all_kwargs, args)
    return f(**sub_kwargs)
