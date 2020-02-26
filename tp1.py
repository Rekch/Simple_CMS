from flask import Flask, render_template, url_for, flash, redirect
from form import PostForm, ModifyPostForm
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a3a9fb269885a66d27c3875e9d3b99bd'


try:
    db = sqlite3.connect(':memory:', check_same_thread=False)
    print("La connexion est etablie: la database est cree dans la memoire.")
    cursor = db.cursor()

    fh = open('db.sql', 'r')
    script = fh.read()
    cursor.executescript(script)

    print("Script lu")

except Exception as e:
    db.rollback()
    raise e


posts = [{}]
postsDup = [{}]


@app.route("/")
@app.route("/accueil")
def accueil():
    cursor.execute(
        "SELECT * FROM article WHERE date_publication <= date('now')"
        " ORDER BY date_publication DESC LIMIT 5 ;")
    del posts[:]
    del postsDup[:]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        post = (row[0], row[1], row[2], row[3], row[4], row[5])
        if post not in postsDup:
            posts.append(post)
            postsDup.append(post)
    return render_template('accueil.html', posts=posts)


@app.route("/admin")
def admin():
    cursor.execute("SELECT * from article;")
    del posts[:]
    del postsDup[:]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        post = (row[0], row[1], row[2], row[3], row[4], row[5])
        if post not in postsDup:
            posts.append(post)
            postsDup.append(post)
    return render_template('admin.html', posts=posts)


@app.route("/admin-nouveau", methods=['GET', 'POST'])
def admin_nouveau():
    form = PostForm()
    if form.validate_on_submit():
        titre = form.title.data
        identifiant = form.identifiant.data
        auteur = form.auteur.data
        date_parution = form.date.data
        paragraphe = form.content.data
        params = (titre, identifiant, auteur, date_parution, paragraphe)
        cursor.execute(
            "INSERT INTO article(titre, identifiant, auteur, "
            "date_publication, paragraphe) VALUES( ?, ?, ?, ?, ?)",
            params)
        flash('Post cree avec succes!', 'success')
        return redirect(url_for('admin'))
    return render_template(
        'creation_post.html',
        title='Nouveau poste',
        form=form)


@app.route("/article/<identifiant>")
def article(identifiant):
    post = []
    cursor.execute(
        "SELECT * FROM article WHERE identifiant = (?);", (identifiant,))
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        post = (row[0], row[1], row[2], row[3], row[4], row[5])
    return render_template('post.html', post=post)


@app.route("/modifier/<identifiant>", methods=['GET', 'POST'])
def modifier(identifiant):
    post = []
    cursor.execute(
        "SELECT * FROM article WHERE identifiant = (?);", (identifiant,))
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        post = (row[0], row[1], row[2], row[3], row[4], row[5])
    form = ModifyPostForm()
    if form.validate_on_submit():
        new_titre = form.title.data
        new_paragraphe = form.content.data
        id = post[0]
        cursor.execute(
            "UPDATE article SET titre=?, paragraphe=? WHERE id = (?);",
            (new_titre,
             new_paragraphe,
             id,
             ))
        flash('Post modifie avec succes!', 'success')
        return redirect(url_for('admin'))
    return render_template(
        'modification_post.html',
        title='Modifier poste',
        form=form,
        post=post)


@app.route("/search/<recherche>")
def search(recherche):
    cursor.execute(
        "SELECT * FROM article WHERE (titre LIKE (?) OR paragraphe LIKE (?));",
        ("%" + recherche + "%",
         "%" + recherche + "%"))
    del posts[:]
    del postsDup[:]
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        post = (row[0], row[1], row[2], row[3], row[4], row[5])
        if post not in postsDup:
            posts.append(post)
            postsDup.append(post)
    return render_template('accueil.html', posts=posts)

if __name__ == '__main__':
	app.run()