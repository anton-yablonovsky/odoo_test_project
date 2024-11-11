from api.models import User, Role
user = User()

if not User.objects.filter(username="admin").exists():
    user.objects.create_user(
        username="admin",
        password="admin",
        role=Role.ADMIN
    )

    user.is_superuser = True
    user.is_staff = True
    user.save()
