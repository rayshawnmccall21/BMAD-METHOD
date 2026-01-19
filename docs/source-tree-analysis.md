---
title: Source Tree Analysis
---

# Source Tree Analysis

## High-Level Tree (Annotated)

```
project-root/
├── _bmad/                 - Packaged BMad module content (agents, workflows, config)
├── src/                   - Source modules and core assets
├── tools/                 - CLI implementation and build utilities
│   ├── cli/               - CLI commands, installers, and helpers
│   ├── flattener/         - Content flattening and export utilities
│   └── schema/            - Schema validation helpers
├── docs/                  - Documentation content (served by website)
├── website/               - Astro + Starlight site configuration
├── samples/               - Sample custom modules
├── test/                  - Test suites and fixtures
└── .github/               - CI/CD workflows and repo automation
```

## Critical Folders
- `_bmad/`: Packaged runtime assets for the BMad method (agents, workflows, templates).
- `src/`: Source-of-truth content that drives `_bmad/` output.
- `tools/cli/`: CLI entry points, install flows, and platform helpers.
- `tools/flattener/`: Aggregation and export utilities for content and workflows.
- `docs/`: Primary documentation content, used directly by the docs site.
- `website/`: Astro site configuration and theme components.
- `test/`: Schema, installation, and integration checks.

## Entry Points and Key Paths
- CLI main: `tools/cli/bmad-cli.js`
- NPM bin wrapper: `tools/bmad-npx-wrapper.js`
- Docs site config: `website/astro.config.mjs`
- Docs content root: `docs/index.md`
