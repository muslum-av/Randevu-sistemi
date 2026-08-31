from flask import Flask, render_template, request
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
GONDEREN_EMAIL ="mohsenafshar401@gmail.com"
GONDEREN_SIFRE ="oqsfkyjznptiancj"
ALICI_EMAIL ="somanentizar23@gmail.com"

def eposta_gonder(ad_soyad, telefon, hizmet, tarih, saat):
  konu: str = f"Yeni Randevu Var! - {ad_soyad}"
  icerik = f"""Merhaba, web sitenizden yeni bir rendevu alindi:

  Muşteri Adi: {ad_soyad}
  Telefon: {telefon}
  Hizmet: {hizmet}
  Tarih: {tarih}
  Saat: {saat}""" 

  msg = MIMEMultipart()
  msg['From'] = GONDEREN_EMAIL
  msg['To'] = ALICI_EMAIL
  msg['Subject'] = konu
  msg.attach(MIMEText(icerik, 'plain', 'utf-8'))

  try:
           server = smtplib.smtp('smtp.gmail.com',587, timeout=5)
           server.starttls()
           server.login(GONDEREN_EMAIL, GONDEREN_SIFRE)
           server.send_message(msg)
           server.quit()
           print("E-posta başariyla gnderildi!")
  except Exception as e:
           print(f"E-posta gonderilirken hata olustu: {e}")


@app.route('/')
def home():
       return render_template('index.html')

@app.route('/randevu-al', methods=['POST'])
def randevu_al():
       ad_soyad = request.form.get('adsoyad')
       telefon = request.form.get('telefon')
       hizmet = request.form.get('hizmet')
       tarih = request.form.get('tarih')
       saat = request.form.get('saat')

       eposta_gonder(ad_soyad, telefon, hizmet, tarih, saat)

       return render_template('success.html')

if __name__ == '__main__':
   app.run(debug=True)
