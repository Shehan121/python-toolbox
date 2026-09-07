"""Topological ordering of a dependency graph."""

from collections import deque


class CycleError(ValueError):
    """Raised when the graph cannot be linearised."""


def toposort(graph):
    """Return nodes of *graph* so every node follows its dependencies.

    *graph* maps a node to the iterable of nodes it depends on.

    >>> toposort({"app": ["lib"], "lib": ["core"], "core": []})
    ['core', 'lib', 'app']
    >>> toposort({"a": ["b"], "b": ["a"]})
    Traceback (most recent call last):
        ...
    toposort.CycleError: graph contains a cycle
    """
    dependents = {}
    indegree = {}
    for node, deps in graph.items():
        indegree.setdefault(node, 0)
        for dep in deps:
            indegree.setdefault(dep, 0)
            dependents.setdefault(dep, []).append(node)
            indegree[node] += 1

    queue = deque(sorted(n for n, d in indegree.items() if d == 0))
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for dependent in dependents.get(node, ()):
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)

    if len(order) != len(indegree):
        raise CycleError("graph contains a cycle")
    return order
