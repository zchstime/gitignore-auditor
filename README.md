<p align="center"><img src="assets/banner.svg" alt="Gitignore Auditor" width="100%"></p>

# Gitignore Auditor

> Find tracked secrets, build artifacts, and missing ignore rules before they leak.

[![CI](https://github.com/zchstime/gitignore-auditor/actions/workflows/ci.yml/badge.svg)](https://github.com/zchstime/gitignore-auditor/actions/workflows/ci.yml) [![Python](https://img.shields.io/badge/python-3.11%2B-3776AB)](pyproject.toml) [![Dependencies](https://img.shields.io/badge/runtime_dependencies-0-16a34a)](pyproject.toml) [![MIT](https://img.shields.io/badge/license-MIT-f59e0b)](LICENSE)

Gitignore Auditor is a compact, privacy-friendly command-line utility built around one recurring workflow. It runs without an account or API key, keeps its decisions inspectable, and produces portable output you can use immediately.

## Why it is useful

Find tracked secrets, build artifacts, and missing ignore rules before they leak. Instead of hiding simple analysis behind a hosted service, it keeps data local and shows the evidence behind every recommendation.

## Highlights

- Tracked-risk pattern detection
- Missing ignore recommendation
- Language-aware artifact rules
- No file mutation by default
- Zero third-party runtime dependencies

## Quick start

```bash
git clone https://github.com/zchstime/gitignore-auditor.git
cd gitignore-auditor
python -m pip install -e .

gitignore-audit .
```

Use the synthetic [`examples/`](examples/) data for a safe first run. Run `gitignore-audit --help` for the complete command reference.

## Design

```text
local input → deterministic analysis → cited findings → portable report
```

The default workflow performs no network requests and does not silently modify source data. The implementation is deliberately small enough to audit, teach from, and extend.

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

GitHub Actions tests Python 3.11, 3.12, and 3.13.

## Roadmap

- Additional import and export formats
- More community-provided edge-case fixtures
- Stable machine-readable report schemas
- Optional plugin hooks while keeping the core dependency-free

If this tool saves you time, **star the repository** and share the workflow you want next. Contributions are welcome—start with the open `good first issue`.

## Community and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md). Never put private data or real credentials in an issue.

## License

[MIT](LICENSE) © 2026 zchstime
