#!/usr/bin/env python3

import mysql.connector
import cherrypy
import config

class VulnerableApp(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host=config.DB_HOST, user=config.DB_USER, database=config.DB_NAME, password=config.DB_PASS)


    @cherrypy.expose
    def view(self, **get):
        if "id" in get:
            cursor = self.conn.cursor()
            requete = "SELECT text FROM articles WHERE id='" + get["id"] + "'"
            print("req: [" + requete + "]")
            cursor.execute(requete)
            rows = cursor.fetchall()
            text="Cet article n'existe pas"
            if cursor.rowcount == 1:
                text=rows[0][0]
            return '''
<html>
<head>
<title>Application Python Vulnerable</title>
</head>
<body>
''' + text + '''
<p>
</p>
</html>
'''
        return '''
<html>
<head>
<title>Application Python Vulnerable</title>
</head>
<body>
<p>
Veuillez specifier un id d'article a afficher
<form method="get">
<input type="text" name="id" id="id" value="" />
<br />
<input type="submit" name="submit" value="OK" />
</form>

</p>
</html>
'''

    @cherrypy.expose
    def login(self, **post):
        cursor = self.conn.cursor()
        if cherrypy.request.method == "POST":
            requete = "SELECT * FROM users WHERE login='" + post["login"] + "' and password='" + post["password"] + "'"
            print("req: [" + requete + "]")
            cursor.execute(requete)
            cursor.fetchall()
            if cursor.rowcount == 1:
                return '''
<html>
<head>
<title>Application Python Vulnerable</title>
</head>
<body>
<p>
Bravo vous etes authentifié!
</p>
</body>
</html>
'''
        return '''
<html>
<head>
<title>Application Python Vulnerable</title>
</head>
<body>
<p>
Veuillez vous identifier

<form method="post">
<input type="text" name="login" id="login" value="" />
<br />
<input type="text" name="password" id="password" value="" />
<br />
<input type="submit" name="submit" value="OK" />
</form>

</p>
</body>
</html>
'''


cherrypy.quickstart(VulnerableApp())

