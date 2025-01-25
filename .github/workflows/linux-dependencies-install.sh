#!/bin/bash

set -e

apt update

# Install OS dependencies
apt install -y curl gnupg2 systemctl git

# Run MongoDB server
mongod --version
systemctl status mongod --no-pager -l
systemctl start mongod
