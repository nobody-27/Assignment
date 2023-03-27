from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .models import User,Vehicle
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType



@receiver(post_save,sender=User)
def set_permision(sender,instance,**kwaregs):
    content_type = ContentType.objects.get_for_model(Vehicle)

    super_admin_group, created = Group.objects.get_or_create(name="Super_admin")
    admin_group, created = Group.objects.get_or_create(name="Admin")
    user_group, created = Group.objects.get_or_create(name="User")

    permission = Permission.objects.filter(
        content_type=content_type, 
    )

    super_perm_list = ['view_vehicle','change_vehicle','delete_vehicle','add_vehicle']
    admin_perm_list = ['view_vehicle','change_vehicle']
    user_perm_list = ['view_vehicle']


    for perm in permission:
        if perm.codename in admin_perm_list:
            admin_group.permissions.add(perm)

        if perm.codename in super_perm_list:
            super_admin_group.permissions.add(perm)

        if perm.codename in user_perm_list:
            user_group.permissions.add(perm)


    if instance.user_type == 1:
        instance.groups.add(super_admin_group)

    elif instance.user_type == 2:
        instance.groups.add(admin_group)

    else:
        instance.groups.add(user_group)







