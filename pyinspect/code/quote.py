import math
import sys
import linecache
from .parse import parse_string, node_name
from .parse import Node, token
from .parse import Visitor, find_indentation


class FindNodeVisitor(Visitor):
    def __init__(self, lineno):
        self.lineno = lineno
        self.r = []

    # todo: performance
    def visit(self, node):
        if node.get_lineno() == self.lineno and node.type != token.INDENT:
            self.r.append(node)
            return
        super().visit(node)


class CuttingNodeVisitor(Visitor):
    def __init__(self, lineno: int):
        self.lineno = lineno
        self.seen = set()

    # todo: performance
    def visit(self, node: Node):
        if node.get_lineno() > self.lineno:
            if node.parent is None:
                node.remove()
                return
            for i, x in enumerate(node.parent.children):
                if x == node:
                    for y in node.parent.children[i + 1 :]:
                        if node != y:
                            y.parent = None
                    node.parent.children = node.parent.children[: i + 1]
                    node.remove()
                    return

        self.seen.add(node.get_lineno())
        super().visit(node)


def select_node(t: Node, *, lineno: int) -> Node:
    visitor = FindNodeVisitor(lineno)
    visitor.visit(t)

    return next(iter(visitor.r))  # xxx:


def find_parents(node: Node) -> Node:
    r = [node]
    seen = set()
    target = node

    while target:
        if id(target) in seen:
            break
        if node_name(target) in ("funcdef", "classdef", "async_funcdef"):
            r.append(target)
        elif target.parent is None:
            break
        seen.add(id(target))
        target = target.parent
    return reversed(r)


class Outputter:
    def __init__(self, filename: str, *, n: int, io=sys.stdout):
        self.filename = filename
        self.n = n
        self.io = io
        self.lower_bounds = []
        self.upper_bound = math.inf

    def output(
        self, node: Node, *, _defs=("classdef", "funcdef", "async_funcdef")
    ) -> None:
        name = node_name(node)
        if name in _defs:
            return self._output_def(node)
        else:
            return self._output_other(node)

    def output_skipping(self):
        print("# ...", file=self.io)
        print("", file=self.io)

    def _output_def(self, node: Node) -> None:
        prefix = node.prefix.rstrip(" ").lstrip("\n") + find_indentation(node)
        next_sibling = node.next_sibling
        if next_sibling is not None:
            self.upper_bound = min(next_sibling.get_lineno(), self.upper_bound)

        node = node.clone()
        node.prefix = prefix

        if self.lower_bounds and self.lower_bounds[-1] < node.get_lineno():
            self.output_skipping()

        max_limit = node.get_lineno() + self.n
        v = CuttingNodeVisitor(max_limit)
        v.visit(node)
        self.lower_bounds.extend(sorted(list(v.seen)))
        print(node, file=self.io)

    def _output_other(self, node: Node) -> None:
        n = self.n
        filename = self.filename
        seen = self.lower_bounds

        lineno = node.get_lineno()
        start_lineno = max(1, lineno - n)
        end_lineno = min(len(linecache.getlines(filename)) + 1, lineno + n + 1)
        skip_check_finished = False
        for lineno in range(start_lineno, end_lineno):
            if seen and lineno <= seen[-1]:
                continue
            if lineno >= self.upper_bound:
                continue
            seen.append(lineno)
            line = linecache.getline(filename, lineno)
            if not line.strip():
                continue
            if not skip_check_finished:
                if self.lower_bounds and self.lower_bounds[-1] < node.get_lineno():
                    self.output_skipping()
                skip_check_finished = True
            print(line, end="", file=self.io)


def run(
    filename, *, lineno: int, n: int = 2, show_lineno: bool = False, io=sys.stdout
) -> None:
    # todo: support show_lineno
    outputter = Outputter(filename, n=n, io=io)

    t = parse_string("".join(linecache.getlines(filename)))
    try:
        targets = list(find_parents(select_node(t, lineno=lineno)))
    except StopIteration:
        raise RuntimeError(f"{filename}:L{lineno} is empty?")

    for node in targets:
        outputter.output(node)
