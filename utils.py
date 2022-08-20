import re
import os

from werkzeug.exceptions import BadRequest

from constants import DATA_DIR


def do_cmd(cmd: str, value: str, data: list[str]) -> list:
    """Добавлена типизация и аннотации"""
    if cmd == "filter":
        result = list(filter(lambda record: value in record, data))
    elif cmd == "map":
        col_num = int(value)
        result = list(map(lambda record: record.split()[col_num], data))
    elif cmd == "unique":
        result = list(set(data))
    elif cmd == "sort":
        reverse = (value == "desc")
        result = sorted(data, reverse=reverse)
    elif cmd == "limit":
        result = data[:int(value)]
    # Добавлена команда regex
    elif cmd == "regex":
        regex = re.compile(value)
        result = list(filter(lambda v: regex.search(v), data))
    else:
        raise BadRequest
    return result


def do_query(params: dict) -> list:
    with open(os.path.join(DATA_DIR, params["file_name"])) as f:
        file_data = f.readlines()
    res = file_data
    if "cmd1" in params.keys():
        res = do_cmd(params["cmd1"], params["value1"], res)
    if "cmd2" in params.keys():
        res = do_cmd(params["cmd2"], params["value2"], res)
    if "cmd3" in params.keys():
        res = do_cmd(params["cmd3"], params["value3"], res)
    return res
