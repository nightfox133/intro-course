from flask import Flask, request, render_template_string
from index import temp

file_path = r'C:\Users\marco\.vscode\python\projects\columbia\assingments\json\project\history2.json'
app = Flask(__name__)

# HTML template with a form
HTML_TEMPLATE = temp()

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        return(user_input)
    #return render_template_string(HTML_TEMPLATE, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
