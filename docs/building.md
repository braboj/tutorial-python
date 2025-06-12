# Building the Site

This project uses [MkDocs](https://www.mkdocs.org/) to build the static documentation site. After installing the 
dependencies, generate a `nav.yml` file containing the navigation mapping and then run:

```bash
python .scripts/update_mkdocs_nav.py --nav-file nav.yml

mkdocs build -f mkdocs.yml -f nav.yml
```

The generated HTML will be placed inside the `site/` directory.

You can preview the documentation locally with:

```bash
mkdocs serve
```

## Using Hugo

If you prefer [Hugo](https://gohugo.io/) for static site generation, create a
menu configuration based on the `docs/` directory with:

```bash
python .scripts/generate_hugo_menu.py --docs-dir docs --output hugo_menu.yml
```

Run Hugo with both configuration files to merge the generated menu with the
main settings:

```bash
hugo --config config.yaml,hugo_menu.yml
```

The `hugo_menu.yml` file mirrors the documentation structure and must be
included so the navigation is rendered correctly.

This script requires the `pyyaml` package which is already listed in
`requirements.txt`.

