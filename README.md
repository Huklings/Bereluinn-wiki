# Bereluinn wiki

The public wiki for the world of Bereluinn, built with [Quartz](https://quartz.jzhao.xyz) and published at <https://huklings.github.io/Bereluinn-wiki/>.

## How it works

- Notes live in `content/`. Every push to `main` builds the site and deploys it to GitHub Pages (`.github/workflows/deploy.yml`).
- Wikilinks, embeds, callouts, tags, backlinks, graph view and search all work like in Obsidian.

## Keeping secrets out

This repository is **public**. Anything pushed here can be read on GitHub, even if the site doesn't show it.

- Only put notes in `content/` that are meant for players and readers.
- Site-level guards, in case something slips in: notes with `draft: true` in their frontmatter, folders named `GM`, `private` or `templates`, and `%% Obsidian comments %%` are left out of the built site. Only images that a published note uses are copied.
- These guards hide things from the *site*, not from the *repository*. Keep GM notes out of `content/` entirely.

## Preview locally

```bash
npm ci
npx quartz plugin install
npx quartz build --serve
```

Then open http://localhost:8080.
