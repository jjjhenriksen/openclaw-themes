#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
for theme in window-seat sleeper-car; do
  for mode in light dark; do
    cwebp -quiet -q 88 "artwork/$theme-$mode.png" -o "assets/$theme-$mode.webp"
  done
done
