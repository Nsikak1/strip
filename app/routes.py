from app import app


@app.route('/')
def root():
    return "<h2>Strip it</h2>"
