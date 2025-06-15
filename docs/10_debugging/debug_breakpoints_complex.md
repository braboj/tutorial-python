# debug_breakpoints_complex

```python
# Advanced Breakpoint Scenarios
# --------------------------------------------------------------------------------
# This script explores a couple of techniques for stopping execution only when
# certain conditions are met. An if-statement can invoke the builtin breakpoint
# function when values match specific criteria, and you can set a conditional
# breakpoint in pdb with ``break my_script.py:20, x > 10``. Studying these
# patterns helps you focus on the critical moments that reveal bugs.


def process_items(items):
    for item in items:
        if item % 2 == 0:
            breakpoint()  # stops when item is even
        if item > 50:
            import pdb
            pdb.set_trace()  # triggers on large values
        print(f'processed {item}')


if __name__ == "__main__":
    sample = [1, 3, 4, 8, 60, 5]
    process_items(sample)
```
