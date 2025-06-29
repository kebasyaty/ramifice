# dynamic_choices

**An example of using selective field types with dynamic elements.**
<br>
<br>
**Path to file with an example:**

- _packages/models/src/models/goods.py_
- _src/dynamic_choices/main.py_

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

# Install UV:
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Checking installed version:
uv --version

# Install the latest version of Python:
uv python install

# Go to the directory with an example:
cd dynamic_choices
# Run:
uv sync
uv run python src/dynamic_choices/main.py
```
