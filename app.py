
from flask import Flask, render_template, request, flash
import requests
import json

app = Flask(__name__)
app.secret_key = 'devr'

api_url = "http://ip-api.com/json/"

def ip_scraping(ip=""):
  res = requests.get(api_url+ip)
  api_json_res = json.loads(res.content)
  return api_json_res

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search', methods = ['GET','POST'])
def search():
  if request.method == 'POST':
    ip = request.form.get('ip')
    dic = ip_scraping(ip)
    if 'fail' in dic.values():
      flash('Ocurrió un error al buscar la información de la dirección IP.')
  return render_template('base.html', dic=dic)
  
if __name__ == '__main__':
  app.run()