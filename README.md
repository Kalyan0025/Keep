# Keep

A memory app prototype. Drop anything worth keeping (photo, video, voice, note, quote, person, place, file) into one calendar, then ask for it later. Search answers show the original memory, and say so when nothing matches.

Single-file vanilla HTML/CSS/JS. Open `index.html` in a browser.

- `src/app.src.html` is the source, with an `__IMGS__` placeholder.
- `src/sample-images.json` holds the demo photos.
- `python3 build.py` inlines them into `index.html`.

Design: OpenAI apps-sdk-ui tokens (type scale, grays, radii), solid strokes, seasonal mesh gradients with grain.
Demo data is sample content. Search is keyword matching, voice and video recording are simulated unless the browser grants camera and microphone access.

## Reference

- `assets/reference/meta-ai-characters.webp`: Meta AI character lineup (stylized 3D avatars on a city street). Visual reference for people/avatar styling; not used by the build.
