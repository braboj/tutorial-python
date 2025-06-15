## File Naming

* Snake-case for all files and folders (e.g., `my_file.py`, `my_folder`)

## Commit Messages

```
[optional issue id]: <description>

[optional body]

[optional footer(s)]
```

**Examples**:
```
* [`#19`] - Add the operator precedence examples
* [`#####`] - Move the image assets to a dedicated folder
```

[//]: # (## Pull Requests)

[//]: # ()
[//]: # (- https://blog.montrealanalytics.com/4-tips-for-effective-pull-request-naming-f60793998f04])


## Building the MkDocs Site

Follow these steps to generate the static documentation using MkDocs.

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Build the site:
   ```bash
   mkdocs build
   ```
   The generated files will appear in the `site/` directory.
3. To preview the documentation locally, run:
   ```bash
   mkdocs serve
   ```

Navigation is created automatically by the `mkdocs-awesome-pages-plugin` based on
files inside the `docs/` folder.
