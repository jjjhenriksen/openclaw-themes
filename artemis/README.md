# Artemis Canopy

A green-glow terminal theme inspired by [Artemis Lost](https://github.com/jjjhenriksen/Artemis-Lost).

## Version 1.2.0 — Binary Canopy
Deep green-black panels, luminous sage controls, restrained gold secondary text, and softly blurred binary columns. The center stays quieter for reading; the edges carry the atmosphere.

The original terminal palette and monospace font preference are retained. Share Tech Mono is used when installed, with system monospace fallbacks. Existing viewer font overrides take precedence.

The backdrop is an original **static WebP**, not a falling animation. No continuous motion, flicker, remote fonts, external artwork or executable decoration. OpenClaw owns placement and contrast-preserving image dimming; appearance varies with background visibility settings and viewport.

## Use
Install or update this plugin through ClawHub, then select **Settings → Appearance → Artemis Canopy**, dark mode. Theme ID: `artemis-canopy-theme/canopy-dark`.

## Privacy and packaging
No runtime dependencies, tools, hooks, network requests or filesystem access. The compiled JavaScript entrypoint is a no-op. The developer-only Pillow artwork generator in `scripts/` is excluded from the distributed package.

The binary design was approved from a browser preview; the published artwork uses the supported native theme background slot, not the preview's injected overlay.
