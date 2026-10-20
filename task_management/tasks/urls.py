# from django.urls import path
# from .views import TaskCreateView, AssignTaskView, UserTasksView

# urlpatterns = [
#     path('', TaskCreateView.as_view(), name='create_task'),
#     path('<int:pk>/assign/', AssignTaskView.as_view(), name='assign_task'),
#     path('user/<int:user_id>/', UserTasksView.as_view(), name='user_tasks'),
# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'', TaskViewSet)  # Automatically generates CRUD endpoints

urlpatterns = [
    path('', include(router.urls)),
]
