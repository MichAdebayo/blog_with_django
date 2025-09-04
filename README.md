# Purely Sports 

<p align="center">
 <img width=800px src= "https://github.com/user-attachments/assets/487de1fb-f40a-451e-8a47-5dcf1ef33188"/>
</p>

Purely Sports is a Django-powered sports blog application with a clean, responsive two-column layout (sidebar navigation & search + main article feed). This repository contains the application used for creating and listing articles and categories, with a modernized UI and CSS.

## Project structure

```
MyBlog/
├── manage.py
├── db.sqlite3
├── MyBlog/            # project settings and URLs (settings.py, urls.py, wsgi/asgi)
├── blog/              # core blog app (models, views, forms, templates)
├── static/            # compiled/static assets (css, img, js)
└── templates/         # shared templates (base.html, includes)
```

## Features
- Two-column responsive layout: left sidebar (nav + search), right content (articles).
- Search/filter form for articles by title, category and publication date.
- Create article and create category forms.
- Clean, blue-accent article cards and accessible UI.

## Requirements
- Python 3.10+.


## Quick setup
1. Create and activate a virtual environment (recommended):

```bash
cd MyBlog
python -m venv .venv
source .venv/bin/activate
```

2. Install project dependencies

```bash
pip install -r ../requirements.txt
```

3. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/blog/ to view the site.

## Static files and assets
- Static CSS is served from `MyBlog/static/css/styles.css`.
- Place logo and social icons in `MyBlog/static/img/` (recommended filenames used by templates):
	- `sports_logo.svg`
	- `twitter.svg`
	- `instagram.svg`
	- `facebook.svg`
- Use SVG for crisp scaling. Recommended sizes:
	- Logo (sidebar/brand): 48–56px square
	- Social icons (footer): 24–28px square

If you update CSS and don't see changes in the browser, hard-reload (Cmd+Shift+R) or use the cache-busting query parameter already included in `base.html` (`?v=2`).

## Templates & customization
- `MyBlog/templates/base.html` holds the main two-column layout and includes the sidebar via `includes/header.html`.
- `MyBlog/templates/includes/header.html` contains the sidebar brand and nav links.
- The article list template is `MyBlog/blog/templates/blog/liste_articles.html` and expects `articles` and an optional `form` (sidebar `ArticleFilterForm`) in the context.

To change markup or layout:
- Edit `base.html` to adjust the grid or top header.
- Edit `styles.css` to tune colors, spacing, and responsive breakpoints.

## Forms and filtering
- The class-based view `ListeArticlesView` (in `blog/views.py`) uses `FormView` + `ListView` and supplies `ArticleFilterForm`.
- The sidebar search form submits `GET` parameters and the view filters the queryset accordingly.

## Tests
- Tests for the `blog` app live in `MyBlog/blog/tests.py` (add tests there).
- To run tests:

```bash
python manage.py test
```

## Troubleshooting
- Static files not updating: hard refresh or restart the dev server. A cache-buster `?v=2` is appended to the stylesheet in `base.html` to help.
- CSS not applied: confirm the `<link>` path shown in page head points to `/static/css/styles.css?v=2` and `DEBUG=True` in development.
- Template errors (e.g., `Invalid block tag 'static'`): make sure templates that use `{% static %}` include `{% load static %}` at the top.


## Contributing
- Fork the repository
- Create a branch for your feature or fix.
- Create a PR

## License
- This project is licensed under the `MIT LICENSE`.


## Author
Michael Adebayo ([@MichAdebayo](https://github.com/MichAdebayo))
