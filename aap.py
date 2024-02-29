from flask import Flask, render_template, request ,redirect
from flask_sqlalchemy import SQLAlchemy


aap = Flask('__name__')
aap.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Site1.db'
db = SQLAlchemy(aap)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

@aap.route('/')
def index():
    return render_template('index.html')


@aap.route('/posts')
def posts():
    return render_template('posts.html')


@aap.route('/about')
def about():
    return render_template('about.html')

@aap.route('/create' , methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
       title = request.form['title']
       text = request.form['text']

       post = Post(title=title, text=text)

       try:
           db.session.add(post)
           db.session.commit()
           return redirect('/')
       except:
           return 'При добавлении статьи произошла ошибка'

    else:
        return render_template('create.html')


@aap.route('/index2')
def index2():
    return render_template('index2.html')

@aap.route('/index3')
def index3():
    return render_template('index3.html')



if __name__ == '__main__':
    aap.run(debug=True)
