from cv06.doors import Graph
import cv06.doors


def test_graph_path01():
    g = Graph({'a': [1, 1], 'b': [1, 1], 'c': [1, 1]})
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')

    assert g.path_exists() == True


def test_graph_path02():
    g = Graph({'o': [2, 0], 'k': [0, 2]})
    g.add_edge('o', 'k')
    g.add_edge('o', 'k')

    assert g.path_exists() == False


def test_resolve_small():
    expected = ['2 False', '3 True', '2 False', '4 True']

    cv06.doors.resolve('small.txt')

    lines = [line.rstrip('\n') for line in open('vysledky.txt')]

    assert lines == expected


def test_resolve_large():
    expected = ['100 True', '100 False']

    cv06.doors.resolve('large.txt')

    lines = [line.rstrip('\n') for line in open('vysledky.txt')]

    assert lines == expected
