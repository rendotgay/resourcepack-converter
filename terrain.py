from logic import grid_png


def terrain_list(texture_dir: str):
    texture_list = [
        (f'{texture_dir}block\\grass_block_top.png', 0, 0),
        (f'{texture_dir}block\\stone.png', 0, 1),
        (f'{texture_dir}block\\dirt.png', 0, 2),
        (f'{texture_dir}block\\grass_block_side.png', 0, 3),
        (f'{texture_dir}block\\oak_planks.png', 0, 4),
        (f'{texture_dir}block\\smooth_stone_slab_side.png', 0, 5),
        (f'{texture_dir}block\\smooth_stone.png', 0, 6),
        (f'{texture_dir}block\\bricks.png', 0, 7),
        (f'{texture_dir}block\\tnt_side.png', 0, 8),
        (f'{texture_dir}block\\tnt_top.png', 0, 9),
        (f'{texture_dir}block\\tnt_bottom.png', 0, 10),
        (f'{texture_dir}block\\cobweb.png', 0, 11),
        (f'{texture_dir}block\\poppy.png', 0, 12),
        (f'{texture_dir}block\\dandelion.png', 0, 13),
        (f'{texture_dir}block\\nether_portal.png', 0, 14, (0, 0)),
        (f'{texture_dir}block\\oak_sapling.png', 0, 15),
        # first row done
        (f'{texture_dir}block\\cobblestone.png', 1, 0),
        (f'{texture_dir}block\\bedrock.png', 1, 1),
        (f'{texture_dir}block\\sand.png', 1, 2),
        (f'{texture_dir}block\\gravel.png', 1, 3),
        (f'{texture_dir}block\\oak_log.png', 1, 4),
        (f'{texture_dir}block\\oak_log_top.png', 1, 5),
        (f'{texture_dir}block\\iron_block.png', 1, 6),
        (f'{texture_dir}block\\gold_block.png', 1, 7),
        (f'{texture_dir}block\\diamond_block.png', 1, 8),
        # 9 is chest block (sometimes)
        # 10 is chest block (sometimes)
        # 11 is chest block (sometimes)
        (f'{texture_dir}block\\red_mushroom.png', 1, 12),
        (f'{texture_dir}block\\brown_mushroom.png', 1, 13),
        (f'{texture_dir}block\\jungle_sapling.png', 1, 14),
        # 15 is fire text
        # second row done
        (f'{texture_dir}block\\gold_ore.png', 2, 0),
        (f'{texture_dir}block\\iron_ore.png', 2, 1),
        (f'{texture_dir}block\\coal_ore.png', 2, 2),
        (f'{texture_dir}block\\bookshelf.png', 2, 3),
        (f'{texture_dir}block\\mossy_cobblestone.png', 2, 4),
        (f'{texture_dir}block\\obsidian.png', 2, 5),
        (f'{texture_dir}block\\grass_block_side_overlay.png', 2, 6),
        (f'{texture_dir}block\\grass.png', 2, 7),
        (f'{texture_dir}block\\grass_block_top.png', 2, 8),
        # 9 is chest block
        # 10 is chest block
        (f'{texture_dir}block\\crafting_table_top.png', 2, 11),
        (f'{texture_dir}block\\furnace_front.png', 2, 12),
        (f'{texture_dir}block\\furnace_side.png', 2, 13),
        (f'{texture_dir}block\\dispenser_front.png', 2, 14),
        # 15 is fire text
        # third row done
        (f'{texture_dir}block\\sponge.png', 3, 0),
        (f'{texture_dir}block\\glass.png', 3, 1),
        (f'{texture_dir}block\\diamond_ore.png', 3, 2),
        (f'{texture_dir}block\\redstone_ore.png', 3, 3),
        (f'{texture_dir}block\\oak_leaves.png', 3, 4),
        (f'{texture_dir}block\\oak_leaves.png', 3, 5, None, None, (44, 44, 44)),
        (f'{texture_dir}block\\stone_bricks.png', 3, 6),
        (f'{texture_dir}block\\dead_bush.png', 3, 7),
        (f'{texture_dir}block\\fern.png', 3, 8),
        # 9 is chest block
        # 10 is chest block
        (f'{texture_dir}block\\crafting_table_side.png', 3, 11),
        (f'{texture_dir}block\\crafting_table_front.png', 3, 12),
        (f'{texture_dir}block\\furnace_front_on.png', 3, 13, (0, 0)),
        (f'{texture_dir}block\\furnace_top.png', 3, 14),
        (f'{texture_dir}block\\spruce_sapling.png', 3, 15),
        # fourth row done
        (f'{texture_dir}block\\white_wool.png', 4, 0),
        (f'{texture_dir}block\\spawner.png', 4, 1),
        (f'{texture_dir}block\\snow.png', 4, 2),
        (f'{texture_dir}block\\ice.png', 4, 3),
        (f'{texture_dir}block\\grass_block_snow.png', 4, 4),
        (f'{texture_dir}block\\cactus_top.png', 4, 5),
        (f'{texture_dir}block\\cactus_side.png', 4, 6),
        (f'{texture_dir}block\\cactus_bottom.png', 4, 7),
        (f'{texture_dir}block\\clay.png', 4, 8),
        (f'{texture_dir}block\\sugar_cane.png', 4, 9),
        (f'{texture_dir}block\\jukebox_side.png', 4, 10),
        (f'{texture_dir}block\\jukebox_top.png', 4, 11),
        (f'{texture_dir}block\\lily_pad.png', 4, 12),
        (f'{texture_dir}block\\mycelium_side.png', 4, 13),
        (f'{texture_dir}block\\mycelium_top.png', 4, 14),
        (f'{texture_dir}block\\birch_sapling.png', 4, 15),
        # fifth row done
        (f'{texture_dir}block\\torch.png', 5, 0),
        (f'{texture_dir}block\\oak_door_top.png', 5, 1),
        (f'{texture_dir}block\\iron_door_top.png', 5, 2),
        (f'{texture_dir}block\\ladder.png', 5, 3),
        (f'{texture_dir}block\\oak_trapdoor.png', 5, 4),
        (f'{texture_dir}block\\iron_bars.png', 5, 5),
        (f'{texture_dir}block\\farmland_moist.png', 5, 6),
        (f'{texture_dir}block\\farmland.png', 5, 7),
        (f'{texture_dir}block\\wheat_stage0.png', 5, 8),
        (f'{texture_dir}block\\wheat_stage1.png', 5, 9),
        (f'{texture_dir}block\\wheat_stage2.png', 5, 10),
        (f'{texture_dir}block\\wheat_stage3.png', 5, 11),
        (f'{texture_dir}block\\wheat_stage4.png', 5, 12),
        (f'{texture_dir}block\\wheat_stage5.png', 5, 13),
        (f'{texture_dir}block\\wheat_stage6.png', 5, 14),
        (f'{texture_dir}block\\wheat_stage7.png', 5, 15),
        # sixth row done
        (f'{texture_dir}block\\lever.png', 6, 0),
        (f'{texture_dir}block\\oak_door_bottom.png', 6, 1),
        (f'{texture_dir}block\\iron_door_bottom.png', 6, 2),
        (f'{texture_dir}block\\redstone_torch.png', 6, 3),
        (f'{texture_dir}block\\mossy_stone_bricks.png', 6, 4),
        (f'{texture_dir}block\\cracked_stone_bricks.png', 6, 5),
        (f'{texture_dir}block\\pumpkin_top.png', 6, 6),
        (f'{texture_dir}block\\netherrack.png', 6, 7),
        (f'{texture_dir}block\\soul_sand.png', 6, 8),
        (f'{texture_dir}block\\glowstone.png', 6, 9),
        (f'{texture_dir}block\\piston_top_sticky.png', 6, 10),
        (f'{texture_dir}block\\piston_top.png', 6, 11),
        (f'{texture_dir}block\\piston_side.png', 6, 12),
        (f'{texture_dir}block\\piston_bottom.png', 6, 13),
        (f'{texture_dir}block\\piston_inner.png', 6, 14),
        (f'{texture_dir}block\\melon_stem.png', 6, 15),
        # seventh row done
        (f'{texture_dir}block\\rail_corner.png', 7, 0),
        (f'{texture_dir}block\\black_wool.png', 7, 1),
        (f'{texture_dir}block\\gray_wool.png', 7, 2),
        (f'{texture_dir}block\\redstone_torch_off.png', 7, 3),
        (f'{texture_dir}block\\spruce_log.png', 7, 4),
        (f'{texture_dir}block\\birch_log.png', 7, 5),
        (f'{texture_dir}block\\pumpkin_side.png', 7, 6),
        (f'{texture_dir}block\\carved_pumpkin.png', 7, 7),
        (f'{texture_dir}block\\jack_o_lantern.png', 7, 8),
        (f'{texture_dir}block\\cake_top.png', 7, 9),
        (f'{texture_dir}block\\cake_side.png', 7, 10),
        (f'{texture_dir}block\\cake_inner.png', 7, 11),
        (f'{texture_dir}block\\cake_bottom.png', 7, 12),
        (f'{texture_dir}block\\red_mushroom_block.png', 7, 13),
        (f'{texture_dir}block\\brown_mushroom_block.png', 7, 14),
        (f'{texture_dir}block\\attached_melon_stem.png', 7, 15),
        # eighth row done
        (f'{texture_dir}block\\rail.png', 8, 0),
        (f'{texture_dir}block\\red_wool.png', 8, 1),
        (f'{texture_dir}block\\pink_wool.png', 8, 2),
        (f'{texture_dir}block\\repeater.png', 8, 3),
        (f'{texture_dir}block\\spruce_leaves.png', 8, 4),  # not positive what leaves these are
        (f'{texture_dir}block\\spruce_leaves.png', 8, 5, None, None, (49, 49, 49)),
        (f'{texture_dir}entity\\bed\\red.png', 8, 6, (6, 28), 270),
        (f'{texture_dir}entity\\bed\\red.png', 8, 7, (6, 6), 270),
        (f'{texture_dir}block\\melon_side.png', 8, 8),
        (f'{texture_dir}block\\melon_top.png', 8, 9),
        (f'{texture_dir}block\\cauldron_top.png', 8, 10),
        (f'{texture_dir}block\\cauldron_inner.png', 8, 11),
        (f'{texture_dir}item\\cake.png', 8, 12),
        (f'{texture_dir}block\\mushroom_stem.png', 8, 13),
        (f'{texture_dir}block\\mushroom_block_inside.png', 8, 14),
        (f'{texture_dir}block\\vine.png', 8, 15),
        # ninth row done
        (f'{texture_dir}block\\lapis_block.png', 9, 0),
        (f'{texture_dir}block\\green_wool.png', 9, 1),
        (f'{texture_dir}block\\lime_wool.png', 9, 2),
        (f'{texture_dir}block\\repeater_on.png', 9, 3),
        (f'{texture_dir}block\\glass_pane_top.png', 9, 4),
        # 5 is end of bed which is in entity and needs cropping
        # 6 is bottom side of bed which is in entity and needs cropping
        # 7 is top side of bed which is in entity and needs cropping
        # 8 is start of bed which is in entity and needs cropping
        (f'{texture_dir}block\\jungle_log.png', 9, 9),
        (f'{texture_dir}block\\cauldron_side.png', 9, 10),
        (f'{texture_dir}block\\cauldron_bottom.png', 9, 11),
        (f'{texture_dir}block\\brewing_stand_base.png', 9, 12),
        (f'{texture_dir}block\\brewing_stand.png', 9, 13),
        (f'{texture_dir}block\\end_portal_frame_top.png', 9, 14),
        (f'{texture_dir}block\\end_portal_frame_side.png', 9, 15),
        # tenth row done
        (f'{texture_dir}block\\lapis_ore.png', 10, 0),
        (f'{texture_dir}block\\brown_wool.png', 10, 1),
        (f'{texture_dir}block\\yellow_wool.png', 10, 2),
        (f'{texture_dir}block\\powered_rail.png', 10, 3),
        (f'{texture_dir}block\\redstone_dust_dot.png', 10, 4),
        (f'{texture_dir}block\\redstone_dust_line0.png', 10, 5, None, 90),
        # 5 is redstone_dust_line0 but rotated
        (f'{texture_dir}block\\enchanting_table_top.png', 10, 6),
        (f'{texture_dir}block\\dragon_egg.png', 10, 7),
        (f'{texture_dir}block\\cocoa_stage2.png', 10, 8),
        (f'{texture_dir}block\\cocoa_stage1.png', 10, 9),
        (f'{texture_dir}block\\cocoa_stage0.png', 10, 10),
        (f'{texture_dir}block\\emerald_ore.png', 10, 11),
        (f'{texture_dir}block\\tripwire_hook.png', 10, 12),
        (f'{texture_dir}block\\tripwire.png', 10, 13),
        (f'{texture_dir}block\\end_portal_frame_eye.png', 10, 14),
        (f'{texture_dir}block\\end_stone.png', 10, 15),
        # eleventh row done
        (f'{texture_dir}block\\sandstone_top.png', 11, 0),
        (f'{texture_dir}block\\blue_wool.png', 11, 1),
        (f'{texture_dir}block\\light_blue_wool.png', 11, 2),
        (f'{texture_dir}block\\powered_rail_on.png', 11, 3),
        # 4 is empty?
        # 5 is empty?
        (f'{texture_dir}block\\enchanting_table_side.png', 11, 6),
        (f'{texture_dir}block\\enchanting_table_bottom.png', 11, 7),  # is literally just obsidian by default
        (f'{texture_dir}block\\command_block_back.png', 11, 8, (0, 0)),
        (f'{texture_dir}block\\item_frame.png', 11, 9),
        (f'{texture_dir}block\\flower_pot.png', 11, 10),
        (f'{texture_dir}block\\comparator.png', 11, 11),
        (f'{texture_dir}block\\comparator_on.png', 11, 12),
        ('missing.png', 11, 13),
        ('missing.png', 11, 14),
        (f'{texture_dir}block\\nether_quartz_ore.png', 11, 15),
        # twelfth row done
        (f'{texture_dir}block\\sandstone.png', 12, 0),
        (f'{texture_dir}block\\purple_wool.png', 12, 1),
        (f'{texture_dir}block\\magenta_wool.png', 12, 2),
        (f'{texture_dir}block\\detector_rail.png', 12, 3),
        (f'{texture_dir}block\\jungle_leaves.png', 12, 4),
        (f'{texture_dir}block\\jungle_leaves.png', 12, 5, None, None, (75, 75, 75)),
        (f'{texture_dir}block\\spruce_planks.png', 12, 6),
        (f'{texture_dir}block\\jungle_planks.png', 12, 7),
        (f'{texture_dir}block\\carrots_stage0.png', 12, 8),
        (f'{texture_dir}block\\carrots_stage1.png', 12, 9),
        (f'{texture_dir}block\\carrots_stage2.png', 12, 10),
        (f'{texture_dir}block\\carrots_stage3.png', 12, 11),
        (f'{texture_dir}block\\potatoes_stage3.png', 12, 12),  # i think this is fully grown potatoes?
        # 13 is flowing water
        # 14 is flowing water
        # 15 is flowing water
        # thirteenth row done
        (f'{texture_dir}block\\sandstone_bottom.png', 13, 0),
        (f'{texture_dir}block\\cyan_wool.png', 13, 1),
        (f'{texture_dir}block\\orange_wool.png', 13, 2),
        (f'{texture_dir}block\\redstone_lamp.png', 13, 3),
        (f'{texture_dir}block\\redstone_lamp_on.png', 13, 4),
        (f'{texture_dir}block\\chiseled_stone_bricks.png', 13, 5),
        (f'{texture_dir}block\\birch_planks.png', 13, 6),
        (f'{texture_dir}block\\anvil.png', 13, 7),
        (f'{texture_dir}block\\chipped_anvil_top.png', 13, 8),
        ('missing.png', 13, 9),
        ('missing.png', 13, 10),
        ('missing.png', 13, 11),
        ('missing.png', 13, 12),
        ('missing.png', 13, 13),
        # 14 is flowing water
        # 15 is flowing water
        # fourteenth row done
        (f'{texture_dir}block\\nether_bricks.png', 14, 0),
        (f'{texture_dir}block\\light_gray_wool.png', 14, 1),
        (f'{texture_dir}block\\nether_wart_stage0.png', 14, 2),
        (f'{texture_dir}block\\nether_wart_stage1.png', 14, 3),
        (f'{texture_dir}block\\nether_wart_stage2.png', 14, 4),
        (f'{texture_dir}block\\chiseled_sandstone.png', 14, 5),
        (f'{texture_dir}block\\cut_sandstone.png', 14, 6),
        (f'{texture_dir}block\\anvil_top.png', 14, 7),
        (f'{texture_dir}block\\damaged_anvil_top.png', 14, 8),
        ('missing.png', 13, 9),
        ('missing.png', 13, 10),
        ('missing.png', 13, 11),
        # 12 is WIP
        # 13 is flowing lava
        # 14 is flowing lava
        # 15 is flowing lava
        # fifteenth row done
        (f'{texture_dir}block\\destroy_stage_0.png', 15, 0),
        (f'{texture_dir}block\\destroy_stage_1.png', 15, 1),
        (f'{texture_dir}block\\destroy_stage_2.png', 15, 2),
        (f'{texture_dir}block\\destroy_stage_3.png', 15, 3),
        (f'{texture_dir}block\\destroy_stage_4.png', 15, 4),
        (f'{texture_dir}block\\destroy_stage_5.png', 15, 5),
        (f'{texture_dir}block\\destroy_stage_6.png', 15, 6),
        (f'{texture_dir}block\\destroy_stage_7.png', 15, 7),
        (f'{texture_dir}block\\destroy_stage_8.png', 15, 8),
        (f'{texture_dir}block\\destroy_stage_9.png', 15, 9),
        # 10 is some kind of particle
        # 11 is some kind of particle
        # 12 is some kind of particle
        # 13 is some kind of particle
        # 14 is flowing lava
        # 15 is flowing lava
    ]
    return texture_list


