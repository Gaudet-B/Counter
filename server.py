from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'somethin somethin somethin'

# counter1 = 0

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def increment():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    # print(session['counter'])
    # counter1 = session['counter']
    return redirect('/')
    
@app.route('/destroy_session', methods=['POST'])
def clear_session():
    session.clear()
    print(session)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)