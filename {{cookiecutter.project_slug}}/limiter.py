from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware


def limiter():
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["{{cookiecutter.global_rate_limit_per_second}}/second"]
    )
    return 