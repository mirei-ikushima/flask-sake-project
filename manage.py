from app import create_app, db
from app.models import User, Bottle
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
manager.add_command("server", Server)

migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.shell
def create_shell_context():
    return dict(app=app,
                db=db,
                User=User,
                Bottle=Bottle)


if __name__ == '__main__':
    manager.run()
