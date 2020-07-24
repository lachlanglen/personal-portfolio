from projects.models import Project

instance = Project.objects.get(id=1)
print(instance)
