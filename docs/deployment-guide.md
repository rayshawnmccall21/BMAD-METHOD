---
title: Deployment Guide
---

# Deployment Guide

## CI/CD Overview
The repository uses GitHub Actions workflows under `.github/workflows/` to run checks, package bundles, and publish releases.

Key workflows:
- `quality.yaml`: Linting and validation checks.
- `docs.yaml`: Documentation build/publish pipeline.
- `bundle-latest.yaml`: Bundle artifacts for distribution.
- `manual-release.yaml`: Release pipeline triggered by maintainers.
- `discord.yaml`: Notifications and community automation.

## Documentation Site
- Site source: `website/` (Astro + Starlight).
- Content source: `docs/`.
- Static assets: `website/public/`.
- Custom domain: `CNAME` at repo root.

## NPM Publishing
- Release commands in `package.json` trigger GitHub Actions workflows:
  - `npm run release:major`
  - `npm run release:minor`
  - `npm run release:patch`

## Bundling
- Use `npm run bundle` to generate distribution bundles.
- Use `npm run rebundle` to refresh existing bundles.
