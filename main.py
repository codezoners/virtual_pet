from flask import Flask, request, render_template, jsonify
import datetime

LOCAL = False

@app.route("/")
def page():
    return "Hello World"

if LOCAL and __name__ == "__main__":
    app.run(debug=True)
