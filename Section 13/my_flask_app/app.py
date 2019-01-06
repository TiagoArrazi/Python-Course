from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
posts = {}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')
def post_it(post_id):
    post = posts.get(post_id)
    if not post:  # post will be None if not found; not None -> True
        return render_template('404.html',
                               message=f'Post with id {post_id} not found')
    return render_template('post.html', post=post)


@app.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post_it', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
