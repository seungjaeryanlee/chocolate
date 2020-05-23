# Chocolate

**Chocolate** is a Python package that improves Python's `**kwargs`.

```python
from chocolate import filter_args


# Here is some function.
def example_function(arg1, arg2: int, arg3=3, arg4: str = ""):
    print(f"{arg1} {arg2} {arg3} {arg4}")

# We can give this function a dictionary of arguments using **kwargs.
kwargs = {"arg1": 1, "arg2": 2, "arg4": "4"}
example_function(**kwargs)

# But what if the **kwargs dictionary has additional keys?
broken_kwargs = {"arg1": "This", "arg2": "does", "undefined_arg": "not", "arg3": "work"}
try:
    example_function(**broken_kwargs)
except Exception as exception:
    print(exception)

# Chocolate can take care of that!
example_function(**filter_args(broken_kwargs, example_function))
```
