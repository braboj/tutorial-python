# Listing installed packages
# -----------------------------------------------------------------------------
# This example prints all installed distributions using ``pkg_resources`` from
# ``setuptools``. It can help inspect the current Python environment.

import pkg_resources

for dist in sorted(pkg_resources.working_set, key=lambda d: d.project_name.lower()):
    print(f"{dist.project_name}=={dist.version}")
