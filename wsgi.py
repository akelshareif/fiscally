from application import create_app

isTesting = False

app = create_app(isTesting)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
