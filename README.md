# satyambarnwal.com

Personal site for Satyam Barnwal — founder, ZAP Innovations Pvt Ltd.

A single static page, no build step. Everything the site serves lives in
`client/`: `index.html` holds all markup, CSS and JS, fonts come from Google
Fonts, and `satyam-cut.webp` is the portrait.

## Run locally

    python3 -m http.server 8000 --directory client

Then open http://localhost:8000

## Hosting

GitHub Pages, deployed by `.github/workflows/pages.yml` on every push to
`main`. Pages is set to the **GitHub Actions** source, so there is nothing to
configure by hand and no second copy of the site to keep in sync.

- Live: https://satyambarnwal.com
- Fallback: https://satymbarnwal.github.io/satyam/

`client/CNAME` is what points Pages at the custom domain. The DNS records at
the registrar are:

    A     @   185.199.108.153
    A     @   185.199.109.153
    A     @   185.199.110.153
    A     @   185.199.111.153
    CNAME www satymbarnwal.github.io

### If the browser shows a privacy / certificate warning

Normal right after the domain is first pointed at Pages. GitHub issues the
Let's Encrypt certificate only once DNS resolves, which takes from about
15 minutes up to a few hours.

1. Settings -> Pages shows the state under the custom domain. "Certificate is
   being provisioned" means it is working; "DNS check unsuccessful" means the
   records are wrong.
2. Leave **Enforce HTTPS** unticked until the certificate exists, then tick it.
3. If it is still warning after several hours, clear the custom domain, save,
   re-enter it and save again. That re-triggers provisioning.

## Portrait

`client/satyam-cut.webp` is the background-removed portrait used in the hero.
`satyam.webp` is the untouched original. `tools-cutout.py` regenerates the
cutout from the original (needs Pillow and numpy):

    python3 tools-cutout.py

## Content

A personal-brand one-pager: hero, about, journey, work, principles, contact.
The ventures (QueZap, Zap Studio, Zap Water, NuraLearn) are listed as context
for the person, not as a company pitch.

## Design

- Type: Archivo variable (restrained widths), IBM Plex Mono for labels
- Colour: white background throughout; black text and orange `#E8430D`
  accents only. Single light theme.
