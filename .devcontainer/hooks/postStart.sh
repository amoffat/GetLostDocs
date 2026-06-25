#!/usr/bin/env bash
set -eux

nohup bash -c 'uv run mkdocs serve &' >/dev/null 2>&1