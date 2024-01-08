import os

from app import create_app

config_class = os.environ.get('CONFIG_CLASS', 'config.TestingConfig')

app = create_app(config_class)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
