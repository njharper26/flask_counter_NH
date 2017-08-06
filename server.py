from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)

app.secret_key = 'd41d8cd98f00b204e9800998ecf8427e'

@app.route('/')
def index():
    print 'plus one or two'
    if 'count' in session.keys():
        session['count'] += 1
    else:
        session['count'] = 1

    return render_template('index.html', count=session['count'])

@app.route('/plus2', methods=['POST'])
def plus2():
    print 'plus two'
    session['count'] += 1

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print 'reset'
    session['count'] = 0

    return redirect('/')

app.run(debug=True)