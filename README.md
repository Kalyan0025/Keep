# Keep

A memory app prototype. Drop anything worth keeping (photo, video, voice, note, quote, person, place, file) into one calendar, then ask for it later. Search answers show the original memory, and say so when nothing matches.

Single-file vanilla HTML/CSS/JS. Open `index.html` in a browser.

- `src/app.src.html` is the source, with an `__IMGS__` placeholder.
- `src/sample-images.json` holds the demo photos.
- `src/ar.js` and `src/ar.css` are the Re-live (3D avatar) feature; `src/vendor/three.min.js` is three.js r160.
- `python3 build.py` inlines all of it into `index.html`.

Design: OpenAI apps-sdk-ui tokens (type scale, grays, radii), solid strokes, seasonal mesh gradients with grain.
Demo data is sample content. Search is keyword matching, voice and video recording are simulated unless the browser grants camera and microphone access.

## Re-live: the person who isn't there any more

Tag a photo with who is in it, their pose (sit, stand, wave, walk) and the spot where they were (tap the photo). Later, tap the cube icon in the header and point the camera at the same place:

- The camera frame is compared with your tagged photos (16x16 gradient hash plus coarse colour). On a match, a 3D avatar of that person appears in the same pose at the same spot.
- Drag to turn the avatar; on a phone, tilting pans the view around it (rotation only).
- A glass card on the left lists every journal kept about that memory (same day, linked, or naming the person). Add a line to it, or tap the shutter to keep the scene with the avatar as a new photo linked to the memory.
- No camera, or standing somewhere else: pick a memory from the chips and the stored photo stands in for the scene. "See Jake there" on a day does the same.

Limits: the avatar is generated from the name (skin, hair, jacket), not from the real person, and the pose and spot are what you tagged, not detected. Matching is a fingerprint, so it needs a similar view of the same place; it does not track you as you walk (that needs ARKit/ARCore or WebXR). Journals are matched by day, link and name.

## Reference

- `assets/reference/meta-ai-characters.webp`: Meta AI character lineup (stylized 3D avatars on a city street). Visual reference for people/avatar styling; not used by the build.
