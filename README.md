# Chocolate

**Chocolate** is a Python package that improves Python's magic variables (`*args` and `**kwargs`).

```python
import chocolate


# Here is some function.
def example_function(arg1, arg2: int, arg3=0, arg4: str = "!"):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}, arg4: {arg4}")

# We can give this function a dictionary of arguments using **kwargs.
kwargs = {"arg1": -2, "arg2": -1, "arg4": ""}
example_function(**kwargs)

# But what if the **kwargs dictionary has additional keys?
broken_kwargs = {"arg1": "This", "arg2": "does", "undefined_arg": "not", "arg3": "work"}
try:
    example_function(**broken_kwargs)
except Exception as exception:
    print(exception)

# Chocolate can take care of that!
chocolate.call(example_function, broken_kwargs)
```
