# Building the Site

This project uses [MkDocs](https://www.mkdocs.org/) to build the static documentation site. After installing the dependencies, generate the navigation YAML and then run:

```bash
python .scripts/update_mkdocs_nav.py --nav-file nav.yml

mkdocs build -f mkdocs.yml -f nav.yml
```

The generated HTML will be placed inside the `site/` directory.

You can preview the documentation locally with:

```bash
mkdocs serve
```

