students = [
    {"name":"Madhava Chary", "house":"Aravali", "sport":"Cricket"},
    {"name":"Pruthvi", "house":"Nilgiri", "sport":"Soccer"},
    {"name":"Shiva", "house":"Shivalik", "sport":"Tennis"},
    {"name":"Harsha", "house":"Udaigiri", "sport":"Basket ball"}
]


for student in students:
    print(student["name"],student["house"],student["sport"],sep=" ~@~ ")