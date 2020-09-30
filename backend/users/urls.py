from users.views import ProfileViewSet

router = DefalutRouter()
router.register(r"profiles", ProfileViewset)