#test.py
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
<<<<<<< HEAD
	return "hello"
=======
	return "hello!"
>>>>>>> e772d6c0d615ef5eda16aaabdcf09e8654d94607
 
if __name__ == "__main__":
	app.run()
