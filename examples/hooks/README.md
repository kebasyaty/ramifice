# hooks

**Hooks - Methods that are called at different stages when accessing the database.**
<br>
( _for a general presentation, how to use hooks methods_ )
<br>
<br>
**Path to file with an example:**
<br>
_packages/models/src/models/accounts.py_
<br>
_src/hooks/main.py_

## Run an example

```shell
# Fedora:
sudo dnf install gettext
gettext --version
# Ubuntu:
sudo apt install gettext
gettext --version
# Windows:
https://mlocati.github.io/articles/gettext-iconv-windows.html
gettext --version

uv python install

cd project_name
uv sync
uv run python src/hooks/main.py
```
