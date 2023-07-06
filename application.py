from funix import get_flask_application

application = get_flask_application("main.py")

if __name__ == "__main__":
    application.run()
