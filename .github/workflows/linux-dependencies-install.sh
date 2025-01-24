#!/bin/bash

set -e

apt update

# Install OS dependencies
apt install -y curl gnupg2 systemctl git

# Install MongoDB server
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] \
   https://repo.mongodb.org/apt/debian bookworm/mongodb-org/8.0 main" | \
   tee /etc/apt/sources.list.d/mongodb-org-8.0.listapt update
apt install -y mongodb-org
mongod --version
systemctl start mongod
