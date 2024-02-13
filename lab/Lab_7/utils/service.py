import json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["students"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["students"]


def update_one_by_id(id, student):
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["id"] == id:

            elem["name"] = student["name"]
            elem["contacts"] = student["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["id"] == id:

            candidate = db["students"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(student):
    db = json_service.get_database()

    last_student_id = get_all()[-1]["id"]
    db["students"].append({"id": last_student_id + 1, **student})

    json_service.set_database(db)