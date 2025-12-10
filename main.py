# Kütüphaneleri yükleme/Flask'a bağlanma
from flask import Flask, render_template, request, redirect, session
# Veti tabanı kütüphanesine bağlanma
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Oturum için gizli anahtarın ayarlanması
app.secret_key = 'my_top_secret_123'
# SQLite bağlantısı kurma
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veritabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Card(db.Model):
    # Tablo giriş alanları oluşturma
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Başlık
    title = db.Column(db.String(100), nullable=False)
    # Alt başlık
    subtitle = db.Column(db.String(300), nullable=False)
    # Metin
    text = db.Column(db.Text, nullable=False)
    # Kart sahibinin e-posta adresi
    user_email = db.Column(db.String(100), nullable=False)

    # Nesneyi ve kimliğini çıktı olarak verme
    def __repr__(self):
        return f'<Card {self.id}>'
    

# Görev #1. Kullanıcı tablosunu oluşturun.


# İçerik sayfasını başlatma
@app.route('/', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
            
        # Görev #4. Kullanıcı doğrulamasını uygulayın

     
    else:
        return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Görev #3. Kullanıcı doğrulamasını uygulayın


        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# İçerik sayfasını başlatma
@app.route('/index')
def index():
    # Görev #4. Kullanıcının yalnızca kendi kartlarını görmesini sağlayın.
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Kart sayfasını başlatma
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Kart oluşturma sayfasını başlatma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Görev #4. Kullanıcı adına kart oluşturma işlemini gerçekleştirin.
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

if __name__ == "__main__":
    app.run(debug=True)