# TODO: chests for 1.3 and blocks for 1.5
def terrain_1dot5(texture_dir: str, jar_path=None):
    texture_list = terrain_list(texture_dir)
    texture_list += [
        (f'{texture_dir}block\\emerald_block.png', 1, 9),
        (f'{texture_dir}block\\redstone_block.png', 1, 10),
        ('missing.png', 1, 11),
        (f'{texture_dir}block\\beacon.png', 2, 9, (0, 272)),
        ('missing.png', 2, 10),
        (f'{texture_dir}block\\daylight_detector_top.png', 3, 9),
        (f'{texture_dir}block\\daylight_detector_side.png', 3, 10),
    ]
    paths = (jar_path, texture_dir)
    return grid_png('output\\terrain.png', texture_list, paths=paths)


def terrain_1dot3(texture_dir: str, jar_path=None):
    texture_list = terrain_list(texture_dir)
    texture_list += [
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 1, 9, (0, 0)),
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 1, 10, (16, 16)),
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 1, 11, (16, 0)),
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 2, 9, (48, 0)),
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 2, 10, (48, 16)),
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 3, 9, (32, 32)),
        (f'{texture_dir}entity\\chest\\fullsize_chest.png', 3, 10, (48, 32)),
    ]
    paths = (jar_path, texture_dir)
    return grid_png('output\\terrain.png', texture_list, paths=paths)


