#!D:\python39\python.exe

print("Content-Type: text/html") #HTML is following #Header
print()
import cgi, os, view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open("data/"+pageId, "r").read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)

else:
    pageId = "Welcome"
    description = 'Hello Web'
    update_link = ''
    delete_action = ''

print("""<!doctype html>
<html>
    <head>
        <title>WEB1 - WELCOME</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1><a href="index.py">WEB</a></h1>
        <ol>
            {listStr}
        </ol>
        <a href="create.py">create</a>
        {update_link}
        {delete_action}
        <h2>{title}</h2>
        <p>{desc}</p>
        <img src="coding.jpg" width="100%">
    </body>
<html>
""".format(title=pageId, desc=description,listStr=view.getList(), update_link=update_link, delete_action=delete_action))
