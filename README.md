# tranngochuan.github.io

# My Profile Page

This project consists of a static profile page built with HTML and CSS, served using Python Flask.

## Frontend

The frontend consists of a single HTML file (`profile.html`) for basic part and a single HTML file (`profile1.html`) for advanced part that defines the structure and content of the profile page. It is styled using an external CSS file (`style.css`).

## Backend

The backend is built using Python Flask.
Basic part: Serve static profile page at default route.
Advanced part: It serves the static profile page and associated resources (images, CSS) at the `/profile` route. The default route (`/`) redirects to the `/profile` route.

## How to Run

1.  Clone the repository.
2.  Install the required Python packages: `pip install Flask`.
3.  Run the Flask:
    Basic part: `py app.py`
    Advanced part: `py app1.py`.
4.  Open your web browser and navigate to `http://127.0.0.1:5000` (or the address shown in terminal).
