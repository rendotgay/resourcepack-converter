from logic import copy_and_rename_files


def environment_latest(texture_dir):
    file_list = [
        (f'{texture_dir}environment\\clouds.png'),
        (f'{texture_dir}environment\\rain.png'),
        (f'{texture_dir}environment\\snow.png'),
    ]
    return copy_and_rename_files('output\\environment', file_list)