# Houses of Roman Timgad

The source code and content for [timgadhouses.org](https://timgadhouses.org), an open source digital humanities project on the houses of Roman Timgad in modern Algeria.

Built with Jekyll, hosted on GitHub Pages, written and maintained by Kim Edher.

---

## Deployment guide

This guide walks you from a fresh clone to a live site. It assumes you already registered `timgadhouses.org` on Cloudflare.

### 1. Push to GitHub

1. Create a new GitHub account at github.com if you don't have one. Use your kimedher@gmail.com email and pick a username (suggested: `kimedher`).
2. On GitHub, create a new repository called `timgadhouses`. Make it public, do not initialize it with a README.
3. From your terminal, in this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: site scaffold and MVP content"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/timgadhouses.git
   git push -u origin main
   ```
   Replace `YOUR-USERNAME` with the GitHub username you picked.

### 2. Enable GitHub Pages

1. On the GitHub repository page, click **Settings**.
2. In the left sidebar, click **Pages**.
3. Under "Build and deployment," set the source to **Deploy from a branch**.
4. Set the branch to `main` and the folder to `/ (root)`. Click Save.
5. Within a minute or two, GitHub will build the site and show you a URL like `https://YOUR-USERNAME.github.io/timgadhouses/`. Open it to confirm the site loads.

### 3. Point timgadhouses.org at GitHub Pages (Cloudflare DNS)

1. Log in to your Cloudflare dashboard at dash.cloudflare.com.
2. Click on **timgadhouses.org**.
3. In the left sidebar, click **DNS** > **Records**.
4. Add four **A records** for the apex domain. For each one, click "Add record" and use:
   - Type: `A`
   - Name: `@` (means the apex, timgadhouses.org)
   - IPv4 address: one of the four IPs below, repeat for each
   - Proxy status: **DNS only** (gray cloud, not orange) — this is important for GitHub Pages SSL to work
   - TTL: Auto

   The four GitHub Pages IPs are:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

5. Add a **CNAME** for the www subdomain:
   - Type: `CNAME`
   - Name: `www`
   - Target: `YOUR-USERNAME.github.io` (no trailing slash, no path)
   - Proxy status: DNS only
   - TTL: Auto

6. Back on GitHub, in the repository's **Settings > Pages**, find the "Custom domain" field. Enter `timgadhouses.org` and click Save. GitHub will check the DNS and, once it propagates, will issue a free SSL certificate.

7. After the certificate is issued (usually within an hour, sometimes longer), check the **Enforce HTTPS** box on the same Pages settings page.

DNS propagation usually completes in 10 to 60 minutes but can take up to 24 hours. Be patient if the custom domain does not work immediately.

---

## Working on the site locally

You only need to do this if you want to preview changes before pushing to GitHub. GitHub Pages will build and deploy the site automatically on every push.

### Install Ruby and Jekyll (one-time setup)

On macOS:
```bash
brew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
gem install bundler jekyll
```

### Preview the site

In this folder:
```bash
bundle install     # one-time, installs site dependencies
bundle exec jekyll serve
```

Open `http://localhost:4000` in your browser. The site rebuilds automatically when you save a file.

---

## Writing new content

### Add a blog post

Create a file in `_posts/` named `YYYY-MM-DD-your-post-slug.md`. Use this front matter:

```yaml
---
layout: post
title: "Your post title"
date: 2026-04-25
categories: [method]
tags: [timgad, your-tags]
reading_time: 6
excerpt: >-
  One or two sentences that summarize the post for the homepage and the
  Notes index.
---

Your post body here, in Markdown.
```

### Edit a page

The four MVP pages live at the top level of this folder:

- `index.md` — Home page
- `about.md` — About the Project
- `why-timgad.md` — Why Timgad
- `cite.md` — Cite and Contribute
- `notes.md` — Notes and Essays index
- `grid/index.md` — Interactive grid page (the embedded viewer is `grid/viewer.html`)

Just open and edit. Push to GitHub to publish.

### Swap in better images

Drop new images into `assets/images/`. The current placeholders are:

- `kim-fieldwork.jpg` — used on the About page (the field photo from the prospectus presentation)
- `timgad-aerial-bw.jpg` — used on the Home hero (B&W view of the ruins, from the presentation)
- `timgad-1886-theater.jpg` — used on the Why Timgad page (1886 archival photo)
- `house-plan-rooms.jpg` — used on the Why Timgad page (architectural plan)

If you replace one, keep the same filename and the page will pick it up automatically. To use a different filename, also update the page that references it.

---

## File structure

```
timgad-houses-site/
├── _config.yml          Site-wide configuration
├── Gemfile              Ruby dependencies
├── CNAME                Custom domain for GitHub Pages
├── index.md             Home page
├── about.md             About the Project
├── why-timgad.md        Why Timgad
├── cite.md              Cite and Contribute
├── notes.md             Blog index
├── grid/
│   ├── index.md         Interactive grid page
│   └── viewer.html      The Leaflet-based viewer (your existing JSX, exported)
├── _posts/
│   └── YYYY-MM-DD-...   Blog posts
├── _layouts/            Page templates
│   ├── default.html     Master layout (header, footer)
│   ├── home.html        Home page layout (hero + features)
│   ├── page.html        Standard page layout
│   └── post.html        Blog post layout
├── assets/
│   ├── css/main.scss    Site stylesheet
│   └── images/          Site images
└── README.md            This file
```

---

## License

Text and content © Kim Edher, released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Site code released under the [MIT License](https://opensource.org/licenses/MIT).
