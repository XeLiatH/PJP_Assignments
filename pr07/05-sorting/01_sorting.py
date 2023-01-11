"""
řazení složitějších struktur jako je například list slovníků
"""

from operator import itemgetter

DATA = [
    {
        "id": 6634,
        "result": "1",
        "time": "2:25:18"
    },
    {
        "id": 1742,
        "result": "1",
        "time": "2:25:18"
    },
    {
        "id": 4983,
        "result": "2",
        "time": "2:25:52"
    }]


def get_key(elem):
    """
    Key funkce pro demo_fce
    """
    return elem["id"]


def demo_fce():
    """
    sorting pomoci vlastni funkce
    """
    return sorted(DATA, key=get_key)


def demo_lambda():
    """
    sorting pomoci anonymni (lambda) funkce
    """
    return sorted(DATA, key=lambda k: k["id"])


def demo_operator():
    """
    sorting pomoci itemgetter operátoru
    """
    return sorted(DATA, key=itemgetter("id"))


if __name__ == '__main__':
    print(DATA)
    print("FUNKCE")
    print(demo_fce())
    print("LAMBDA FUNKCE")
    print(demo_lambda())
    print("OPERATOR")
    print(demo_operator())
