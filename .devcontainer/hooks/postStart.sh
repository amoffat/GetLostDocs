#!/usr/bin/env bash
set -eux

nohup bash -c 'mkdocs serve &' >/dev/null 2>&1