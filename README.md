# satyambarnwal.com

Personal site for Satyam Barnwal — founder, ZAP Innovations Pvt Ltd.

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

A personal-brand one-pager: hero, about, journey, work, principles, contact.
The ventures (QueZap, Zap Studio, Zap Water, NuraLearn) are listed as context
for the person, not as a company pitch.

## Design

- Type: Archivo variable (restrained widths), IBM Plex Mono for labels
- Colour: white background throughout; black text and orange `#FF4A00` accents only. Single light theme.

## Portrait

`satyam-cut.webp` is the background-removed portrait used in the hero.
`satyam.webp` is the untouched original. `tools-cutout.py` regenerates the
cutout from the original (needs Pillow + numpy):

    python3 tools-cutout.py
