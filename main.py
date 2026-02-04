from pathlib import Path

import numpy as np

from armor import armor_1dot5, armor_1dot21
from environment import environment_latest
from gui import bars_1dot20, widgets_1dot20, items_1dot5, gui_1dot5, icons_1dot20
from item import double_chest_1dot20
from terrain import terrain_1dot5, terrain_1dot3
from title import title_latest

root_dir = "F:\\renegade complete\\renegade\\"
texture_dir = f"{root_dir}assets\\minecraft\\textures\\"
mc_path = Path.home() / "AppData" / "Roaming" / ".minecraft" / "versions"
fallback_version = '1.21.8'
jar_path = mc_path / fallback_version / f'{fallback_version}.jar'

errors = []
errors += terrain_1dot3(texture_dir, jar_path)
errors += title_latest(texture_dir)
errors += armor_1dot5(texture_dir)
errors += armor_1dot21(texture_dir)
errors += environment_latest(texture_dir)
errors += bars_1dot20(texture_dir, jar_path)
errors += widgets_1dot20(texture_dir)
errors += items_1dot5(texture_dir, jar_path)
errors += gui_1dot5(texture_dir)
errors += double_chest_1dot20(texture_dir)
errors += icons_1dot20(texture_dir, jar_path)
np.savetxt('errors.txt', errors, fmt='%s')