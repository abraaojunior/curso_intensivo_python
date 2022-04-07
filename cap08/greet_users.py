def greet_users(names):
    """Exibe um msg simples a cada usuario"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ["hannah", "ty", "margot"]
greet_users(usernames)