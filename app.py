from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Demo functions (small "abre bones" utilities) ---

def add(a, b):
    """Return numeric sum of a and b."""
    return a + b


def greet(name):
    """Return a simple greeting for name."""
    return f"Hello, {name}!"


def reverse(text):
    """Return reversed string."""
    return text[::-1]


# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/add')
def api_add():
    """API endpoint: /api/add?a=1&b=2 returns JSON with the sum."""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid numbers'}), 400
    return jsonify({'result': add(a, b)})


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name, greeting=greet(name))


if __name__ == '__main__':
    app.run(debug=True)
