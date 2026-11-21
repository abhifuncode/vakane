# Vakane Engineering website

A minimal, fast, static website for a certification and compliance consultancy. It has 181 pages and no framework.

## Folders
- `site/` – the finished website. Upload this folder to any host (Netlify, Vercel, Hostinger, cPanel, S3).
- `src/data.py` – **all the content**: brand name, phone, email, address, services, countries and articles.
- `src/templates.py` – the benefits, documents, process and FAQ for each type of service.
- `src/assets/` – `styles.css`, `main.js` and the favicon.
- `src/build.py` – the generator. It turns the content into the pages in `site/`.

## Make changes
1. Edit `src/data.py`. Start with `BRAND` at the top: the name, phone numbers, email, address and WhatsApp number.
2. Rebuild:
   ```
   python3 src/build.py
   ```
3. Open `site/index.html` or upload `site/`.

## Before going live
- **Contact form:** set `FORM_ENDPOINT` in `src/build.py` to a form service URL, such as Formspree or Getform. Until you do, the form opens the visitor's email app.
- **Domain:** replace `https://www.example.com/` in `build.py` so the generated `sitemap.xml` uses your domain.
- **Placeholders to replace:** team names and photos (`team.html`), client logos (`clients.html`), the recognition items (`recognition.html`), the partner office addresses and the social media links.
- **Adding a service:** add one `add(...)` or `prod(...)` line in `data.py` and rebuild. The service then gets its own page and appears in its category, in search and on the sitemap.

## Photos
The photos in `src/assets/img/` come from Unsplash, under the Unsplash License: free for commercial use, no attribution required. Each photo has two sizes, `name.webp` (1600px wide) and `name-sm.webp` (820px wide). To swap a photo, replace both files and keep the same name.
