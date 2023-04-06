import random
from flask_seeder import Seeder

from app.models import User


class UserSeeder(Seeder):
    def run(self):
        admin = User('admin', 'admin', 'a@.ru', 0, True)
        manager = User('manager', 'manager', 'm@.ru', 1, True)
        moderator = User('moderator', 'moderator', 'mod@.ru', 2, True)
        anonymous = User('anonymous', random.randbytes(256).hex(), 'anon@.ru', 3, True)

        self.db.session.add(admin)
        self.db.session.add(manager)
        self.db.session.add(moderator)
        self.db.session.add(anonymous)
