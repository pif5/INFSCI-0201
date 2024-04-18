from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# List of poems as dictionaries
poems = [
    {
        "title": "The Road Not Taken",
        "author": "Robert Frost",
        "text": "Two roads diverged in a yellow wood, And sorry I could not travel both..."
    },
    {
        "title": "Ozymandias",
        "author": "Percy Bysshe Shelley",
        "text": "I met a traveller from an antique land Who said: Two vast and trunkless legs of stone..."
    },
    {
        "title": "Daffodils",
        "author": "William Wordsworth",
        "text": "I wandered lonely as a cloud That floats on high o'er vales and hills..."
    },
    {
        "title": "Sonnet 18",
        "author": "William Shakespeare",
        "text": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate..."
    },
    {
        "title": "The Raven",
        "author": "Edgar Allan Poe",
        "text": "Once upon a midnight dreary, while I pondered, weak and weary..."
    }
]

@app.route('/')
def index():
    return render_template('index.html', poems=poems)

@app.route('/poem/<int:index>')
def poem(index):
    if 0 <= index < len(poems):
        return render_template('poem.html', poem=poems[index])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)