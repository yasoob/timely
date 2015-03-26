import pytest

from Bookme import create_app
from Bookme.models import db, User


@pytest.fixture()
def testapp(request):
    app = create_app('Bookme.settings.DevConfig', env='dev')
    client = app.test_client()

    db.app = app
    db.create_all()

    if getattr(request.module, "create_user", True):
        admin = User('admin', 'supersafepassword')
        db.session.add(admin)
        db.session.commit()

    def teardown():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(teardown)

    return client
