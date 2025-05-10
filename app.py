# app.py
"""
Minimal clicker game in a single file.
Run with:  python app.py
Then open http://localhost:5000
"""

from flask import Flask, jsonify, Response, request

app = Flask(__name__)

# ----‑ Global state -----------------------------------------------------------
click_count: int = 0           # resets every time the process restarts


# ----‑ Routes -----------------------------------------------------------------
@app.get("/")
def index() -> Response:
    """Serve the whole app (HTML + CSS + JS inline)."""
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Minimal Clicker</title>
        <style>
            html,body {{
                height: 100%;
                margin: 0;
            }}
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                background: #ff7300;                 /* orange backdrop */
                font-family: sans-serif;
            }}
            #wrapper {{
                text-align: center;
            }}
            #count {{
                font-size: 48px;
                font-weight: 600;
                color: #000;
                margin-bottom: 20px;
            }}
            #circle {{
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: #fff;
                cursor: pointer;
                transition: transform 150ms ease;
                display: inline-block;
            }}
            #circle:active {{
                transform: scale(0.9);              /* scale animation */
            }}
        </style>
    </head>
    <body>
        <div id="wrapper">
            <div id="count">{click_count}</div>
            <div id="circle" onclick="increment()"></div>
        </div>

        <script>
            async function increment() {{
                try {{
                    const res = await fetch('/click', {{method: 'POST'}});
                    if (!res.ok) throw new Error('Network response was not ok');
                    const data = await res.json();
                    document.getElementById('count').textContent = data.count;
                }} catch (err) {{
                    console.error(err);
                }}
            }}
        </script>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")


@app.post("/click")
def click() -> Response:
    """Increment global counter and return new value."""
    global click_count
    click_count += 1
    return jsonify(count=click_count)


# ----‑ Entry point ------------------------------------------------------------
if __name__ == "__main__":
    # Development server (single process → safe for in‑memory counter)
    app.run(host="0.0.0.0", port=5000, debug=True)