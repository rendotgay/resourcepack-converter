from logic import grid_png, freeform_png, copy_and_rename_files


def bars_1dot20(texture_dir, jar_path=None):
    texture_list = [
        (f'{texture_dir}gui\\sprites\\boss_bar\\pink_background.png', 0, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\pink_progress.png', 1, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\blue_background.png', 2, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\blue_progress.png', 3, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\red_background.png', 4, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\red_progress.png', 5, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\green_background.png', 6, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\green_progress.png', 7, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\yellow_background.png', 8, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\yellow_progress.png', 9, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\purple_background.png', 10, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\purple_progress.png', 11, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\white_background.png', 12, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\white_progress.png', 13, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_6_background.png', 16, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_6_background.png', 17, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_10_background.png', 18, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_10_background.png', 19, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_12_background.png', 20, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_12_background.png', 21, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_20_background.png', 22, 0),
        (f'{texture_dir}gui\\sprites\\boss_bar\\notched_20_background.png', 23, 0),
    ]
    paths = (jar_path, texture_dir)
    return grid_png('output\\assets\\minecraft\\textures\\gui\\bars.png', texture_list, grid_width=182,
                       grid_height=5, paths=paths)


def icons_1dot20(texture_dir, jar_path=None):
    texture_list = [
        (f'{texture_dir}gui\\sprites\\hud\\crosshair.png', 0, 0, None, None, None, (15, 15)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container.png', 16, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_blinking.png', 25, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_hardcore.png', 34, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_hardcore_blinking.png', 43, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\full.png', 52, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\half.png', 61, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\full_blinking.png', 70, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\half_blinking.png', 79, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_full.png', 88, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_half.png', 97, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_full_blinking.png', 106, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_half_blinking.png', 115, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_full.png', 124, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_half.png', 133, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_full_blinking.png', 142, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_half_blinking.png', 151, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\absorbing_full.png', 160, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\absorbing_half.png', 169, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\frozen_full.png', 178, 0, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\frozen_half.png', 187, 0, None, None, None, (9, 9)),
    # first row done
        (f'{texture_dir}gui\\sprites\\hud\\armor_empty.png', 16, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\armor_half.png', 25, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\armor_full.png', 34, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\armor_full.png', 43, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container.png', 52, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_blinking.png', 61, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_hardcore.png', 70, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_hardcore_blinking.png', 79, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\vehicle_full.png', 88, 9, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\vehicle_half.png', 97 , 9, None, None, None, (9, 9)),
        # vehicle blinking exists on icons.png, but doesn't seem to have a texture
    # second row done
        (f'{texture_dir}gui\\sprites\\icon\\ping_5.png', 0, 16, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\icon\\ping_4.png', 0, 24, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\icon\\ping_3.png', 0, 32, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\icon\\ping_2.png', 0, 40, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\icon\\ping_1.png', 0, 48, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\icon\\ping_unknown.png', 0, 56, None, None, None, (10, 8)),
    # network icons done
        (f'{texture_dir}gui\\sprites\\hud\\air.png', 16, 18, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\air_bursting.png', 25, 18, None, None, None, (9, 9)),
        # blue armor icon. unsure if used.
    # third row done
        (f'{texture_dir}gui\\sprites\\hud\\food_empty.png', 16, 27, None, None, None, (9, 9)),
        # food blinking? hardcore food blinking?
        (f'{texture_dir}gui\\sprites\\hud\\food_full.png', 52, 27, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\food_half.png', 61, 27, None, None, None, (9, 9)),
        # more food blinking
        (f'{texture_dir}gui\\sprites\\hud\\food_full_hunger.png', 88, 27, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\food_half_hunger.png', 97, 27, None, None, None, (9, 9)),
        # more food blinking and missing empty
        (f'{texture_dir}gui\\sprites\\hud\\food_empty_hunger.png', 133, 27, None, None, None, (9, 9)),
    # fourth row done
    # fifth row is flipped hunger with outline, unsure if used
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container.png', 16, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_blinking.png', 25, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_hardcore.png', 34, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\container_hardcore_blinking.png', 43, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\hardcore_full.png', 52, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\hardcore_half.png', 61, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\hardcore_full_blinking.png', 70, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\hardcore_half_blinking.png', 79, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_hardcore_full.png', 88, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_hardcore_half.png', 97, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_hardcore_full_blinking.png', 106, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\poisoned_hardcore_half_blinking.png', 115, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_hardcore_full.png', 124, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_hardcore_half.png', 133, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_hardcore_full_blinking.png', 142, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\withered_hardcore_half_blinking.png', 151, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\absorbing_hardcore_full.png', 160, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\absorbing_hardcore_half.png', 169, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\frozen_hardcore_full.png', 178, 45, None, None, None, (9, 9)),
        (f'{texture_dir}gui\\sprites\\hud\\heart\\frozen_hardcore_half.png', 187, 45, None, None, None, (9, 9)),
    # heart rows done
        (f'{texture_dir}gui\\sprites\\hud\\experience_bar_background.png', 0, 64, None, None, None, (182, 5)),
        (f'{texture_dir}gui\\sprites\\hud\\experience_bar_progress.png', 0, 69, None, None, None, (182, 5)),
        (f'{texture_dir}gui\\sprites\\hud\\jump_bar_cooldown.png', 0, 74, None, None, None, (182, 5)), # similar to pink boss bar
        # i would assume this is another jump bar cooldown, but a texture doesnt exist. its probably identical to the pink boss bar
        (f'{texture_dir}gui\\sprites\\hud\\jump_bar_background.png', 0, 84, None, None, None, (182, 5)),
        (f'{texture_dir}gui\\sprites\\hud\\jump_bar_progress.png', 0, 89, None, None, None, (182, 5)),
    # bars rows done
        (f'{texture_dir}gui\\sprites\\hud\\hotbar_attack_indicator_background.png', 0, 94, None, None, None, (18, 18)),
        (f'{texture_dir}gui\\sprites\\hud\\hotbar_attack_indicator_progress.png', 18, 94, None, None, None, (18, 18)),
        (f'{texture_dir}gui\\sprites\\hud\\crosshair_attack_indicator_background.png', 36, 94, None, None, None, (16, 4)),
        (f'{texture_dir}gui\\sprites\\hud\\crosshair_attack_indicator_progress.png', 52, 94, None, None, None, (16, 4)),
        (f'{texture_dir}gui\\sprites\\hud\\crosshair_attack_indicator_full.png', 68, 94, None, None, None, (16, 16)),
    # attack indicator row done
        (f'{texture_dir}gui\\sprites\\server_list\\ping_5.png', 0, 177, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\ping_4.png', 0, 185, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\ping_3.png', 0, 193, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\ping_2.png', 0, 201, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\ping_1.png', 0, 209, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\unreachable.png', 0, 217, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\pinging_1.png', 10, 177, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\pinging_2.png', 10, 185, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\pinging_3.png', 10, 193, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\pinging_4.png', 10, 201, None, None, None, (10, 8)),
        (f'{texture_dir}gui\\sprites\\server_list\\pinging_5.png', 10, 209, None, None, None, (10, 8)),
        # no idea what those circles are at the bottom, hopefully unused
    ]
    paths = (jar_path, texture_dir)
    return freeform_png('output\\assets\\minecraft\\textures\\gui\\icons.png', texture_list, paths=paths)


def widgets_1dot20(texture_dir, jar_path=None):
    texture_list = [
        (f'{texture_dir}gui\\sprites\\hud\\hotbar.png', 0, 0, None, None, None, (182, 22)),
        (f'{texture_dir}gui\\sprites\\hud\\hotbar_selection.png', 0, 22, None, None, None, (24, 23)),
        (f'{texture_dir}gui\\sprites\\hud\\hotbar_offhand_left.png', 24, 22, None, None, None, (29, 24)),
        (f'{texture_dir}gui\\sprites\\hud\\hotbar_offhand_right.png', 53, 22, None, None, None, (29, 24)),
        (f'{texture_dir}gui\\sprites\\widget\\button_disabled.png', 0, 46, None, None, None, (200, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\button.png', 0, 66, None, None, None, (200, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\button_highlighted.png', 0, 86, None, None, None, (200, 20)),
        # language icon is split for some fuckass reason
        (f'{texture_dir}gui\\sprites\\widget\\locked_button.png', 0, 146, None, None, None, (20, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\unlocked_button.png', 20, 146, None, None, None, (20, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\locked_button_highlighted.png', 0, 166, None, None, None, (20, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\unlocked_button_highlighted.png', 20, 166, None, None, None, (20, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\locked_button_disabled.png', 0, 186, None, None, None, (20, 20)),
        (f'{texture_dir}gui\\sprites\\widget\\unlocked_button_disabled.png', 20, 186, None, None, None, (20, 20)),
        (f'{texture_dir}gui\\sprites\\notification\\1.png', 198, 22, None, None, None, (8, 8)),
        (f'{texture_dir}gui\\sprites\\notification\\2.png', 198, 30, None, None, None, (8, 8)),
        (f'{texture_dir}gui\\sprites\\notification\\3.png', 198, 38, None, None, None, (8, 8)),
        (f'{texture_dir}gui\\sprites\\notification\\4.png', 198, 46, None, None, None, (8, 8)),
        (f'{texture_dir}gui\\sprites\\notification\\5.png', 198, 54, None, None, None, (8, 8)),
        (f'{texture_dir}gui\\sprites\\notification\\more.png', 198, 62, None, None, None, (8, 8)),
        (f'{texture_dir}gui\\sprites\\icon\\draft_report.png', 182, 24, None, None, None, (15, 15)), # this is highlighted but again i cannot find the file
        (f'{texture_dir}gui\\sprites\\icon\\draft_report.png', 167, 24, None, None, None, (15, 15)),
        (f'{texture_dir}gui\\sprites\\hud\\crosshair.png', 240, 0, None, None, None, (15, 15)),
        # idk what those stoplight lookin things are atm
    ]
    paths = (jar_path, texture_dir)
    return freeform_png('output\\assets\\minecraft\\textures\\gui\\widgets.png', texture_list, paths=paths)


def items_1dot5(texture_dir, jar_path=None):
    texture_list = [
        # leather items will be interesting because of overlay
        (f'{texture_dir}item\\chainmail_helmet.png', 0, 1),
        (f'{texture_dir}item\\chainmail_chestplate.png', 1, 1),
        (f'{texture_dir}item\\chainmail_leggings.png', 2, 1),
        (f'{texture_dir}item\\chainmail_boots.png', 3, 1),
        (f'{texture_dir}item\\iron_helmet.png', 0, 2),
        (f'{texture_dir}item\\iron_chestplate.png', 1, 2),
        (f'{texture_dir}item\\iron_leggings.png', 2, 2),
        (f'{texture_dir}item\\iron_boots.png', 3, 2),
        (f'{texture_dir}item\\diamond_helmet.png', 0, 3),
        (f'{texture_dir}item\\diamond_chestplate.png', 1, 3),
        (f'{texture_dir}item\\diamond_leggings.png', 2, 3),
        (f'{texture_dir}item\\diamond_boots.png', 3, 3),
        (f'{texture_dir}item\\golden_helmet.png', 0, 4),
        (f'{texture_dir}item\\golden_chestplate.png', 1, 4),
        (f'{texture_dir}item\\golden_leggings.png', 2, 4),
        (f'{texture_dir}item\\golden_boots.png', 3, 4),
        # armor done
        (f'{texture_dir}item\\wooden_sword.png', 4, 0),
        (f'{texture_dir}item\\wooden_shovel.png', 5, 0),
        (f'{texture_dir}item\\wooden_pickaxe.png', 6, 0),
        (f'{texture_dir}item\\wooden_axe.png', 7, 0),
        (f'{texture_dir}item\\wooden_hoe.png', 8, 0),
        (f'{texture_dir}item\\stone_sword.png', 4, 1),
        (f'{texture_dir}item\\stone_shovel.png', 5, 1),
        (f'{texture_dir}item\\stone_pickaxe.png', 6, 1),
        (f'{texture_dir}item\\stone_axe.png', 7, 1),
        (f'{texture_dir}item\\stone_hoe.png', 8, 1),
        (f'{texture_dir}item\\iron_sword.png', 4, 2),
        (f'{texture_dir}item\\iron_shovel.png', 5, 2),
        (f'{texture_dir}item\\iron_pickaxe.png', 6, 2),
        (f'{texture_dir}item\\iron_axe.png', 7, 2),
        (f'{texture_dir}item\\iron_hoe.png', 8, 2),
        (f'{texture_dir}item\\diamond_sword.png', 4, 3),
        (f'{texture_dir}item\\diamond_shovel.png', 5, 3),
        (f'{texture_dir}item\\diamond_pickaxe.png', 6, 3),
        (f'{texture_dir}item\\diamond_axe.png', 7, 3),
        (f'{texture_dir}item\\diamond_hoe.png', 8, 3),
        (f'{texture_dir}item\\golden_sword.png', 4, 4),
        (f'{texture_dir}item\\golden_shovel.png', 5, 4),
        (f'{texture_dir}item\\golden_pickaxe.png', 6, 4),
        (f'{texture_dir}item\\golden_axe.png', 7, 4),
        (f'{texture_dir}item\\golden_hoe.png', 8, 4),
        # tools done
        (f'{texture_dir}item\\flint_and_steel.png', 0, 5),
        (f'{texture_dir}item\\bow.png', 1, 5),
        (f'{texture_dir}item\\arrow.png', 2, 5),
        (f'{texture_dir}item\\stick.png', 3, 5),
        (f'{texture_dir}item\\fishing_rod.png', 4, 5),
        (f'{texture_dir}item\\fishing_rod_cast.png', 5, 5),
        (f'{texture_dir}item\\bow_pulling_0.png', 6, 5),
        (f'{texture_dir}item\\bow_pulling_1.png', 7, 5),
        (f'{texture_dir}item\\bow_pulling_1.png', 8, 5),

        (f'{texture_dir}item\\flint.png', 0, 6),
        (f'{texture_dir}item\\brick.png', 1, 6),
        # 2 is fletcher bag thing
        # 3 is compass but its been split into 32 textures
        # 4 is clock but its been split into 64 textures
        (f'{texture_dir}item\\repeater.png', 5, 6),
        (f'{texture_dir}item\\carrot_on_a_stick.png', 6, 6),
        (f'{texture_dir}item\\baked_potato.png', 7, 6),
        (f'{texture_dir}item\\poisonous_potato.png', 8, 6),
        (f'{texture_dir}item\\golden_carrot.png', 9, 6),

        (f'{texture_dir}item\\coal.png', 0, 7),
        (f'{texture_dir}item\\iron_ingot.png', 1, 7),
        (f'{texture_dir}item\\gold_ingot.png', 2, 7),
        (f'{texture_dir}item\\diamond.png', 3, 7, (0, 0)),
        (f'{texture_dir}item\\bowl.png', 4, 7),
        (f'{texture_dir}item\\porkchop.png', 5, 7),
        (f'{texture_dir}item\\leather.png', 6, 7),
        (f'{texture_dir}item\\potato.png', 7, 7),
        (f'{texture_dir}item\\minecart.png', 8, 7),
        (f'{texture_dir}item\\chest_minecart.png', 9, 7),
        (f'{texture_dir}item\\furnace_minecart.png', 10, 7),

        (f'{texture_dir}item\\string.png', 0, 8),
        (f'{texture_dir}item\\feather.png', 1, 8),
        (f'{texture_dir}item\\gunpowder.png', 2, 8),
        (f'{texture_dir}item\\redstone.png', 3, 8),
        (f'{texture_dir}item\\mushroom_stew.png', 4, 8),
        (f'{texture_dir}item\\cooked_porkchop.png', 5, 8),
        (f'{texture_dir}item\\saddle.png', 6, 8),
        (f'{texture_dir}item\\oak_boat.png', 8, 8),
        (f'{texture_dir}item\\pumpkin_pie.png', 8, 8),

        (f'{texture_dir}item\\wheat_seeds.png', 0, 9),
        (f'{texture_dir}item\\wheat.png', 1, 9),
        (f'{texture_dir}item\\bread.png', 2, 9),
        (f'{texture_dir}item\\clay_ball.png', 3, 9),
        (f'{texture_dir}item\\glowstone_dust.png', 4, 9),
        (f'{texture_dir}item\\cod.png', 5, 9), # only like half sure this is cod lmao
        (f'{texture_dir}item\\beef.png', 6, 9),
        (f'{texture_dir}item\\chicken.png', 7, 9),
        (f'{texture_dir}item\\glistering_melon_slice.png', 8, 9),
        # 9 is spawn egg no colors
        # 10 is spawn egg overlay no colors
        (f'{texture_dir}item\\nether_star.png', 11, 9),
        (f'{texture_dir}item\\firework_rocket.png', 12, 9),

        (f'{texture_dir}item\\apple.png', 0, 10),
        (f'{texture_dir}item\\painting.png', 1, 10),
        (f'{texture_dir}item\\oak_sign.png', 2, 10),
        (f'{texture_dir}item\\paper.png', 3, 10),
        (f'{texture_dir}item\\bucket.png', 4, 10),
        (f'{texture_dir}item\\cooked_cod.png', 5, 10), # only like half sure this is cod lmao
        (f'{texture_dir}item\\cooked_beef.png', 6, 10),
        (f'{texture_dir}item\\cooked_chicken.png', 7, 10),
        (f'{texture_dir}item\\fermented_spider_eye.png', 8, 10),
        (f'{texture_dir}item\\splash_potion.png', 9, 10),
        # 10 is ruby
        (f'{texture_dir}item\\emerald.png', 10, 10),
        (f'{texture_dir}item\\firework_star.png', 11, 10),

        (f'{texture_dir}item\\golden_apple.png', 0, 11),
        (f'{texture_dir}item\\sugar_cane.png', 1, 11),
        (f'{texture_dir}item\\oak_door.png', 2, 11),
        (f'{texture_dir}item\\book.png', 3, 11),
        (f'{texture_dir}item\\water_bucket.png', 4, 11),
        (f'{texture_dir}item\\rotten_flesh.png', 5, 11),
        (f'{texture_dir}item\\ender_pearl.png', 6, 11),
        (f'{texture_dir}item\\ghast_tear.png', 7, 11),
        (f'{texture_dir}item\\spider_eye.png', 8, 11),
        (f'{texture_dir}item\\ender_eye.png', 9, 11, (0, 0)),
        (f'{texture_dir}item\\experience_bottle.png', 10, 11),
        (f'{texture_dir}item\\writable_book.png', 11, 11),
        (f'{texture_dir}item\\firework_star_overlay.png', 12, 11),

        (f'{texture_dir}item\\egg.png', 0, 12),
        (f'{texture_dir}item\\bone.png', 1, 12),
        (f'{texture_dir}item\\iron_door.png', 2, 12),
        (f'{texture_dir}item\\map.png', 3, 12), # has filled map markings overlay graah
        (f'{texture_dir}item\\lava_bucket.png', 4, 12),
        (f'{texture_dir}item\\cookie.png', 5, 12),
        (f'{texture_dir}item\\blaze_rod.png', 6, 12),
        (f'{texture_dir}item\\gold_nugget.png', 7, 12),
        (f'{texture_dir}item\\glass_bottle.png', 8, 12),
        (f'{texture_dir}item\\cauldron.png', 9, 12),
        (f'{texture_dir}item\\brewing_stand.png', 10, 12),
        (f'{texture_dir}item\\written_book.png', 11, 12),

        (f'{texture_dir}item\\sugar.png', 0, 13),
        (f'{texture_dir}item\\cake.png', 1, 13),
        (f'{texture_dir}item\\bed.png', 2, 13),
        (f'{texture_dir}item\\pumpkin_seeds.png', 3, 13),
        (f'{texture_dir}item\\milk_bucket.png', 4, 13),
        (f'{texture_dir}item\\shears.png', 5, 13),
        (f'{texture_dir}item\\melon_slice.png', 6, 13),
        (f'{texture_dir}item\\nether_wart.png', 7, 13),
        (f'{texture_dir}item\\potion_overlay.png', 8, 13),
        (f'{texture_dir}item\\blaze_powder.png', 9, 13),
        (f'{texture_dir}item\\magma_cream.png', 10, 13),
        (f'{texture_dir}item\\flower_pot.png', 11, 13),
        (f'{texture_dir}item\\map.png', 12, 13),

        (f'{texture_dir}item\\snowball.png', 0, 14),
        (f'{texture_dir}item\\slime_ball.png', 1, 14),
        (f'{texture_dir}item\\melon_seeds.png', 3, 14),
        (f'{texture_dir}item\\ink_sac.png', 4, 14),
        (f'{texture_dir}item\\red_dye.png', 5, 14),
        (f'{texture_dir}item\\green_dye.png', 6, 14),
        (f'{texture_dir}item\\brown_dye.png', 7, 14),
        (f'{texture_dir}item\\lapis_lazuli.png', 8, 14),
        (f'{texture_dir}item\\purple_dye.png', 9, 14),
        (f'{texture_dir}item\\cyan_dye.png', 10, 14),
        (f'{texture_dir}item\\light_gray_dye.png', 11, 14),
        (f'{texture_dir}item\\item_frame.png', 12, 14),

        (f'{texture_dir}gui\\sprites\\container\\slot\\helmet.png', 0, 15),
        (f'{texture_dir}gui\\sprites\\container\\slot\\chestplate.png', 1, 15),
        (f'{texture_dir}gui\\sprites\\container\\slot\\leggings.png', 2, 15),
        (f'{texture_dir}gui\\sprites\\container\\slot\\boots.png', 3, 15),
        (f'{texture_dir}item\\gray_dye.png', 4, 15),
        (f'{texture_dir}item\\pink_dye.png', 5, 15),
        (f'{texture_dir}item\\lime_dye.png', 6, 15),
        (f'{texture_dir}item\\yellow_dye.png', 7, 15),
        (f'{texture_dir}item\\light_blue_dye.png', 8, 15),
        (f'{texture_dir}item\\magenta_dye.png', 9, 15),
        (f'{texture_dir}item\\orange_dye.png', 10, 15),
        (f'{texture_dir}item\\bone_meal.png', 11, 15),
        (f'{texture_dir}item\\enchanted_book.png', 12, 15),

        (f'{texture_dir}item\\music_disc_13.png', 15, 0),
        (f'{texture_dir}item\\music_disc_cat.png', 15, 1),
        (f'{texture_dir}item\\music_disc_blocks.png', 15, 2),
        (f'{texture_dir}item\\music_disc_chirp.png', 15, 3),
        (f'{texture_dir}item\\music_disc_far.png', 15, 4),
        (f'{texture_dir}item\\music_disc_mall.png', 15, 5),
        (f'{texture_dir}item\\music_disc_mellohi.png', 15, 6),
        (f'{texture_dir}item\\music_disc_stal.png', 15, 7),
        (f'{texture_dir}item\\music_disc_strad.png', 15, 8),
        (f'{texture_dir}item\\music_disc_ward.png', 15, 9),
        (f'{texture_dir}item\\music_disc_11.png', 15, 10),
        (f'{texture_dir}item\\music_disc_wait.png', 15, 11),
        (f'{texture_dir}item\\music_disc_13.png', 15, 12),
        (f'{texture_dir}item\\music_disc_cat.png', 15, 13),
        (f'{texture_dir}item\\music_disc_13.png', 15, 14),
        (f'{texture_dir}item\\music_disc_cat.png', 15, 15),
    ]
    paths = (jar_path, texture_dir)
    return grid_png('output\\gui\\items.png', texture_list, grid_width=16,
                    grid_height=16, paths=paths)


def gui_1dot20(texture_dir):
    file_list = [
        (f'{texture_dir}gui\\menu_background.png', 'options_background.png'),
    ]
    return copy_and_rename_files('output\\assets\\minecraft\\textures\\gui', file_list)


def gui_1dot5(texture_dir):
    file_list = [
        (f'{texture_dir}gui\\menu_background.png', 'background.png'),
        (f'{texture_dir}gui\\container\\generic_54.png', 'container.png'),
        (f'{texture_dir}gui\\container\\crafting_table.png', 'crafting.png'),
        (f'{texture_dir}gui\\container\\furnace.png', 'furnace.png'),
        (f'{texture_dir}gui\\container\\inventory.png', 'inventory.png'),
        (f'{texture_dir}gui\\container\\dispenser.png', 'trap.png'),
        (f'{texture_dir}gui\\container\\brewing_stand.png', 'alchemy.png'),
        (f'{texture_dir}gui\\container\\beacon.png', 'beacon.png'),
        (f'{texture_dir}gui\\book.png', 'book.png'),
        (f'{texture_dir}gui\\container\\enchanting_table.png', 'enchant.png'),
        (f'{texture_dir}gui\\container\\anvil.png', 'repair.png'),
        # trading.png isn't very compatible with villager.png
        (f'{texture_dir}gui\\demo_background.png', 'demo_bg.png'),
        (f'{texture_dir}gui\\container\\creative_inventory\\tab_items.png', 'creative_inv\\list_items.png'),
        (f'{texture_dir}gui\\container\\creative_inventory\\tab_item_search.png', 'creative_inv\\search.png'),
        (f'{texture_dir}gui\\container\\creative_inventory\\tab_inventory.png', 'creative_inv\\survival_inv.png'),
    ]
    return copy_and_rename_files('output\\gui', file_list)


