import functools

user = {'username': 'john', 'access_level': 'guest'}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else: 
                return f'No access {access_level} to user {user["username"]}'
        return secure_function
    return decorator

@make_secure('guest')
def get_admin_password():
    return "admin_password_123"


@make_secure('guest')
def get_dashboard_password():
    return 'user: user_password'

print(get_admin_password())
print(get_dashboard_password())
