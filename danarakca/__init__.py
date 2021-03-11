# __init__.py
# main interface to danarakca module

from .datasets_handler import __print_item_docs, __read_csv, __datasets_desc
from .support import find_similar


def data(item=None, show_doc=False):
    """loads a dataset (from in-modules datasets) in a dataframe data structure.

    Args:
        item (str)      : name of the dataset to load.
        show_doc (bool) : to show the dataset's documentation.

    Examples:

    >>> apbd = data('apbd')


    >>> data('datadasar_dau', show_doc=True)
        : returns the dataset's documentation.

    >>> data()
        : like help(), returns a dataframe [Item, Title]
        for a list of the available datasets.
    """

    if item:
        try:
            if show_doc:
                __print_item_docs(item)
                return

            df = __read_csv(item)
            return df
        except KeyError:
            find_similar(item)
    else:
        return __datasets_desc()


if __name__ == '__main__':
    # Numerical data
    apbd = data('apbd')
    print(apbd)
