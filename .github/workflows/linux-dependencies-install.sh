# #!/bin/bash

# set -e

# # Install sudo on Linux
# apt update
# apt install -y sudo

# # Install OS dependencies
# sudo apt install -y curl gnupg2 systemctl git

# # Install MongoDB server
# curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
#     sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor
# echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] \
#     https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | \
#     sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
# sudo apt update
# sudo apt install -y mongodb-org
# mongod --version
# sudo systemctl start mongod
