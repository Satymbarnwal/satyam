# satyambarnwal.com

Personal site for Satyam Barnwal — founder & CEO, ZAP Innovations Pvt Ltd.

Single static page, no build step. `index.html` holds all markup, CSS and JS;
fonts come from Google Fonts and `satyam.webp` is the portrait.

## Run locally

    python3 -m http.server 8000

Then open http://localhost:8000

## Deploy

Any static host works (GitHub Pages, Netlify, Vercel, Cloudflare Pages).
For GitHub Pages, add a `CNAME` file containing `satyambarnwal.com` and point
the domain's DNS at GitHub.

## Content

Sourced from zapinnovations.in: four sectors (QueZap, Zap Water, NuraLearn,
Zap Studio), the Zap Studio service list, and the shared QueZap/Zap Water
ecosystem.

## Design

- Type: Archivo variable (width + weight axes), IBM Plex Mono for labels
- Colour: white, black, and orange `#FF4A00` only; full light and dark themes

## Portrait

`satyam-cut.webp` is the background-removed portrait used in the hero.
`satyam.webp` is the untouched original. `tools-cutout.py` regenerates the
cutout from the original (needs Pillow + numpy):

    python3 tools-cutout.py
