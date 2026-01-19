---
title: Project Overview
---

# Project Overview

## Summary
BMad Method is an AI-driven agile development framework packaged as a Node.js CLI with a large library of agents, workflows, and reference content. The repo also hosts the documentation site (Astro + Starlight) that serves content from the top-level `docs/` directory.

## Scope and Capabilities
- CLI installer and workflow runner for the BMad method (`bmad` / `bmad-method`).
- Packaged module content under `_bmad/` and source modules under `src/`.
- Documentation site configuration under `website/` with content sourced from `docs/`.
- Tooling for bundling, validation, linting, and schema checks.

## Repository Structure
- Monolith repository with a single primary part.
- Core content and workflow definitions live in `_bmad/` and `src/`.
- CLI implementation and support tools live in `tools/`.
- Docs content lives in `docs/` and is served by `website/`.

## Technology Stack
| Category | Technology | Version | Notes |
| --- | --- | --- | --- |
| Runtime | Node.js | >= 20 (nvmrc: 22) | CLI and tooling runtime |
| Language | JavaScript (ESM) | N/A | Repository is JS-first |
| CLI Framework | commander | ^14 | Command routing |
| CLI UX | @clack/prompts, chalk, ora, boxen | N/A | Interactive prompts and terminal UX |
| Docs Site | Astro + Starlight | ^5 / ^0.37 | Static docs site |
| Lint/Format | ESLint, Prettier, markdownlint | N/A | Code and docs quality |
| Testing | Jest, c8 | N/A | Schema and installation tests |

## Entry Points
- CLI main: `tools/cli/bmad-cli.js`
- NPM bin wrapper: `tools/bmad-npx-wrapper.js`
- Docs site: `website/astro.config.mjs`

## Related Documentation
- Architecture: `docs/architecture.md`
- Source Tree: `docs/source-tree-analysis.md`
- Development Guide: `docs/development-guide.md`
- Deployment Guide: `docs/deployment-guide.md`
- Component Inventory: `docs/component-inventory.md`
