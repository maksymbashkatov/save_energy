import random
from datapoints.models import Datapoint
from organizations.models import OrganizationProject, OrganizationObject
from users.models import CustomUser


def data_initialization(project_amount):
    for i in range(1, project_amount + 1):
        op = OrganizationProject.objects.create(name=f'OrganizationProject{i}')
        for j in range(1, 4):
            oo = OrganizationObject.objects.create(name=f'OrganizationObject{j}', organization_project=op)
            for o in range(1, random.randint(2, 5)):
                Datapoint.objects.create(
                    name=f'{oo.name}Datapoint{o}', counter_data=random.randint(1, 10), organization_object=oo
                )
        for j in range(1, 4):
            CustomUser.objects.create(
                email=f'{op.name}_user{j}@gmail.com', role=random.choice(CustomUser.roles)[0], organization_project=op
            )
