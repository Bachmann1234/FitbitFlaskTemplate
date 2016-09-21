import flask_login


def register_batman(test_client):
    return test_client.post(
        '/register',
        data=dict(
            username='batman',
            password='robin',
            confirm='robin'
        ),
        follow_redirects=True
    )


def login_batman(test_client):
    return test_client.post(
        '/login',
        data=dict(
            username='batman',
            password='robin'
        ),
        follow_redirects=True
    )


def test_unauthed_index(test_client):
    response = test_client.get('/')
    assert b'login' in response.data


def test_unsuccessful_login(test_client):
    response = register_batman(test_client)
    assert response.status_code == 200
    response = test_client.post(
        '/login',
        data=dict(
            username='batman',
            password='joker'
        ),
        follow_redirects=True
    )
    assert response.status_code == 401
    assert b'Invalid Credentials' in response.data
    response = test_client.post(
        '/login',
        data=dict(
            username='joker',
            password='robin'
        ),
        follow_redirects=True
    )
    assert b'Invalid Credentials' in response.data
    assert response.status_code == 401


def test_logout(test_client):
    response = register_batman(test_client)
    assert response.status_code == 200
    response = login_batman(test_client)
    assert response.status_code == 200
    assert b'batman' in response.data
    response = test_client.get('/logout', follow_redirects=True)
    assert b'Logged Out' in response.data
    assert b'login' in response.data  # Redirected to login


def test_register_and_login_new_user(test_client):
    response = register_batman(test_client)
    assert response.status_code == 200
    response = login_batman(test_client)
    assert response.status_code == 200
    assert b'batman' in response.data


def test_reregistering_is_error(test_client):
    response = register_batman(test_client)
    assert response.status_code == 200
    response = register_batman(test_client)
    assert response.status_code == 400
    assert b'Username batman already taken' in response.data
