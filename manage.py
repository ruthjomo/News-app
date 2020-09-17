from app import create_app
from flask_script import  Manager, Server
import os


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


# if __name__ == '__main__':
#     manager.run()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)