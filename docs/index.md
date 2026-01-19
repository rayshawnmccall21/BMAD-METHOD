---
title: Project Documentation Index
---

# Project Documentation Index

## Project Overview
- Type: monolith (single-part repository)
- Primary Language: JavaScript (Node.js)
- Architecture: modular CLI + file-based content + static docs site

This index is the primary entry point for AI-assisted development and brownfield planning.

## Quick Reference
- Tech Stack: Node.js, commander, Astro, ESLint, Prettier, Jest
- CLI Entry Points: `tools/cli/bmad-cli.js`, `tools/bmad-npx-wrapper.js`
- Docs Site: `website/` with content from `docs/`

## Generated Documentation
- [Project Overview](./project-overview.md)
- [Architecture](./architecture.md)
- [Source Tree Analysis](./source-tree-analysis.md)
- [Component Inventory](./component-inventory.md)
- [Development Guide](./development-guide.md)
- [Deployment Guide](./deployment-guide.md)
- [Contribution Guide](./contribution-guide.md)

## Existing Documentation
- [README](../README.md) - Project overview and quick start
- [CHANGELOG](../CHANGELOG.md) - Release history
- [CONTRIBUTING](../CONTRIBUTING.md) - Contribution guidelines
- [SECURITY](../SECURITY.md) - Security policy
- [Docs Style Guide](./_STYLE_GUIDE.md)
- [Workflow Diagrams](./_README_WORKFLOW_DIAGRAMS.md)
- [Docs Home: Explanation](./explanation/index.md)
- [Docs Home: How-To Guides](./how-to/index.md)
- [Docs Home: Reference](./reference/index.md)
- [Docs Home: Tutorials](./tutorials/getting-started/getting-started-bmadv6.md)
- [CLI README](../tools/cli/README.md)
- [Tools Docs](../tools/docs/index.md)
- [Docs Site README](../website/README.md)

## Getting Started
1. Install dependencies: `npm install`
2. Run the CLI installer: `npx bmad-method@alpha install`
3. Initialize a workflow: `*workflow-init`
4. For docs development: `npm run docs:dev`
