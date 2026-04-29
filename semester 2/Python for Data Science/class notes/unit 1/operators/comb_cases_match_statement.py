def access(user):
    match user:
        case "admin" | "manager": return "Full Access"
        case "guest": return "Limited Access"
        case _:return "No Access"
print(access("manager"))
print(access("guest"))
print(access("Ravi"))