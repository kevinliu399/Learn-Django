if IN_DOCKER:  # type: ignore # noqa: F821
    print('IN_DOCKER is True')  # type: ignore
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware',
    ]
