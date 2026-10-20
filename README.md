# Keep

A memory app prototype. Drop anything worth keeping (photo, video, voice, note, quote, person, place, file) into one calendar, then ask for it later. Search answers show the original memory, and say so when nothing matches.

Single-file vanilla HTML/CSS/JS. Open `index.html` in a browser.

- `src/app.src.html` is the source, with an `__IMGS__` placeholder.
- `src/sample-images.json` holds the demo photos.
- `python3 build.py` inlines them, and the DialKit stylesheet, into `index.html`.

Prototyping dials: a [DialKit](https://github.com/joshpuckett/dialkit) panel (MIT, `vendor/dialkit/`) opens beside the phone on wide windows and shows as a small round button on narrow ones. Its Transition folder picks how memories move when you swipe (fade & scale, blur, slide, cover flow, stack, parallax, zoom out), edits the motion curve with DialKit's easing and spring editor (used for swipes, caption fade-ins and sheets), sets fade, scale, blur, tilt and parallax strength, and has Play demo, Previous and Next buttons; changing a transition dial previews it on Jun 22. Other folders tune memory photo size, margins and edge fade, viewfinder radius, shutter size, accent, page colour and the seasonal wash. Values persist in the browser; `window.keepDials` exposes the controller. The script loads from jsDelivr (`dialkit@2.0.2`) and falls back to `vendor/dialkit/browser.global.js` when that fails, so serving the repo locally works offline: `python3 -m http.server 8000`, then open http://localhost:8000. The vendored files are built from [joshpuckett/dialkit](https://github.com/joshpuckett/dialkit) (commit in `vendor/dialkit/VERSION`); `sh vendor/dialkit/update.sh [ref]` rebuilds them from the repo.

Design: the Keep for Meta design system by default (Meta-style greys, one blue for the primary action, pill controls, Optimistic with Figtree as the fallback, and a blue-to-pink AI gradient used only on Meta AI moments: the Ask bar while in use, today's ring, the voice orb, the Keep mark). The original look, built on OpenAI apps-sdk-ui tokens with seasonal mesh gradients, is one switch away in the DialKit panel (Look > Design system). Both are token layers in `src/app.src.html`, switched by `data-ds` on the root element.
Demo data is sample content. Search is keyword matching, voice and video recording are simulated unless the browser grants camera and microphone access.

## Open it on your phone (live camera and mic)

The camera and microphone only work on a page served over HTTPS, not inside an embedded viewer. `.github/workflows/pages.yml` publishes `index.html` to GitHub Pages. One-time setup: repo **Settings → Pages → Source: GitHub Actions**, then run the workflow (Actions → Deploy Keep to GitHub Pages → Run workflow). The page is at `https://<owner>.github.io/Keep/`.

## First weeks (prototype)

The pin button on the camera screen opens a walk-by game: add the first two weeks to a month of photos (location read from each photo's GPS tag), then walk toward a place. Within about 40 m Keep asks you to find the spot, with a cloudy ghost of the old photo over the camera that clears as the view lines up. With no camera it falls back to a drag-to-align practice view, and the walk can be simulated with a slider. The Meta AI step (`metaRecreate`) is an on-device style preview, the plug-in point for real avatar image generation.
