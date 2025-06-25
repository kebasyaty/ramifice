# hooks

**Hooks - Methods that are called at different stages when accessing the database.**
<br>
( for a general presentation, how to use hooks methods )
<br>
<br>
**Path to file with an example:**
<br>
packages\models\src\models\accounts.py
<br>
src\hooks\main.py

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
