from logic import copy_and_rename_files


def title_latest(texture_dir: str):
    file_list = [
        (f'{texture_dir}gui\\title\\background\\panorama_0.png', 'panorama0.png'),
        (f'{texture_dir}gui\\title\\background\\panorama_1.png', 'panorama1.png'),
        (f'{texture_dir}gui\\title\\background\\panorama_2.png', 'panorama2.png'),
        (f'{texture_dir}gui\\title\\background\\panorama_3.png', 'panorama3.png'),
        (f'{texture_dir}gui\\title\\background\\panorama_4.png', 'panorama4.png'),
        (f'{texture_dir}gui\\title\\background\\panorama_5.png', 'panorama5.png'),
    ]
    return copy_and_rename_files('output\\title\\bg', file_list)