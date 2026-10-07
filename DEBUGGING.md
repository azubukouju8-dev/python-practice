# Debugging Note

## The error

While installing pytest, I got this error:

```
ERROR: Could not find a version that satisfies the requirement pytestpip (from versions: none)
ERROR: No matching distribution found for pytestpip
```

## What I was doing

I was setting up automated tests. I wanted to run two commands: `pip install pytest` to install the testing tool, then `pip freeze` to save the installed packages into `requirements.txt`.

## What caused it

The two commands ended up on the same line when I copied and pasted them. The terminal ran this as a single command:

```
pip install pytestpip freeze | Out-File -Encoding utf8 requirements.txt
```

`pip install` treats every word after it as a package name, so it tried to install packages called `pytestpip` and `freeze`. The first one does not exist on PyPI, so pip stopped with an error.

## How I fixed it

I ran the two commands separately, one per line:

```
pip install pytest
pip freeze | Out-File -Encoding utf8 requirements.txt
```

The install succeeded and `requirements.txt` was created.

## What I learned

- Read the package name in the error message closely. Seeing `pytestpip` instead of `pytest` showed that two commands had merged.
- Run each terminal command on its own line, and check the output before moving on.
- A "no matching distribution" error from pip usually means a typo in the package name, not a problem with pip itself.