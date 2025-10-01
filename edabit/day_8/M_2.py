"""Medium"""

"""https://edabit.com/challenge/TQrHYN9CNQD9miZwj"""


def fix_import(import_statement):
    import_list = import_statement.split()

    """creating a sub list from index of "from" till end of the import string"""
    new_statement = import_list[import_list.index("from") : :]

    """concatenating a sub list from  0 index to index of "from" """

    new_statement.extend(import_list[: import_list.index("from") :])

    return " ".join(new_statement)


fix_import("import object from module_name")
