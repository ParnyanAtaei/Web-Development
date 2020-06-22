import web

urls = [
    "/", "home"
]

render = web.template.render("Views/templates", base="MainLayout" )
app = web.application(urls, globals())

class home:
    def GET(self):
        return render.home()

if __name__ == "__main__":
    app.run()
