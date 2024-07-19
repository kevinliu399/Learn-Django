
if IN_DOCKER: # type: ignore
    print('IN_DOCKER is True') # type: ignore
    assert MIDDLEWARE[:1] == [ # type: ignore
        "django.middleware.security.SecurityMiddleware",
    ]