from learnit import app
from learnit.views.pages import pages
from learnit.models import db, login_manager

if __name__ == "__main__":
    app.register_blueprint(pages)
    db.init_app(app)
    login_manager.init_app(app)

    app.run(debug=True)