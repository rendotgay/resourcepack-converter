from logic import freeform_png, copy_and_rename_files


def chest_texture_list(texture_dir) -> list:
    return [
        (f'{texture_dir}entity\\chest\\normal_left.png', 59, 0, (14, 0), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_left.png', 29, 0, (29, 0), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_left.png', 29, 14, (14, 14), 180, None, (44, 5)),
        (f'{texture_dir}entity\\chest\\normal_left.png', 59, 19, (14, 19), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_left.png', 29, 19, (29, 19), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_left.png', 29, 33, (14, 33), 180, None, (44, 10)),
        (f'{texture_dir}entity\\chest\\normal_right.png', 44, 0, (14, 0), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_right.png', 14, 0, (29, 0), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_right.png', 14, 14, (43, 14), 180, None, (15, 5)),
        (f'{texture_dir}entity\\chest\\normal_right.png', 0, 14, (0, 14), 180, None, (14, 5)),
        (f'{texture_dir}entity\\chest\\normal_right.png', 73, 14, (14, 14), 180, None, (15, 5)),
        (f'{texture_dir}entity\\chest\\normal_right.png', 44, 19, (14, 19), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_right.png', 14, 19, (29, 19), 180, None, (15, 14), True),
        (f'{texture_dir}entity\\chest\\normal_right.png', 14, 33, (43, 33), 180, None, (15, 10)),
        (f'{texture_dir}entity\\chest\\normal_right.png', 0, 33, (0, 33), 180, None, (14, 10)),
        (f'{texture_dir}entity\\chest\\normal_right.png', 73, 33, (14, 33), 180, None, (15, 10)),

        (f'{texture_dir}entity\\chest\\normal_left.png', 3, 1, (2, 1), 180, None, (1, 4), True), # right side
        (f'{texture_dir}entity\\chest\\normal_left.png', 2, 1, (3, 1), 180, None, (1, 4), True), # right front
        (f'{texture_dir}entity\\chest\\normal_left.png', 4, 1, (1, 1), 180, None, (1, 4), True), # back stage right
        (f'{texture_dir}entity\\chest\\normal_left.png', 4, 0, (1, 0), 180, None, (1, 1)), # bottom right
        (f'{texture_dir}entity\\chest\\normal_left.png', 2, 0, (2, 0), 180, None, (1, 1)), # top right

        (f'{texture_dir}entity\\chest\\normal_right.png', 0, 1, (0, 1), 180, None, (1, 4), True), # left side
        (f'{texture_dir}entity\\chest\\normal_right.png', 1, 1, (3, 1), 180, None, (1, 4), True), # left front
        (f'{texture_dir}entity\\chest\\normal_right.png', 5, 1, (1, 1), 180, None, (1, 4), True), # back stage left
        (f'{texture_dir}entity\\chest\\normal_right.png', 3, 0, (1, 0), 180, None, (1, 1)), # bottom left
        (f'{texture_dir}entity\\chest\\normal_right.png', 1, 0, (2, 0), 180, None, (1, 1)), # top left
    ]


def double_chest_1dot20(texture_dir):
    texture_list = chest_texture_list(texture_dir)
    return freeform_png('output\\assets\\minecraft\\textures\\entity\\chest\\normal_double.png', texture_list, 128, 64,
                        (15, 14))


def item_1dot5(texture_dir):
    errors = []
    texture_list = chest_texture_list(texture_dir)
    errors += freeform_png('output\\item\\largechest.png', texture_list, 128, 64,
                        (15, 14))
    file_list = [
        (f'{texture_dir}entity\\chest\\experience_orb.png', 'xporb.png'),
    ]
    errors += copy_and_rename_files('output\\item', file_list)
    return errors