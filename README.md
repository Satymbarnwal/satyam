# satyambarnwal.com

Personal site for Satyam Barnwal — founder & CEO, ZAP Innovations Pvt Ltd.

Single static page, no build step. `index.html` contains all markup, CSS and JS;
fonts load from Google Fonts.

## Run locally

    python3 -m http.server 8000

Then open http://localhost:8000

## Deploy

Any static host works (GitHub Pages, Netlify, Vercel, Cloudflare Pages).
For GitHub Pages, add a `CNAME` file containing `satyambarnwal.com` and point
the domain's DNS at GitHub.

## Design

- Type: Bricolage Grotesque (display), Archivo (body), IBM Plex Mono (labels)
- Colour: ultramarine `#1E3FD8` on blue-biased neutrals; full light and dark themes
