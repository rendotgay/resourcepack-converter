import os
import shutil
from collections import defaultdict

from PIL import Image
import numpy as np

from default_fallback import fallback_asset


fallbacks = {
    'enchanting_table_bottom.png': 'obsidian.png',
    'icon\\ping_5.png': 'server_list\\ping_5.png',
    'server_list\\ping_5.png': 'icon\\ping_5.png',
    'icon\\ping_4.png': 'server_list\\ping_4.png',
    'server_list\\ping_4.png': 'icon\\ping_4.png',
    'icon\\ping_3.png': 'server_list\\ping_3.png',
    'server_list\\ping_3.png': 'icon\\ping_3.png',
    'icon\\ping_2.png': 'server_list\\ping_2.png',
    'server_list\\ping_2.png': 'icon\\ping_2.png',
    'icon\\ping_1.png': 'server_list\\ping_1.png',
    'server_list\\ping_1.png': 'icon\\ping_1.png',
    'icon\\ping_unknown.png': 'server_list\\unreachable.png',
    'server_list\\unreachable.png': 'icon\\ping_unknown.png',
}


def grid_png(output_path, texture_list, width=256, height=256, grid_width=16, grid_height=16, paths=None):
    """
    Builds a 256x256 terrain.png from a list of (input_png_path, row, col, crop_coords, rotation, bg_color) tuples.

    :param height: int, height of png created, default is 256 as was originally created for 'terrain.png'
    :param width: int, width of png created, default is 256 as was originally created for 'terrain.png'
    :param output_path: str, path to save the output PNG (e.g., 'terrain.png')
    :param texture_list: list of tuples, each (input_png_path, grid_row, grid_col, crop_coords, rotation, bg_color)
                         where row and col are 0-15 integers, crop_coords is (x, y) or None,
                         rotation is degrees (0, 90, 180, 270) or None, and bg_color is (r, g, b) or None.
    """
    # Initialize a 256x256x4 numpy array (RGBA), fully transparent
    terrain = np.zeros((width, height, 4), dtype=np.uint8)

    errors = []
    for entry in texture_list:
        # Parse tuple: allow for optional crop_coords, rotation, and bg_color
        if len(entry) == 3:
            input_path, row, col = entry
            crop_coords, rotation, bg_color = None, None, None
        elif len(entry) == 4:
            input_path, row, col, crop_coords = entry
            rotation, bg_color = None, None
        elif len(entry) == 5:
            input_path, row, col, crop_coords, rotation = entry
            bg_color = None
        elif len(entry) == 6:
            input_path, row, col, crop_coords, rotation, bg_color = entry
        else:
            print(
                f"Invalid entry format: {entry}. Expected (path, row, col) or (path, row, col, crop_coords, rotation, bg_color).")
            errors.append(f"Invalid entry format: {entry}. Expected (path, row, col) or (path, row, col, crop_coords, rotation, bg_color).")
            continue

        max_height = (height / grid_height) - 1
        max_width = (width / grid_width) - 1
        if not (0 <= row <= max_height and 0 <= col <= max_width):
            print(f"Invalid grid position ({row}, {col}) for {input_path}: must be 0-15.")
            errors.append(f"Invalid grid position ({row}, {col}) for {input_path}: must be 0-15.")
            continue

        # Load image with Pillow
        try:
            img = Image.open(input_path).convert('RGBA')  # Ensure RGBA format
        except FileNotFoundError:
            if 'enchanting_table_bottom.png' in input_path:
                try:
                    img = Image.open(input_path.replace('enchanting_table_bottom.png', 'obsidian.png')).convert(
                        'RGBA')  # Ensure RGBA format
                    errors.append("enchanting_table_bottom.png is missing. Falling back to obsidian.png.")
                except FileNotFoundError:
                    if paths:
                        jar_path, texture_dir = paths
                        if jar_path:
                            asset_path = f'assets/minecraft/textures/{input_path.replace(texture_dir, '').replace('\\', '/')}'
                            img = fallback_asset(asset_path=asset_path, jar_path=jar_path)
                            if not img:
                                print(f"File not found: {input_path}")
                                errors.append(f"File not found: {input_path}")
                                continue
                            errors.append(f'Substituted {input_path} for default texture')
                        else:
                            print(f"File not found: {input_path}")
                            errors.append(f"File not found: {input_path}")
                            continue
                    else:
                        print(f"File not found: {input_path}")
                        errors.append(f"File not found: {input_path}")
                        continue
                except Exception as e:
                    print(f"Error loading {input_path}: {e}")
                    errors.append(f"Error loading {input_path}: {e}")
                    continue
            else:
                if paths:
                    jar_path, texture_dir = paths
                    if jar_path:
                        asset_path = f'assets/minecraft/textures/{input_path.replace(texture_dir, '').replace('\\', '/')}'
                        img = fallback_asset(asset_path=asset_path, jar_path=jar_path)
                        if not img:
                            print(f"File not found: {input_path}")
                            errors.append(f"File not found: {input_path}")
                            continue
                        errors.append(f'Substituted {input_path} for default texture')
                    else:
                        print(f"File not found: {input_path}")
                        errors.append(f"File not found: {input_path}")
                        continue
                else:
                    print(f"File not found: {input_path}")
                    errors.append(f"File not found: {input_path}")
                    continue
        except Exception as e:
            print(f"Error loading {input_path}: {e}")
            errors.append(f"Error loading {input_path}: {e}")
            continue

        # Crop if crop_coords is provided
        if crop_coords is not None:
            x, y = crop_coords
            if x < 0 or y < 0 or x + grid_width > img.width or y + grid_height > img.height:
                print(f"Invalid crop coordinates {crop_coords} for {input_path}: image size is {img.size}.")
                errors.append(f"Invalid crop coordinates {crop_coords} for {input_path}: image size is {img.size}.")
                continue
            img = img.crop((x, y, x + 16, y + 16))

        # Verify image size
        if img.size != (grid_width, grid_height):
            print(f"Error: {input_path} is not 16x16 after processing. Size: {img.size}")
            errors.append(f"Error: {input_path} is not 16x16 after processing. Size: {img.size}")
            continue

        # Apply rotation if specified
        if rotation in (90, 180, 270):
            # Rotate without expansion, preserving original size
            img = img.rotate(rotation, expand=False, resample=Image.Resampling.BILINEAR)
            # Ensure it stays 16x16 (trim if needed)
            img = img.crop((0, 0, 16, 16))

        # Apply background color if specified and transparency exists
        if bg_color is not None:
            r, g, b = bg_color
            if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
                print(f"Invalid bg_color {bg_color} for {input_path}: must be (r, g, b) with 0-255.")
                errors.append(f"Invalid bg_color {bg_color} for {input_path}: must be (r, g, b) with 0-255.")
                bg_color = None
            if bg_color:
                # Create a new image with solid background
                new_img = Image.new('RGBA', (16, 16), (r, g, b, 255))
                # Paste the original image over it
                new_img.paste(img, (0, 0), img)
                img = new_img

        # Convert to numpy array
        small_img = np.array(img)

        # Check alpha channel
        alpha = small_img[:, :, 3]
        print(f"{input_path}: Alpha min={alpha.min()}, max={alpha.max()}, mean={alpha.mean():.2f}")

        # Calculate pixel coordinates
        y_start = row * grid_height
        x_start = col * grid_width

        # Paste into the big array
        terrain[y_start:y_start + grid_height, x_start:x_start + grid_width] = small_img

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Save with Pillow
    Image.fromarray(terrain).save(output_path, 'PNG')
    print(f"Saved to {output_path}")
    return errors


