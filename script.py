import os
from colorama import init, Fore, Style

# Initialiser colorama
init()

nom_projet = input(Fore.CYAN + "Entrez le nom du projet : " + Style.RESET_ALL)

projet_express = input(Fore.CYAN + "Est-ce un projet express ? (y/n) : " + Style.RESET_ALL)

if projet_express.lower() == 'y':
    projet_express = True
    nombre_pages = int(input(Fore.CYAN + "Entrez le nombre de pages pour votre projet express : " + Style.RESET_ALL))

    noms_pages = []
    for i in range(nombre_pages):
        nom_page = input(Fore.YELLOW + "Entrez le nom de la page {} : ".format(i+1) + Style.RESET_ALL)
        noms_pages.append(nom_page)
    
    os.makedirs(nom_projet)
    os.chdir(nom_projet)
    os.system('npm init --yes --name="{nom_projet}"')
    os.system('npm install express')
    os.system('npm install path')
    os.makedirs("public")
    with open("index.js", "w") as f:
        f.write('''const express = require('express');
const app = express();
const path = require('path');

''')

        for nom_page in noms_pages:
            if nom_page == 'index':
                f.write(f'''app.get('/', (req, res) => {{
    res.sendFile(path.join(__dirname, 'public', '{nom_page}.html'));
}});
''')
            else:
                f.write(f'''app.get('/{nom_page}', (req, res) => {{
    res.sendFile(path.join(__dirname, 'public', '{nom_page}.html'));
}});
''')

        f.write('''
app.listen(3000, () => {
    console.log('Server started on http://localhost:3000');
});
''')

    os.chdir("public")
    for i, nom_page in enumerate(noms_pages):
        nom_fichier = "{}.html".format(nom_page)
        with open(nom_fichier, "w"):
            pass

    print(Fore.GREEN + "Le projet a été créé avec succès." + Style.RESET_ALL)

else:
    projet_express = False
    nombre_pages = int(input(Fore.CYAN + "Entrez le nombre de pages : " + Style.RESET_ALL))

    noms_pages = []
    for i in range(nombre_pages):
        nom_page = input(Fore.YELLOW + "Entrez le nom de la page {} : ".format(i+1) + Style.RESET_ALL)
        noms_pages.append(nom_page)
    
    os.makedirs(nom_projet)

    for page in noms_pages:
        page_dir = os.path.join(nom_projet, page)
        os.makedirs(page_dir)
        html_file = os.path.join(page_dir, page + ".html")
        css_file = os.path.join(page_dir, page + ".css")
        js_file = os.path.join(page_dir, page + ".js")
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>{}</title>
            <link rel="stylesheet" type="text/css" href="/{}">
            <script src="/{}"></script>
        </head>
        <body>
            <h1>{}</h1>
            <p>Ceci est ma page {}.</p>
        </body>
        </html>
        """.format(page, os.path.join(page_dir, page + ".css"), os.path.join(page_dir, page + ".js"), nom_projet, page)

        with open(html_file, 'w') as f:
            f.write(html_content)
        open(css_file, 'a').close()
        open(js_file, 'a').close()

    print(Fore.GREEN + "Le projet a été créé avec succès." + Style.RESET_ALL)