# Localization

## How to create custom translations ?

```python
from ramifice import translations

translations.add_languages(
    default_locale="en",  # For Ramifice by default = "en"
    languages=frozenset(("en", "ru")),  # For Ramifice by default = ["en", "ru"]
)
```

```shell
cd project_name
# Add your custom translations:
uv run pybabel extract -o config/translations/custom.pot src
uv run pybabel init -i config/translations/custom.pot -d config/translations/custom -l en
uv run pybabel init -i config/translations/custom.pot -d config/translations/custom -l ru
...
# Hint: Do not forget to add translations for new languages.
uv run pybabel compile -d config/translations/custom

# Update your custom translations:
uv run pybabel extract -o config/translations/custom.pot src
uv run pybabel update -i config/translations/custom.pot -d config/translations/custom
# Hint: Do not forget to check the translations for existing languages.
uv run pybabel compile -d config/translations/custom
```

## How to add new languages ​​to Ramifice ?

```python
from ramifice import translations

translations.add_languages(
    default_locale="en",  # For Ramifice by default = "en"
    languages=frozenset(("en", "ru", "de", "de_ch")),  # For Ramifice by default = ["en", "ru"]
)
```

```shell
cd project_name
# Example:
uv run pybabel init -i config/translations/ramifice.pot -d config/translations/ramifice -l de
uv run pybabel init -i config/translations/ramifice.pot -d config/translations/ramifice -l de_ch
...
# Hint: Do not forget to add translations for new languages.
uv run pybabel compile -d config/translations/ramifice

# Update translations to Ramifice:
uv run pybabel extract -o config/translations/ramifice.pot ramifice
uv run pybabel update -i config/translations/ramifice.pot -d config/translations/ramifice
# Hint: Do not forget to check the translations for existing languages.
uv run pybabel compile -d config/translations/ramifice
```
