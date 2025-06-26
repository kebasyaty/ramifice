# files

**An example of using fields for files and images.**
<br>
<br>
**Path to file with an example:**
<br>
_packages/models/src/models/accounts.py_
<br>
_src/files/main.py_

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
uv run python src/files/main.py
```
