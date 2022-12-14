from flask import Flask,render_template
app=Flask(__name__,template_folder='template')

@app.route('/')
def Chatbot():
    return render_template('Chatbot.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/home.html')
def Home():
    return render_template('Chatbot.html')

if __name__ =='__main__':
    app.run(debug=True)