def freeform_png(output_path, texture_list, width=256, height=256, default_size=(16, 16), paths=None):
    """
    Builds a PNG by placing textures at absolute (x, y) coordinates.

    :param output_path: str, path to save the output PNG.
    :param texture_list: list of tuples, each (input_png_path, x, y, crop_coords, rotation, bg_color, entry_size, flip_horizontal)
                         where x and y are absolute pixel coordinates (top-left),
                         crop_coords is (crop_x, crop_y) or None,
                         rotation is degrees (0, 90, 180, 270) or None,
                         bg_color is (r, g, b) or None,
                         entry_size is (w, h) or None (falls back to default_size),
                         flip_horizontal is bool (True to flip left-right) or None (defaults to False).
    :param width: int, width of the output PNG.
    :param height: int, height of the output PNG.
    :param default_size: tuple, default (w, h) if not specified per entry.
    """
    # Initialize an RGBA array, fully transparent
    terrain = np.zeros((height, width, 4), dtype=np.uint8)

    errors = []
    for entry in texture_list:
        # Parse tuple
        if len(entry) == 3:
            input_path, x, y = entry
            crop_coords, rotation, bg_color, entry_size, flip_horizontal = None, None, None, None, False
        elif len(entry) == 4:
            input_path, x, y, crop_coords = entry
            rotation, bg_color, entry_size, flip_horizontal = None, None, None, False
        elif len(entry) == 5:
            input_path, x, y, crop_coords, rotation = entry
            bg_color, entry_size, flip_horizontal = None, None, False
        elif len(entry) == 6:
            input_path, x, y, crop_coords, rotation, bg_color = entry
            entry_size, flip_horizontal = None, False
        elif len(entry) == 7:
            input_path, x, y, crop_coords, rotation, bg_color, entry_size = entry
            flip_horizontal = False
        elif len(entry) == 8:
            input_path, x, y, crop_coords, rotation, bg_color, entry_size, flip_horizontal = entry
        else:
            print(
                f"Invalid entry format: {entry}. Expected up to (path, x, y, crop_coords, rotation, bg_color, entry_size, flip_horizontal).")
            errors.append(f"Invalid entry format: {entry}.")
            continue

        # Use per-entry size or default
        entry_w = entry_size[0] if entry_size else default_size[0]
        entry_h = entry_size[1] if entry_size else default_size[1]

        if x < 0 or y < 0 or x + entry_w > width or y + entry_h > height:
            print(
                f"Warning: Placement for {input_path} at ({x}, {y}) with size ({entry_w}, {entry_h}) overflows output ({width}x{height}). Clipping.")
            errors.append(f"Placement overflow for {input_path}.")

        # Load image
        try:
            img = Image.open(input_path).convert('RGBA')
        except FileNotFoundError:
            for original, replacement in fallbacks.items():
                if original in input_path:
                    try:
                        img = (
                            Image
                            .open(input_path.replace(original, replacement))
                            .convert('RGBA')  # ensure RGBA
                        )
                        errors.append(f"{original} is missing. Falling back to {replacement}.")
                    except FileNotFoundError:
                        if paths:
                            jar_path, texture_dir = paths
                            if jar_path:
                                asset_path = f'assets/minecraft/textures/{input_path.replace(texture_dir, '').replace('\\', '/')}'
                                img = fallback_asset(asset_path=asset_path, jar_path=jar_path)
                                if not img:
                                    print(f"File not found: {input_path}")
                                    errors.append(f"File not found: {input_path}")
                                    continue
                                errors.append(f'Substituted {input_path} for default texture')
                            else:
                                print(f"File not found: {input_path}")
                                errors.append(f"File not found: {input_path}")
                                continue
                        else:
                            print(f"File not found: {input_path}")
                            errors.append(f"File not found: {input_path}")
                            continue
            else:
                if paths:
                    jar_path, texture_dir = paths
                    if jar_path:
                        asset_path = f'assets/minecraft/textures/{input_path.replace(texture_dir, '').replace('\\', '/')}'
                        img = fallback_asset(asset_path=asset_path, jar_path=jar_path)
                        if not img:
                            print(f"File not found: {input_path}")
                            errors.append(f"File not found: {input_path}")
                            continue
                        errors.append(f'Substituted {input_path} for default texture')
                    else:
                        print(f"File not found: {input_path}")
                        errors.append(f"File not found: {input_path}")
                        continue
                else:
                    print(f"File not found: {input_path}")
                    errors.append(f"File not found: {input_path}")
                    continue
        except Exception as e:
            print(f"Error loading {input_path}: {e}")
            errors.append(f"Error loading {input_path}: {e}")
            continue

        # Crop with overflow handling (clip + transparent fill)
        if crop_coords is not None:
            crop_x, crop_y = crop_coords
            if crop_x < 0 or crop_y < 0:
                print(f"Invalid crop coordinates {crop_coords} for {input_path}: coordinates must be non-negative.")
                errors.append(f"Invalid crop coordinates {crop_coords} for {input_path}.")
                continue

            # Effective crop bounds
            effective_right = min(crop_x + entry_w, img.width)
            effective_bottom = min(crop_y + entry_h, img.height)

            if effective_right > crop_x and effective_bottom > crop_y:
                cropped = img.crop((crop_x, crop_y, effective_right, effective_bottom))
                new_img = Image.new('RGBA', (entry_w, entry_h), (0, 0, 0, 0))
                new_img.paste(cropped, (0, 0))
                img = new_img
            else:
                img = Image.new('RGBA', (entry_w, entry_h), (0, 0, 0, 0))

        # Verify size (after crop)
        if img.size != (entry_w, entry_h):
            print(f"Error: {input_path} is not {entry_w}x{entry_h} after processing. Size: {img.size}")
            errors.append(f"Error: {input_path} is not {entry_w}x{entry_h} after processing. Size: {img.size}")
            continue

        # Apply rotation
        if rotation in (90, 180, 270):
            img = img.rotate(rotation, expand=False, resample=Image.Resampling.BILINEAR)
            img = img.crop((0, 0, entry_w, entry_h))

        # Apply horizontal flip
        if flip_horizontal:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Apply background color
        if bg_color is not None:
            r, g, b = bg_color
            if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                print(f"Invalid bg_color {bg_color} for {input_path}: must be (r, g, b) with 0-255.")
                errors.append(f"Invalid bg_color {bg_color} for {input_path}.")
            else:
                new_img = Image.new('RGBA', (entry_w, entry_h), (r, g, b, 255))
                new_img.paste(img, (0, 0), img)
                img = new_img

        # Convert to numpy
        small_img = np.array(img)

        # Alpha check
        alpha = small_img[:, :, 3]
        print(f"{input_path}: Alpha min={alpha.min()}, max={alpha.max()}, mean={alpha.mean():.2f}")

        # Paste (clip if overflow)
        paste_h = min(entry_h, height - y)
        paste_w = min(entry_w, width - x)
        terrain[y:y + paste_h, x:x + paste_w] = small_img[:paste_h, :paste_w]

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Save
    Image.fromarray(terrain).save(output_path, 'PNG')
    print(f"Saved to {output_path}")
    return errors


