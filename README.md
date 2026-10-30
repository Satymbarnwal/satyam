# satyambarnwal.com

Personal site for Satyam Barnwal — founder, ZAP Innovations Pvt Ltd.

A single static page, no build step. `index.html` holds all markup, CSS and
JS, fonts come from Google Fonts, and `satyam-cut.webp` is the portrait.

Only two files are needed to serve the site: `index.html` and
`satyam-cut.webp`, side by side.

## Run locally

    python3 -m http.server 8000

Then open http://localhost:8000

## Deploy with GitHub Pages

The site sits at the repository root, so Pages needs no configuration:

1. Push this branch, or merge it into `main`.
2. In the repository, go to **Settings -> Pages**.
3. Under **Source**, choose **Deploy from a branch**, pick the branch and
   the `/ (root)` folder, and save.

The site goes live at `https://<user>.github.io/<repo>/` within a minute or
two. For `satyambarnwal.com`, enter it under **Custom domain** on that same
page, then add these DNS records at your registrar:

    A     @   185.199.108.153
    A     @   185.199.109.153
    A     @   185.199.110.153
    A     @   185.199.111.153
    CNAME www <user>.github.io

GitHub writes a `CNAME` file into the repository once you save the domain.
`.nojekyll` is already present so Pages serves the files untouched.

## Deploy to Zoho Catalyst

The repository also works as a Catalyst **Web Client Hosting** project.

1. Install the CLI and sign in:

       npm install -g zcatalyst-cli
       catalyst login

2. Create a project named `satyam` in the Catalyst console, then open
   `catalyst.json` and replace `REPLACE_WITH_YOUR_PROJECT_ID` with that
   project's ID. (Running `catalyst init` in this directory writes the file
   for you instead, if you prefer — pick "Client" as the component and the
   current directory, and keep the existing files when asked.)

3. Deploy:

       catalyst deploy --only client

Catalyst serves the site at `https://<project>-<id>.development.catalystserverless.in/`
Add `satyambarnwal.com` under the project's **Custom Domain** settings and
point the domain's DNS at the CNAME the console gives you.

## Deploy anywhere else

`index.html` and `satyam-cut.webp` are a plain static pair, so they drop
straight into Netlify, Vercel or Cloudflare Pages with no changes.

## Portrait

`satyam-cut.webp` is the background-removed portrait used in the hero.
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
