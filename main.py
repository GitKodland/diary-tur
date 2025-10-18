from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'secret-key-enis'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'diary.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Kart tablosu
class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Card {self.id}>"

# Kullanıcı tablosu
# Kullanıcı tablosunu güncel şekilde tanımla
class Kullanici(db.Model):
    __tablename__ = 'kullanicilar'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    
    # Yeni sütunlar
    last_login_ip = db.Column(db.String(50))
    last_login_user_agent = db.Column(db.String(300))
    last_login_time = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Kullanici {self.id}>"

# Mevcut tabloya sütun ekleme (sadece bir kez çalıştır)
with app.app_context():
    try:
        db.engine.execute("ALTER TABLE kullanicilar ADD COLUMN last_login_ip TEXT;")
    except:
        pass
    try:
        db.engine.execute("ALTER TABLE kullanicilar ADD COLUMN last_login_user_agent TEXT;")
    except:
        pass
    try:
        db.engine.execute("ALTER TABLE kullanicilar ADD COLUMN last_login_time DATETIME;")
    except:
        pass


with app.app_context():
    db.create_all()

# Login route
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']

        user = Kullanici.query.filter_by(login=form_login, password=form_password).first()
        if user:
            # IP ve User-Agent kaydet
            user.last_login_ip = request.remote_addr
            user.last_login_user_agent = request.headers.get('User-Agent')
            user.last_login_time = datetime.now()
            db.session.commit()

            session['user_id'] = user.id
            return redirect('/index')
        else:
            error = "E-posta veya şifre hatalı."
            return render_template('login.html', error=error)
    return render_template('login.html', error=error)


# Registration
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login_input = request.form.get('email')
        password_input = request.form.get('password')

        user_exists = Kullanici.query.filter_by(login=login_input).first()
        if user_exists:
            error = "Bu e-posta zaten kayıtlı."
            return render_template('registration.html', error=error)
        else:
            user = Kullanici(login=login_input, password=password_input)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
    return render_template('registration.html')

# Ana sayfa ve kartlar
@app.route('/index')
def index():
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Tek kart sayfası
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get_or_404(id)
    return render_template('card.html', card=card)

# Kart oluşturma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu gönderme
@app.route('/form_create', methods=['POST'])
def form_create():
    title = request.form.get('title')
    subtitle = request.form.get('subtitle')
    text = request.form.get('text')

    card = Card(title=title, subtitle=subtitle, text=text)
    db.session.add(card)
    db.session.commit()
    return redirect('/index')

if __name__ == "__main__":
    debug_env = os.environ.get("FLASK_DEBUG", "1").lower()
    debug_mode = debug_env in ("1", "true")
    app.run(debug=debug_mode)
