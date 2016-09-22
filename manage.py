from app import create_app
from config import get_current_config

app = create_app(
    get_current_config()
)


if __name__ == '__main__':
    app.run()
