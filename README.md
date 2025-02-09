# GetLostDocs

The dev documentation for the Get Lost game. Intended for creators that want to contribute levels to the game.

https://docs.getlost.gg

## Developing docs locally

The instructions below are only if you want to edit this documentation. It is not necessary to do these steps if you just want to build levels.

- Create a python virtual env and activate it
- Install deps with `pip install -r requirements.txt`
- Start the dev server with `mkdocs serve` to serve the current version, or `mike serve` to serve all versions with the version dropdown.
- Make changes to markdown files

### Fixing a specific version of the docs

- Find the commit on the `main` branch where the change applies to that version
- Create a new branch with `git checkout -b $branch_name $commit_hash`
- Make changes to the markdown files
- Commit changes
- `git checkout main`
- Incorporate the change into `main`'s history with `git rebase $branch_name`
- Rebuild the `gh-pages` branch at that version with `mike deploy --push $version`
- Sync remote `git push origin HEAD`
