from django.contrib.auth.models import User
from django.http import parse_cookie

from rest_framework.authtoken.models import Token

from channels.db import database_sync_to_async

@database_sync_to_async
def get_user(token):
    try:
        return Token.objects.get(key=token).user
    except User.DoesNotExist:
        return AnonymousUser()

class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if 'headers' in scope:
            for name, value in scope.get("headers", []):
                if name == b"cookie":
                    cookies = parse_cookie(value.decode("latin1"))
                    scope['user'] = await get_user(cookies.get('token'))
                    break
        elif 'token' in scope['query_string']:
            token = scope['query_string'].decode("utf-8").replace('token=', '')
            scope['user'] = await get_user(token)

        return await self.app(scope, receive, send)
