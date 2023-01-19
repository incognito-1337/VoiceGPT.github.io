from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
    else:
        message = ""
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run()