---
title: Architecture
---

# Architecture

## Executive Summary
BMad Method is delivered as a Node.js CLI that installs and orchestrates a large library of agents and workflows. The repository also hosts the documentation site (Astro + Starlight) with content stored in `docs/`. The architecture emphasizes file-based content, modular workflows, and strong tooling for validation and bundling.

## Technology Stack
| Category | Technology | Notes |
| --- | --- | --- |
| Runtime | Node.js (>= 20) | CLI and tooling runtime |
| Language | JavaScript (ESM) | Repository primary language |
| CLI | commander, @clack/prompts | Command routing and interactive prompts |
| Docs | Astro + Starlight | Static site for documentation |
| Validation | ESLint, Prettier, markdownlint | Code and docs quality gates |
| Testing | Jest, c8 | Schema and installation tests |

## Architecture Pattern
- Modular CLI orchestrator with a file-based content registry.
- Module content packaged under `_bmad/` with source-of-truth in `src/`.
- Documentation served from `docs/` via `website/` configuration.

## Data Architecture
- Predominantly file-based data: Markdown, YAML, JSON, CSV, and XML.
- Content is bundled and validated via tooling under `tools/`.
- No external database required for core operation.

## API Design
- Primary interface is the CLI with local file operations.
- No network API surface detected in the core runtime.

## Component Overview
- CLI core: `tools/cli/` (commands, installers, helpers).
- Content modules: `_bmad/` and `src/modules/`.
- Docs site: `website/` with content from `docs/`.
- Build and validation tooling: `tools/`.
- Tests: `test/`.

## Source Tree
See `docs/source-tree-analysis.md` for the annotated structure.

## Development Workflow
- Install dependencies with `npm install`.
- CLI and docs workflows are driven by `package.json` scripts.
- Validation uses ESLint, Prettier, markdownlint, and schema checks.

## Deployment Architecture
- NPM package distribution for the CLI.
- GitHub Actions for release automation and docs publishing.
- Astro build artifacts for the documentation site.

## Testing Strategy
- Schema and installation tests under `test/`.
- `npm run test` aggregates schema checks, install tests, and linting.
