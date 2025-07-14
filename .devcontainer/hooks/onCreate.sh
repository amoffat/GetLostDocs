#!/usr/bin/env bash
set -eux

# Needed for mkdocs-material imaging
sudo apt-get update
sudo apt-get install --yes libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev

pip install -r requirements.txt