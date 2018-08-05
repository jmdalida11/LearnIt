from learnit import app
from learnit.models import db, login_manager
from learnit.views.pages import pages
from learnit.views.activities import activities

if __name__ == "__main__":
    app.register_blueprint(pages)
    app.register_blueprint(activities, url_prefix="/activities")

    db.init_app(app)
    login_manager.init_app(app)

    app.run(debug=True)