def terrain_tu18(texture_dir: str, jar_path=None):
    texture_list = terrain_list(texture_dir)
    texture_list += [
        (f'{texture_dir}block\\emerald_block.png', 1, 9),
        (f'{texture_dir}block\\redstone_block.png', 1, 10),
        (f'{texture_dir}block\\dropper_front.png', 1, 11),
        (f'{texture_dir}block\\beacon.png', 2, 9, (0, 272)),
        (f'{texture_dir}block\\dropper_front_vertical.png', 2, 10),
        ('missing.png', 2, 10),
        (f'{texture_dir}block\\daylight_detector_top.png', 3, 9),
        (f'{texture_dir}block\\daylight_detector_side.png', 3, 10),
        (f'{texture_dir}block\\activator_rail.png', 11, 13),
        (f'{texture_dir}block\\activator_rail_on.png', 11, 14),
        # Some of these quartz textures (specifically quartz_block) might need changing
        (f'{texture_dir}block\\chiseled_quartz_block_top.png', 13, 9),
        (f'{texture_dir}block\\quartz_pillar_top.png', 13, 10),
        (f'{texture_dir}block\\quartz_block_bottom.png', 13, 11),
        # no clue what 13,12 is supposed to be??? looks like a stone wood? cauldron_side????
        (f'{texture_dir}block\\detector_rail_on.png', 13, 13),
        (f'{texture_dir}block\\chiseled_quartz_block.png', 14, 9),
        (f'{texture_dir}block\\quartz_pillar.png', 14, 10),
        (f'{texture_dir}block\\quartz_block_bottom.png', 14, 11),
        (f'{texture_dir}block\\cauldron_inner.png', 14, 12),
        (f'{texture_dir}block\\hay_block_side.png', 15, 10),
        (f'{texture_dir}block\\quartz_block_top.png', 15, 11),
        (f'{texture_dir}block\\cauldron_top.png', 15, 12),
        (f'{texture_dir}block\\hay_block_top.png', 15, 13),
        ('missing.png', 13, 9),
        ('missing.png', 13, 10),
        ('missing.png', 13, 11),
    ]
    paths = (jar_path, texture_dir)
    return grid_png('output\\terrain.png', texture_list, paths=paths)