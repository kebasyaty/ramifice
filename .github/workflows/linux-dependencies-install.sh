#!/bin/bash

set -e

apt update

# Install OS dependencies
apt install -y curl gnupg2 systemctl git

# Run MongoDB server
mongod --version
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
