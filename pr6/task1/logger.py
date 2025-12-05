from datetime import datetime

def write_log(a, b, oper, result):
    with open("log.txt", "a", encoding="utf-8") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time} | {a} {oper} {b} = {result}\n")