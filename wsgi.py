from mattfemia import create_app

app = create_app()
app.config.from_object('config.ProductionConfig')

if __name__ == "__main__":
    app.run()