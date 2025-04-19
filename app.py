from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

projects_data = [
    {
        'title': 'Metasploit',
        'description': 'Installasi Metasploit.',
        'image': 'images/metasploit.jpeg',
        'link': 'https://ishikawauta.blogspot.com/2021/11/metasploit.html'  # Ganti dengan tautan proyek
    },
    {
        'title': 'Ubuntu',
        'description': 'command line Nmap.',
        'image': 'images/Ubuntu.jpeg',
        'link': 'https://ishikawauta.blogspot.com/2024/10/install-paket-dasar-ubuntu.html'  # Ganti dengan tautan proyek
    },
    {
        'title': 'Sqlmap',
        'description': 'Installasi Sqlmap.',
        'image': 'images/sqlmap.png',
        'link': 'https://ishikawauta.blogspot.com/2021/11/sqlmap.html'  # Ganti dengan tautan proyek
    },
]

@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)

@app.route('/about')
def about():
    current_year = datetime.now().year
    return render_template('about.html', year=current_year)

@app.route('/projects')
def projects():
    current_year = datetime.now().year
    return render_template('project.html', year=current_year, projects=projects_data)

@app.route('/contact')
def contact():
    current_year = datetime.now().year
    return render_template('contact.html', year=current_year)

if __name__ == '__main__':
    app.run(debug=True)
