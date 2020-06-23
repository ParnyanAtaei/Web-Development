import web

urls = [
    "/", "home",
    "/register", "register"
]

render = web.template.render("Views/templates", base="MainLayout")
app = web.application(urls, globals())

class home:
    def GET(self):
        return render.home()

class register:
    def GET(self):
        return render.register()

if __name__ == "__main__":
    app.run()
