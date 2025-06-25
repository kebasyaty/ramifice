# basic

**A simple example to start using.**
<br>
<br>
**Path to file with an example:**
<br>
packages\models\src\models\accounts.py
src\basic\main.py

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
uv run python src/basic/main.py
```
