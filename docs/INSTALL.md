# Install and preview

Read [DESIGN_BRIEF.md](DESIGN_BRIEF.md) for the assignment and [ASSETS.md](ASSETS.md)
for approved references. All starter files and technical choices can evolve with the website.

## Install

Use Bash and an existing Python 3.12 installation on macOS. From the repository directory:

```bash
bash
source source_me.sh && python3 --version
source source_me.sh && python3 -m pip install -r pip_requirements.txt
```

If Python 3.12 is missing, install it with `brew install python@3.12` and put its commands
on this Bash session's path:

```bash
export PATH="$(brew --prefix python@3.12)/libexec/bin:$PATH"
source source_me.sh && python3 --version
```

If the interpreter rejects package installation as externally managed, use a local virtual
environment as a last resort. Source the repository environment first, then activate it:

```bash
source source_me.sh && python3 -m venv .venv
source source_me.sh && source .venv/bin/activate && python3 -m pip install -r pip_requirements.txt
```

For subsequent commands in that case, activate `.venv` after sourcing `source_me.sh`.
The startup script optionally reads your own Bash configuration; no other checkout or
machine-specific Python path is required. Check the reported interpreter if your Bash
configuration changes PATH.

## Preview and build

```bash
source source_me.sh && python3 -m mkdocs serve --strict
```

Open [the local preview](http://127.0.0.1:8000/nilbc-web/). Stop the server with Ctrl-C.

```bash
source source_me.sh && python3 -m mkdocs build --strict
```

The starter reads [mkdocs.yml](../mkdocs.yml), renders [site_src/index.md](../site_src/index.md),
and writes the ignored `output_site/` directory. Maintainer documents and source presentation files
are outside the published content. The default Material theme is an operational placeholder.

## GitHub Pages compatibility

The starter's `site_url` is `https://vosslab.github.io/nilbc-web/`; change it to the actual
publication URL when needed. MkDocs uses its path for the local preview too. The built
directory is a static site suitable for a GitHub Pages artifact; this starter does not
publish anything or require hosting credentials.

Upload the built site directory when configuring deployment, not the source repository.
See the [MkDocs configuration documentation](https://www.mkdocs.org/user-guide/configuration/)
and [GitHub Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Repository checks

The inherited maintainer suite has extra dependencies, separate from website installation:

```bash
source source_me.sh && python3 -m pip install -r pip_requirements-dev.txt
source source_me.sh && python3 -m pytest tests/
```

An extracted source archive omits Git history. If running the inherited repository checks
from such a copy, initialize its own local repository first with `git init`; the checks
locate their root through Git. Website installation and preview do not require Git metadata.

For the suite's scope, see [tests/TESTS_README.md](../tests/TESTS_README.md).
Document the commands and checks appropriate to your completed website.
