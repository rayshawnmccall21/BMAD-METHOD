---
title: Development Guide
---

# Development Guide

## Prerequisites
- Node.js >= 20 (repo uses `.nvmrc` set to 22).
- npm (lockfile included).

## Install Dependencies
```bash
npm install
```

## Common Commands

### CLI Workflows
```bash
# Run the installer
npm run bmad:install

# Alternative installer entry
npm run install:bmad
```

### Documentation Site
```bash
npm run docs:dev
npm run docs:build
npm run docs:preview
```

### Bundling and Packaging
```bash
npm run bundle
npm run rebundle
```

### Linting and Formatting
```bash
npm run lint
npm run lint:md
npm run format:check
npm run format:fix
```

### Tests and Validation
```bash
npm run test
npm run test:schemas
npm run test:install
npm run validate:schemas
```

## Key Entry Points
- CLI main: `tools/cli/bmad-cli.js`
- NPM bin wrapper: `tools/bmad-npx-wrapper.js`
- Docs site config: `website/astro.config.mjs`

## Notes
- Docs content is served from `docs/` via the symlink setup in `website/src/content/`.
