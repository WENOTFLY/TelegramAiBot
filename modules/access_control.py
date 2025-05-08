from utils.file_manager import load_json

permissions = load_json("config/permissions.json")

def has_permission(user_id: int, permission: str) -> bool:
    """
    Проверяет, имеет ли пользователь определенное разрешение.
    """
    user_roles = permissions["users"].get(str(user_id), {}).get("roles", [])
    for role in user_roles:
        role_permissions = permissions["roles"].get(role, {}).get("permissions", [])
        if permission in role_permissions:
            return True
    return False
