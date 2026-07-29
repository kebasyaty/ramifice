# Installation

1. Install MongoDB (if not installed):<br>
   [![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v2/assets/FEDORA_INSTALL_MONGODB.md)
   [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v2/assets/UBUNTU_INSTALL_MONGODB.md)
   [![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.mongodb.com/try/download/community)

2. Install system dependencies:

```shell
# Fedora:
sudo dnf install gettext
# Ubuntu:
sudo apt install gettext
# MacOS
brew install gettext
brew link gettext --force
# Windows:
https://mlocati.github.io/articles/gettext-iconv-windows.html
```

3. Install Ramifice in your project:

```shell
uv add ramifice
```

4. Add `config` and `public` directories in root of your project:<br>
   [Download config directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/config "Download config directory")<br>
   [Download public directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/public "Download public directory")

5. Run

```shell
# Run Development:
uv run python main.py
# Run Production:
uv run python -OOP main.py
```
