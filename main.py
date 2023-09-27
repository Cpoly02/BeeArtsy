from website import create_app
import controller as c

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug="true")
