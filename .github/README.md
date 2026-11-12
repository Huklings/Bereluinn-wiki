# Bereluinn wiki

This repository is an Obsidian vault for the world of Bereluinn. Every push to `main` builds it into a wiki with [Quartz](https://quartz.jzhao.xyz) and publishes it at <https://huklings.github.io/Bereluinn-wiki/>.

## Layout

- The notes themselves are at the root of the repo, exactly as they are in the vault.
- `.quartz-site/` holds the Quartz settings (`quartz.config.yaml`) and its pinned dependencies. Obsidian hides dot-folders, so it doesn't clutter the vault.
- `.github/workflows/deploy.yml` checks out Quartz at a pinned commit, applies those settings and builds the vault.

## What stays private

The repo is **public**. Anything pushed here can be read on GitHub, even if the site doesn't show it.

- `.gitignore` keeps `meta/`, `card pulls/`, `templates/`, `GM/`, `private/` and `.obsidian/` on your computer. They are never pushed.
- As a second guard, Quartz also skips those folders, notes with `draft: true` in their properties, and `%% comments %%`. Only images that a published note uses are copied to the site.
- `%% comments %%` and `draft: true` notes are still readable in the repo. Put real secrets in an excluded folder.

## The home page

The site's front page is the note called `index` at the vault root.
