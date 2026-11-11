# Artemis Canopy

An OpenClaw dark theme inspired by [Artemis Lost](https://github.com/jjjhenriksen/Artemis-Lost) with a distinct graphite-and-cyan mission-console palette, amber secondary accents, and monospace typography.

## Use

Install this plugin from ClawHub, enable it, then choose **Settings → Appearance → Artemis Canopy** in dark mode. Theme catalog ID: `artemis-canopy-theme/canopy-dark`.

This release supplies native semantic theme colors and font preferences, not the custom layout or decorative telemetry of a concept mockup. Cyan highlights primary actions, theme-aware links, interaction text, and focus rings. Amber marks secondary control text; graphite-blue surfaces replace the former green tint. Error colors remain reserved for destructive actions. It does not change your selected theme automatically. JetBrains Mono is used only if already installed; no external font requests are made.

## Privacy

No dependencies, tools, hooks, network requests, configuration changes, or filesystem access. The JavaScript entrypoint is a no-op; theme data is static JSON.

## Palette revision · 1.0.3

Graphite and cyan deliberately distinguish this theme from Sacred Harp 2025’s pine-and-gold palette. The gallery is a palette study, not a receiving-host screenshot. Run `npm test` for semantic color, contrast, manifest, and no-op entrypoint checks. Registry installation may still serve an earlier release until this revision is published.
