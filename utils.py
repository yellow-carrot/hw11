import json


def load_candidates_from_json(path):
    """
    returns list of candidates from json
    :param path: filename
    :return: candidates list (list)
    """
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id, path):
    """
    returns candidate info with id
    :param candidate_id: id
    :path: file link
    :return: candidate info (dict)
     """
    candidate_list = load_candidates_from_json(path)
    for candidate in candidate_list:
        if candidate['id'] == candidate_id:
            return candidate
        return 'Кандидата с таким id нет'


def get_candidates_by_name(candidate_name, path):
    """
    returns candidate info with name
    :param candidate_name: candidate name
    :param path: file link
    :return: candidate info (dict)
    """
    candidate_list = load_candidates_from_json(path)
    for candidate in candidate_list:
        candidate_info = candidate['name'].lower().split()
        if candidate_name.lower() in candidate_info:
            return candidate
        return 'Кандидата с таким именем нет'


def get_candidates_by_skill(skill_name, path):
    """
    returns candidate info with skill
    :param skill_name: skill
    :param path: file link
    :return: candidate info (dict)
    """
    candidate_list = load_candidates_from_json(path)
    fit_candidates_list = []
    for candidate in candidate_list:

        skills_list = candidate['skills'].lower().replace(',', ' ').split()
        if skill_name.lower() in skills_list:
            fit_candidates_list.append(candidate)
    return fit_candidates_list
