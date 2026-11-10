# Christmas Themes

Five festive OpenClaw Control UI themes, each with light and dark palettes and matching static backgrounds.

- **Holly & Hearth:** evergreen, cranberry, ivory, garlands and presents.
- **Silent Night:** midnight blue, silver and a snowy village.
- **Sugarplum:** plum, rose, ornaments and candy canes.
- **Gingerbread:** cocoa, icing and a warmly lit three-house village.
- **Delivering the Cheer:** a complete gift train, snowy station and layered forest.

## Use

Requires OpenClaw 2026.11.1 or newer. Install through OpenClaw's managed ClawHub plugin flow, review its requested access, then enable the plugin. Choose a Christmas theme in **Settings → Appearance**. Select theme artwork under **Appearance → Background**; visibility and placement remain viewer-controlled. Each theme supports light, dark and system preferences.

Theme IDs use `christmas-themes/<slug>`. Backgrounds are static, not animated. Original editable SVGs are included in `artwork/`; PNG backgrounds and the compact SVG evergreen mark live in `assets/`.

## Validation and limitations

All 10 palettes pass 100 text-color contrast checks (minimum 4.5:1), plus focus-ring checks. All 10 PNG backgrounds pass signature, dimension and file-size validation. These token tests do not guarantee contrast over every artwork pixel.

Train and gingerbread compositions were previewed temporarily in the real Control UI at 1440×1000 and 1100×900, in both modes. These were browser-only appearance previews, not end-to-end installed-plugin tests. Portrait/mobile crops remain unverified. Cover sizing can crop artwork at other aspect ratios; dark variants show more scenery through the UI readability overlay.

The runtime entry registers nothing: no tools, network calls, credentials or configuration options. Theme discovery uses the static manifest. This release has no install/build lifecycle scripts or runtime dependencies.

Host managed installation has not yet been verified: the local authoring packer rejected the plain static entry for missing tool/feature authoring metadata. No fabricated metadata or trust bypass is included. Registry validation/publication is separate from host activation.

Documentation: https://docs.openclaw.ai/tools/theme and https://docs.openclaw.ai/plugins/manifest/surfaces#themes
