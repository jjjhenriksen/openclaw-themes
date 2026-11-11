# Travel Themes · 0.1.0

A scenic companion pack for Travel Copilot, usable with any OpenClaw agent. Installing a theme does not install or modify Travel Copilot.

- **Window Seat** — ivory and sky-blue sunrise above a coast; navy and amber on a night flight.
- **Sleeper Car** — cream and forest-green countryside daylight; espresso, brass lamps and an overnight carriage.

Both themes include full light/dark semantic palettes and original AI-generated backgrounds. The scenic detail sits at the right edge, leaving a quieter reading area. The plugin preserves OpenClaw's layout and product identity. No tools, credentials, services, network access or runtime dependencies are registered.

## Use

Declared baseline: OpenClaw 2026.11.1. Install/enable only through the managed plugin workflow, then select `travel-themes/window-seat` or `travel-themes/sleeper-car` under Settings → Appearance. Select the matching theme artwork under Background. Background visibility and placement remain viewer-controlled. No installation, enablement, theme selection or template changes are performed by this source package.

## Development

`npm test` checks complete palette tokens, manifest/definition consistency, definition and icon limits, 40 text-contrast pairs (minimum 4.5:1), focus-ring contrast, and shipped WebP signatures/dimensions/size limits. `npm pack --dry-run` audits distribution contents. Original PNG masters are in `artwork/`; only compressed WebP backgrounds ship. Run `sh scripts/render-backgrounds.sh` to regenerate WebPs with `cwebp`.

## Validation and limitations

Palette tests, host definition normalization, package inspection and artwork visual review are development checks—not installed-plugin validation. Live Control UI rendering, composited text contrast and mobile crops are not yet verified. Static cover sizing may crop the right-hand scenery on narrow or unusually wide viewports. UI opacity/scrim settings will make artwork quieter than the concept mockups. No custom layout or persistent window frame is implemented.

See `artwork/PROVENANCE.md` for asset origins and generation prompts. Concept mockups are not real UI screenshots.

Status: local development pack, not installed or published.
