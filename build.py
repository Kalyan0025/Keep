"""Builds index.html from src/app.src.html: inlines sample images, the Re-live (AR) module and three.js."""
r=lambda f:open(f).read()
s=r('src/app.src.html').replace('__IMGS__',r('src/sample-images.json').strip()).replace('__AR_CSS__',r('src/ar.css')).replace('__AR_JS__',r('src/ar.js')).replace('__THREE__',r('src/vendor/three.min.js'))
open('index.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+s+'</body></html>')
