# fixtures

**An example of using Fixtures.**
<br>
**Fixtures:** To populate the database with pre-created data.
<br>
**config/fixtures** - Directory for creating fixtures.
<br>
<br>
**Path to file with an example:**
<br>
_packages/models/src/models/site.py_
<br>
_config/fixtures/SiteParameters.yml_
<br>
_src/fixtures/main.py_

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
uv run python src/fixtures/main.py
```
