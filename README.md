# Flask Basics — Learning Project

A beginner-friendly Flask project covering core concepts: routing, variable routes, HTML templates, forms, and redirects.

---

## Concepts Covered

### 1. App Setup
```python
from flask import Flask
app = Flask(__name__)
```
- `Flask(__name__)` creates the application instance.

---

### 2. Basic Routing
```python
@app.route("/", methods=["GET"])
def welcome():
    return "welcome to my flask app"
```
- `@app.route` maps a URL path to a Python function (called a **view function**).
- `methods=["GET"]` restricts the route to GET requests only.

---

### 3. Variable Routing
```python
@app.route('/success/<float:score>')
def success(score):
    return "the person has passed and the score is " + str(score)
```
- `<float:score>` captures a dynamic value from the URL and passes it to the function.
- Supported converters: `string`, `int`, `float`, `path`, `uuid`.

---

### 4. Rendering HTML Templates
```python
from flask import render_template

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")
```
- Templates go inside a `templates/` folder.
- Flask uses **Jinja2** templating — use `{{ variable }}` for expressions and `{% %}` for logic.

---

### 5. Handling Form Data (POST)
```python
from flask import request

maths = float(request.form["maths"])
```
- `request.form` holds data submitted via an HTML form with `method="post"`.
- Access fields by their `name` attribute from the HTML `<input>`.

---

### 6. Redirect & url_for
```python
from flask import redirect, url_for

return redirect(url_for('success', score=avg))
```
- `url_for('function_name')` generates the URL for a given view function.
- `redirect()` sends the user to that URL.

---

## Project Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Welcome message |
| `/index` | GET | Index page |
| `/form` | GET | Renders the marks input form |
| `/form` | POST | Calculates average and redirects |
| `/success/<score>` | GET | Shows pass result |
| `/failure/<score>` | GET | Shows fail result |

---

## Setup & Run

```bash
# Create and activate conda environment
conda create -p venv python=3.11 -y
conda activate ./venv

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
