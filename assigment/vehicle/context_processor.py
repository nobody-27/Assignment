from .models import Vehicle_Types,User
def get_List_of_vehicle_types(request):

    if request.user.is_anonymous:
        return {}
    
    
    ip = request.id_address
    current_user = request.user.id
    user = User.objects.get(id=current_user)
    usertype = user.get_role_details
    vehicle_types = Vehicle_Types.objects.all()

    permision = []
    if user.user_type == 1:
        permision.append("Add,Edit,Delete,View")
    if user.user_type == 2:
        permision.append("Edit,View")
    if user.user_type == 3:
        permision.append("View")

    return {
        'vehicle_types': vehicle_types,
        'user_role':usertype,
        'ip':ip,
        'permision':permision,
        'username':user.username
    }