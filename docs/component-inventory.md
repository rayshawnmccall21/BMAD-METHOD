---
title: Component Inventory
---

# Component Inventory

## CLI Layer
- `tools/cli/bmad-cli.js`: CLI entry point and command dispatcher.
- `tools/bmad-npx-wrapper.js`: NPM binary wrapper for `bmad` / `bmad-method`.
- `tools/cli/commands/`: CLI command implementations (install, etc.).
- `tools/cli/lib/`: CLI helpers (file ops, prompts, platform codes, XML/YAML tooling).
- `tools/cli/installers/`: Install flow logic and install messages.

## Content Modules
- `_bmad/`: Packaged module artifacts distributed with the CLI.
- `src/core/`: Core module sources (agents, workflows, tasks).
- `src/modules/`: Module sources (bmm, bmb, sub-modules).

## Documentation System
- `docs/`: Primary markdown content for the documentation site.
- `website/`: Astro + Starlight site, components, and styling.
- `website/src/components/`: Doc site UI components.

## Build and Validation Tooling
- `tools/build-docs.js`: Docs build orchestration.
- `tools/validate-agent-schema.js`: Agent schema validation.
- `tools/validate-doc-links.js`: Documentation link validation.
- `tools/flattener/`: Content aggregation and export tooling.

## Tests
- `test/`: Schema, installation, and CLI integration tests.
