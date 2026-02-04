import zipfile
from pathlib import Path

from PIL import Image


def fallback_asset(asset_path, jar_path):
    if jar_path.exists():
        jar = zipfile.ZipFile(jar_path, 'r')
    else:
        print(f"Error: Minecraft jar not found at {jar_path}. Default assets unavailable.")
        return None
    try:
        with jar.open(asset_path) as default_file:
            print(f'Opened file')
            return Image.open(default_file).convert('RGBA')
    except KeyError:
        print(f"Default asset {asset_path} not found in 1.21.8.jar.")
        return None


if __name__ == "__main__":
    mc_path = Path.home() / "AppData" / "Roaming" / ".minecraft" / "versions"
    fallback_version = '1.21.8'
    jar_path = mc_path / fallback_version / f'{fallback_version}.jar'
    fallback_asset(asset_path='assets/minecraft/texturesblock/rail.png', jar_path=jar_path)