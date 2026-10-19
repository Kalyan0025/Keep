# Keep

A memory app prototype. Drop anything worth keeping (photo, video, voice, note, quote, person, place, file) into one calendar, then ask for it later. Search answers show the original memory, and say so when nothing matches.

Single-file vanilla HTML/CSS/JS. Open `index.html` in a browser.

- `src/app.src.html` is the source, with an `__IMGS__` placeholder.
- `src/sample-images.json` holds the demo photos.
- `python3 build.py` inlines them, and the DialKit stylesheet, into `index.html`.

Prototyping dials: on desktop-width windows a [DialKit](https://github.com/joshpuckett/dialkit) panel (MIT, `vendor/dialkit/`) tunes memory photo size, margins, edge fade, neighbour scale and fade, slide speed, viewfinder radius, shutter size, accent, page colour and the seasonal wash. Values persist in the browser; `window.keepDials` exposes the controller. The script loads from jsDelivr (`dialkit@2.0.2`), so the panel needs a network connection; the app works without it.

Design: OpenAI apps-sdk-ui tokens (type scale, grays, radii), solid strokes, seasonal mesh gradients with grain.
Demo data is sample content. Search is keyword matching, voice and video recording are simulated unless the browser grants camera and microphone access.
