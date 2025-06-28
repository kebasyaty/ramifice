# fixtures

**An example of using Fixtures.**
<br>
**Fixtures:** To populate the database with pre-created data.
<br>
**config/fixtures** - Directory for creating fixtures.
<br>
<br>
**Path to file with an example:**

- _packages/models/src/models/site.py_
- _config/fixtures/SiteParameters.yml_
- _src/fixtures/main.py_

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
cd fixtures
# Run:
uv sync
uv run python src/fixtures/main.py
```