def copy_and_rename_files(output_path, file_list, paths=None):
    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    errors = []
    for item in file_list:
        # Check if item is a string (single file path) or tuple (file path, new name)
        if isinstance(item, str):
            source_path = item
            # Extract the filename from the source path
            filename = os.path.basename(source_path)
        elif isinstance(item, tuple) and len(item) == 2:
            source_path, new_filename = item
            filename = new_filename
        else:
            print(f"Invalid item format: {item}")
            errors.append(f"Invalid item format: {item}")
            continue

        # Create the destination path
        dest_path = os.path.join(output_path, filename)

        try:
            # Copy the file to the new location
            shutil.copy2(source_path, dest_path)
            print(f"Copied {source_path} to {dest_path}")
        except FileNotFoundError:
            if paths:
                jar_path, texture_dir = paths
                if jar_path:
                    asset_path = f'assets/minecraft/textures/{source_path.replace(texture_dir, '').replace('\\', '/')}'
                    img = fallback_asset(asset_path=asset_path, jar_path=jar_path)
                    if not img:
                        print(f"File not found: {source_path}")
                        errors.append(f"File not found: {source_path}")
                        continue
                    errors.append(f'Substituted {source_path} for default texture')
                else:
                    print(f"File not found: {source_path}")
                    errors.append(f"File not found: {source_path}")
                    continue
            else:
                print(f"File not found: {source_path}")
                errors.append(f"File not found: {source_path}")
                continue
        except Exception as e:
            print(f"Error copying {source_path}: {str(e)}")
            errors.append(f"Error copying {source_path}: {str(e)}")
    return errors