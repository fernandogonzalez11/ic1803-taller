tabla = """
Nombre JG  JF
─────────────
lol     1   2
lol2    3   4
"""

html = f"""
<html>
    <body style="font-family: sans-serif;">
        <h2>Torneos de bola</h2>
        <h3>Tabla de resultados</h3>
        <pre>{tabla}</pre>
    </body>
</html>
"""

file = open("tabla.html", "w")
file.write(html)
file.close()