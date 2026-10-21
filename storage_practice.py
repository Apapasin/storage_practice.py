import json
# Задание 1
def append_event(path,text):
    text=text.strip()
    if not text or "\n" in text or "\r" in text:
        return False
    try:
        with open(path, "a", encoding="utf-8") as file:
            file.write(text+"\n")
        return True
    except OSError:
        return False
print(append_event("events.txt", " T118: вход проверен "))
print(append_event("events.txt", "EKEB: профиль открыт"))

# Задание 2
def read_events(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines=file.readlines()
    except FileNotFoundError:
        return []
    except (OSError, UnicodeError):
        return None
    result=[]
    for line in lines:
        text=line.strip()
        if text:
            result.append(text)
    return result
print(read_events("events.txt"))

# Задание 3
bugs=[
    {"id": 1, "title": "Не работает вход",
    "severity": "high", "status": "open"},
    {"id": 4, "title": "Опечатка в расписании",
    "severity": "low", "status": "closed"},
    {"id": 7, "title": "Не сохраняется профиль",
     "severity": "medium", "status": "in_progress"}
]

def export_report(path,bugs):
    total=len(bugs)
    open_count=0
    in_progress_count=0
    closed_count=0
    for bug in bugs:
        if bug["status"]=="open":
            open_count+=1
        if bug["status"]=="closed":
            closed_count+=1
        if bug["status"]=="in_progress":
            in_progress_count+=1

    text= (
        "Отчёт EKEB / T118\n"
        f"Всего: {total}\n"
        f"Открыто: {open_count}\n"
        f"В работе: {in_progress_count}\n"
        f"Закрыто: {closed_count}\n"
    )
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
        return True
    except OSError:
        return False
result=export_report("report.txt",bugs)
print(result)

# Задание 4
def valid_bugs(data):
    if type(data) is not list:
        return False
    ids=[]
    for bug in data:
        if type(bug) is not dict:
            return False
        if set(bug.keys())!={"id", "title", "severity", "status"}:
            return False
        if type(bug["id"]) is not int or bug["id"]<=0:
            return False
        if bug["id"] in ids:
            return False
        ids.append(bug["id"])

        if type(bug["title"]) is not str or len(bug["title"])<5:
            return False
        if bug["severity"] not in ("low", "medium", "high"):
            return False
        if bug["status"] not in ("open", "in_progress", "closed"):
            return False
    return True

def save_bugs(path,bugs):
    if not valid_bugs(bugs):
        return False
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(bugs, file, ensure_ascii=False, indent=4)
        return True
    except OSError:
        return False
result=save_bugs("check_bugs.json",bugs)
print(result)
