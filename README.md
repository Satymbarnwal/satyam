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

- Type: Archivo variable (width + weight axes), IBM Plex Mono for labels
- Colour: white, black, and orange `#FF4A00` only; full light and dark themes
