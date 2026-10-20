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

The pin button on the camera screen opens a walk-by game. Add the first two weeks to a month of photos (location, and the direction you were facing, are read from each photo's GPS tag; photos taken in Keep record both). Walk toward a place and, within about 40 m, Keep asks you to look for it.

The match is AR, not a drag game: your camera is live and the old photo hangs in the world where it was taken, under clouds. Turn and tilt the phone (compass and motion sensors) and it slides into view; the clouds clear as you face it. Matching is by heading and tilt plus a light image comparison, not true visual positioning. Without a camera it runs a scripted preview. After a match, "Memory fragments recovered" shows the original photo full-phone with misty edges, then Meta AI avatars appear in the live camera where the people stood (`avatarsFor()` is the plug-in point for real Meta AI avatar generation; today they are drawn on the device). Needs HTTPS, camera and motion permission.

**People-free scenes.** A spot can carry a clean plate (`<key>_clean` in `src/sample-images.json`): the same place with the people taken out. When present, the match screen shows it instead of the original photo, and the Meta AI avatars stand where the people were. Without one, the original photo is used.
