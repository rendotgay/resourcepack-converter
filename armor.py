from logic import copy_and_rename_files


def armor_1dot21(texture_dir: str):
    file_list = [
        (f'{texture_dir}entity\\equipment\\humanoid\\chainmail.png', 'chainmail_layer_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\chainmail.png', 'chainmail_layer_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\diamond.png', 'diamond_layer_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\diamond.png', 'diamond_layer_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\gold.png', 'gold_layer_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\gold.png', 'gold_layer_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\iron.png', 'iron_layer_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\iron.png', 'iron_layer_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\netherite.png', 'netherite_layer_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\netherite.png', 'netherite_layer_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\leather.png', 'leather_layer_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\leather.png', 'leather_layer_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\leather_overlay.png', 'leather_layer_1_overlay.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\leather_overlay.png', 'leather_layer_2_overlay.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\turtle_scute.png', 'turtle_layer_1.png')
    ]
    return copy_and_rename_files('output\\assets\\minecraft\\textures\\models\\armor', file_list)


def armor_1dot5(texture_dir: str):
    file_list = [
        (f'{texture_dir}entity\\equipment\\humanoid\\chainmail.png', 'chain_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\chainmail.png', 'chain_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\diamond.png', 'diamond_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\diamond.png', 'diamond_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\gold.png', 'gold_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\gold.png', 'gold_2.png'),
        (f'{texture_dir}entity\\equipment\\humanoid\\iron.png', 'iron_1.png'),
        (f'{texture_dir}entity\\equipment\\humanoid_leggings\\iron.png', 'iron_2.png'),
        (f'{texture_dir}entity\\creeper\\creeper_armor.png', 'power.png'),
        (f'{texture_dir}entity\\wither\\wither_armor.png', 'witherarmor.png'),
    ]
    return copy_and_rename_files('output\\armor', file_list)