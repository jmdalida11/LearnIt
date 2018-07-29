from learnit import app
from learnit.views.pages import pages

if __name__ == "__main__":
    app.register_blueprint(pages)
    app.run(debug=True)