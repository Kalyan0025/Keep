"""Builds index.html from src/app.src.html by inlining the sample images."""
s=open('src/app.src.html').read().replace('__IMGS__',open('src/sample-images.json').read().strip())
open('index.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+s+'</body></html>')
