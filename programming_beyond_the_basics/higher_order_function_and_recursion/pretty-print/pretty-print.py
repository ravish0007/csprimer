from pprint import pprint
from collections.abc import Iterable

l = [1, 2, 3, ['a', 'b', ['c'], 'foo'], 4]


def pretty_formatted(data, indent=4):
    def pretty_print_inner(data, start_indent=0, result=''):

        outer_spacing = start_indent * ' '
        inner_spacing = (indent + start_indent) * ' '
        if not isinstance(data, Iterable):
            return result + outer_spacing + str(data) + '\n'

        if isinstance(data, list):
            if len(data) == 0:
                return result + outer_spacing + '[]' + '\n'
            result = result + outer_spacing + '[' + '\n'

        for datum in data:
            if isinstance(datum, list):
                result = pretty_print_inner(datum,
                                            start_indent+indent, result)
            else:
                result += inner_spacing + str(datum) + ',\n'

        result = result[:-2] + '\n' + outer_spacing + '],' + '\n'
        return result

    return pretty_print_inner(data, 0)[:-2]+'\n'


pprint(l, width=10)
# formatted_string = pretty_formatted(l)
# print(formatted_string)
