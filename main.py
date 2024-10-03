import os
from tqdm import tqdm

DEBUG = True


def get_new_file_names(file_paths: list[str], rename_function: callable) -> list[str]:
    """
    Returns a list of new file names using a rename function or lambda.

    :param file_paths: list of absoulute file paths
    :param rename_function: function that takes a file path and returns a new file path

    :return: list of new file names
    """

    new_file_names = []

    if DEBUG:
        _iter = tqdm(file_paths)
    else:
        _iter = file_paths

    for file_path in _iter:
        file_name = os.path.basename(file_path)
        new_file_name = rename_function(file_name)
        new_file_names.append(new_file_name)

    return new_file_names


def rename(file_paths: list[str], rename_function: callable):
    """
    Renames a list of files using a rename function or lambda.

    :param file_paths: list of absoulute file paths
    :param rename_function: function that takes a file path and returns a new file path

    :return: None
    """

    new_file_names = get_new_file_names(file_paths, rename_function)

    if DEBUG:
        _iter = tqdm(zip(file_paths, new_file_names))
    else:
        _iter = zip(file_paths, new_file_names)

    for file_path, new_file_name in _iter:
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        os.rename(file_path, new_file_path)






