import json

def load_candidates_from_json(path):
    """
    returns list of candidates from json
    :param path: filename
    :return: candidates list
    """
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        return data
