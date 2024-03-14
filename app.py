from flask import Flask, render_template, request

app = Flask(__name__)
notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")  # Retrieve note from form
        if note:
            notes.append(note)  # Append note to notes list
    return render_template("home1.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
