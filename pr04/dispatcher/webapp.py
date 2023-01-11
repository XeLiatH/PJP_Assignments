# -*- coding: utf-8 -*-
"""
ukazka implementace navhroveho vzoru Dispatcher
- pomoci funkce getattr
- pomoci slovniku
"""

import gethandler


def error_404():
    """
    chybova hlaska
    """
    return '404 - not found'


def if_else_pristup(page):
    """
    takhle ne přátelé - to moc daleko nedojdete
    """
    if page == 'index':
        return gethandler.index()
    elif page == 'page1':
        return gethandler.page1()
    


def slovnik(page):
    """
    slovník = hashtable => nejrychlejší hledání
    je to lepší přístup, ale stále náročný na údržbu
    nestačí jen přidat funkci do modulu
    """
    dis = {
        "index": gethandler.index,
        "page1": gethandler.page1,
        "page2": "page2"
    }

    try:
        return dis[page]()
    except KeyError:
        return error_404()
    except TypeError:
        return error_404()    

def dispatcher(page):
    """
    dispatcher je implementován built-ín funkcí gettatr
    :param page: string
    :return: string
    """
    process_func = getattr(gethandler, page, error_404)
    return process_func()


if __name__ == '__main__':
    GET = 'page33'
    print(if_else_pristup(GET))
    print(slovnik(GET))
    print(dispatcher(GET))
