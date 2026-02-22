import json
import os
import random
import time
import zipfile
from pathlib import Path
import urllib.request

from console_colors import RED, YELLOW, CYAN, GREEN, WHITE, RESET


def download_json(url):
    """
    Downloads the versions JSON file from the given URL, which contains the JAR url.
    :param url: The URL of from the version manifest to download the JSON from.
    """
    if not Path("assets").exists():
        Path("assets").mkdir()
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = min(downloaded / total_size * 100, 100)
        bar_filled = int(percent // 2)
        bar = "█" * bar_filled + "░" * (50 - bar_filled)
        print(f"\r{RESET}Downloading JSON: [{bar}] {percent:.1f}%", end="", flush=True)
        if percent >= 100:
            print()

    urllib.request.urlretrieve(
        url,
        filename=f"assets/info.json",
        reporthook=progress
    )


def download_jar(url):
    """
    Downloads the Minecraft JAR from the given URL.
    :param url: The URL from the versions info.json to download the JAR from.
    """
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = min(downloaded / total_size * 100, 100)
        bar_filled = int(percent // 2)
        bar = "█" * bar_filled + "░" * (50 - bar_filled)
        print(f"\r{RESET}Downloading JAR: [{bar}] {percent:.1f}%", end="", flush=True)
        if percent >= 100:
            print()

    urllib.request.urlretrieve(url, filename="assets/minecraft.jar", reporthook=progress)


def parse_json(vid=None):
    """
    Parses the versions info.json file and returns the JAR download URL.
    :param vid: [Optional] The version ID for debugging purposes.
    :return: The URL to download the client JAR.
    """
    path = Path("assets/info.json")
    if not path.exists():
        return None
    with open(path, 'r') as file:
        data = json.load(file)

    if 'downloads' in data:
        if 'client' in data['downloads']:
            if 'url' in data['downloads']['client']:
                return data['downloads']['client']['url']
            else:
                if vid:
                    print(f"{RED}Client download url not found for {vid}")
                else:
                    print(f"{RED}Client download url not found.")
        else:
            if vid:
                print(f"{RED}Client download not found for {vid}")
            else:
                print(f"{RED}Client download not found.")
    else:
        if vid:
            print(f"{RED}Downloads not found for {vid}")
        else:
            print(f"{RED}Downloads not found.")
    return None


def parse_jar(vid=None, is_beta=False):
    """
    Finds all assets in the Minecraft JAR and returns their paths.
    :param vid: [Optional] The version ID for debugging purposes.
    :param is_beta: Determines what assets to filter.
    :return: The contents of the assets folder from the version JAR
    """
    path = Path("assets/minecraft.jar")
    if not path.exists():
        if vid:
            print(f"{RED}Jar not found for {vid}")
        else:
            print(f"{RED}Jar not found.")
        return None
    contents = []
    with zipfile.ZipFile(path, "r") as archive:
        for filename in archive.namelist():
            if not is_beta:
                if filename.startswith("assets/") and not "atlases" in filename and not "shaders" in filename:
                    contents.append(filename)
            else:
                if (not filename.endswith(".class")
                        and not filename.startswith("null")
                        and not filename.startswith("com/")
                        and not filename.startswith("META-INF/")
                        and not filename.startswith("misc/")
                        and not filename.startswith("net/")
                        and not filename.startswith("paulscode/")
                        and not filename.startswith("a/")
                        and not filename.startswith("de/")
                ):
                    contents.append(filename)
        print(f"{YELLOW}{len(contents)} assets found in jar")
        return contents


def build_tree(paths):
    """Builds a nested dict tree from a list of file paths."""
    tree = {}
    for path in paths:
        parts = path.replace("\\", "/").split("/")
        node = tree
        for part in parts:
            node = node.setdefault(part, {})
    return tree


def is_file(key, subtree):
    """A leaf node (empty dict) is a file."""
    return len(subtree) == 0


def print_tree(tree, indent=0, color=RED):
    for key, subtree in sorted(tree.items()):
        if is_file(key, subtree):
            if key.endswith(".png"):
                print(f"{color}{'    ' * indent}{key}")
            else:
                print(f"{YELLOW}{'    ' * indent}{key}")
        else:
            print(f"{WHITE}{'    ' * indent}{key}")
            print_tree(subtree, indent + 1, color)


def get_file_class(key):
    """Returns a CSS class name based on file extension."""
    ext = key.rsplit(".", 1)[-1] if "." in key else ""
    classes = {
        "png":     "file-image",
        "gif":     "file-image",
        "json":    "file-json",
        "mcmeta":  "file-mcmeta",
        "txt":  "file-mcmeta",
        "fsh":     "file-shader",
        "vsh":     "file-shader",
        "ogg":     "file-audio",
        "nbt":     "file-nbt",
        "lang":     "file-lang",
    }
    return classes.get(ext, "file-unknown")


def tree_to_html(tree, is_added, path=""):
    """Recursively builds HTML list items for the tree."""
    lines = []
    section_class = "added" if is_added else "removed"
    for key, subtree in sorted(tree.items()):
        current_path = f"{path}-{key}" if path else key
        if is_file(key, subtree):
            file_class = get_file_class(key)
            lines.append(f'<li class="file {section_class} {file_class}">{key}</li>')
        else:
            li_id = f"{current_path}-{'added' if is_added else 'removed'}"
            lines.append(f'<li class="folder" id="{li_id}"><a href="#{li_id}">{key}</a>')
            lines.append('<ul>')
            lines.extend(tree_to_html(subtree, is_added, current_path))
            lines.append('</ul>')
            lines.append('</li>')
    return lines


def get_present_classes(tree, found=None):
    """Recursively collects all file classes present in the tree."""
    if found is None:
        found = set()
    for key, subtree in tree.items():
        if is_file(key, subtree):
            found.add(get_file_class(key))
        else:
            get_present_classes(subtree, found)
    return found


def export_changes(removed_tree, added_tree, vid1, vid2):
    os.makedirs("assets", exist_ok=True)
    filepath = f"assets/{vid1}_to_{vid2}.html"

    present_classes = set()
    if removed_tree:
        present_classes |= get_present_classes(removed_tree)
    if added_tree:
        present_classes |= get_present_classes(added_tree)

    has_json = "file-json" in present_classes
    has_nbt  = "file-nbt"  in present_classes
    has_lang  = "file-lang"  in present_classes

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Changes: {vid1} to {vid2}</title>
            <style>
                body {{ font-family: monospace; background: #1e1e1e; color: #ccc; padding: 2rem; }}
                h1 {{ color: #fff; }}
                h2 {{ margin-top: 2rem; }}
                h2.added {{ color: #f44336; }}
                h2.removed {{ color: #4caf50; }}
                ul {{ list-style: none; padding-left: 1.5rem; }}
                li.folder {{ color: #fff; margin-top: 0.25rem; }}
                li.file {{ margin-top: 0.1rem; }}
                li.added {{ color: #f44336; }}
                li.removed {{ color: #4caf50; }}
                li.file-image {{ }}
                li.file-json {{ color: #d2b545; }}
                li.file-mcmeta {{ color: #d2b545; }}
                li.file-shader {{ color: #d2b545; }}
                li.file-audio {{ color: #d2b545; }}
                li.file-nbt {{ color: #d2b545; }}
                li.file-lang {{ color: #d2b545; }}
                li.file-unknown {{ color: #719f72; }}
                a {{ color: inherit; text-decoration: none; }}
                code {{ color: white; }}
                .hidden {{ display: none !important; }}
                .buttons {{ display: flex; flex-direction: row; gap: 5px }}
                .buttons button {{ 
                    background: transparent;
                    color: white;
                    border: 1px solid white;
                    border-radius: 6px;
                    padding: 5px 10px;
                    cursor: pointer;
                }}
                .buttons button:hover {{ 
                    background: white;
                    color: black;
                    border: 1px solid black;
                }}
            </style>
        </head>
        <body>
            <h1>Changes: {vid1} &rarr; {vid2}</h1>
            <div class="buttons">
        """)
        if has_json:
            f.write('        <button id="hideJson">Hide JSON</button>\n')
        if has_nbt:
            f.write('        <button id="hideNbt">Hide NBT</button>\n')
        if has_lang:
            f.write('        <button id="hideLang">Hide lang</button>\n')

        f.write('    </div>\n')

        if added_tree:
            f.write(f'    <h2 class="added">Removed in {vid1}</h2>\n')
            f.write(f'    <p>Present in <code>{vid2}</code>, missing in <code>{vid1}</code></p>\n')
            f.write('    <ul>\n')
            for line in tree_to_html(added_tree, is_added=True):
                f.write(f'        {line}\n')
            f.write('    </ul>\n')

        if removed_tree:
            f.write(f'    <h2 class="removed">Added in {vid1}</h2>\n')
            f.write(f'    <p>Present in <code>{vid1}</code>, missing in <code>{vid2}</code></p>\n')
            f.write('    <ul>\n')
            for line in tree_to_html(removed_tree, is_added=False):
                f.write(f'        {line}\n')
            f.write('    </ul>\n')

        f.write('<script>\n')
        if has_json:
            f.write("""
            const jsonBtn = document.getElementById('hideJson');
            jsonBtn.addEventListener('click', () => {
                document.querySelectorAll('.file-json').forEach(el => el.classList.toggle('hidden'));
                const isHidden = document.querySelector('.file-json')?.classList.contains('hidden') ?? false;
                jsonBtn.textContent = isHidden ? 'Show JSON' : 'Hide JSON';
            });
            """)
        if has_nbt:
            f.write("""
            const nbtBtn = document.getElementById('hideNbt');
            nbtBtn.addEventListener('click', () => {
                document.querySelectorAll('.file-nbt').forEach(el => el.classList.toggle('hidden'));
                const isHidden = document.querySelector('.file-nbt')?.classList.contains('hidden') ?? false;
                nbtBtn.textContent = isHidden ? 'Show NBT' : 'Hide NBT';
            });
            """)
        if has_lang:
            f.write("""
            const langBtn = document.getElementById('hideLang');
            langBtn.addEventListener('click', () => {
                document.querySelectorAll('.file-lang').forEach(el => el.classList.toggle('hidden'));
                const isHidden = document.querySelector('.file-lang')?.classList.contains('hidden') ?? false;
                langBtn.textContent = isHidden ? 'Show lang' : 'Hide lang';
            });
            """)
        f.write('</script>\n</body>\n</html>')

    print(f"{WHITE}Changes exported to {filepath}")


def compare_contents(contents1, contents2, vid1, vid2):
    """
    Compares the contents of two JARs and prints any differences.
    :param contents1: The previous, older JAR asset contents.
    :param contents2: The new JAR assets to compare against.
    :param vid1: The old version ID to compare against.
    :param vid2: The new version ID to compare against.
    """
    if vid1 is None:
        print(f"{GREEN}Baseline set.")
    else:
        removed = [c for c in contents1 if c not in contents2]
        added = [c for c in contents2 if c not in contents1]

        removed_tree = build_tree(removed) if removed else None
        added_tree = build_tree(added) if added else None

        if added_tree:
            print(f"{RED}Removed in {vid1} (missing in {vid1}, present in {vid2}):")
            print_tree(added_tree, color=RED)

        if removed_tree:
            print(f"{GREEN}Added in {vid1} (present in {vid1}, missing in {vid2}):")
            print_tree(removed_tree, color=GREEN)

        if not removed and not added:
            print(f"{CYAN}No changes between {vid1} and {vid2}.")
        else:
            export_changes(removed_tree, added_tree, vid1, vid2)


def main(count:int=None, max_ver:str=None, min_ver:str=None, min_sleep:int=10, max_sleep:int=60):
    """
    Download Minecraft version JARs and compare the assets to find changes.
    Creates .html files for each version pair, along with console output.
    :param count: Number of versions to compare. Keep in mind that the first count is used as a baseline.
     Primarily used for debugging.
    :param max_ver: The newest version to download.
    :param min_ver: The oldest version to download.
    :param min_sleep: The minimum number of seconds to sleep between downloads.
    :param max_sleep: The maximum number of seconds to sleep between downloads.
    """
    version_manifest = Path("version_manifest.json")
    seen = set()
    minor_versions = []
    snapshots = []
    betas = []
    last_data = []
    last_version = None

    if version_manifest.exists():
        with open(version_manifest, 'r') as file:
            data = json.load(file)
        if 'versions' in data:
            for v in data['versions']:
                if 'snapshot' in v['id'] or 'w' in v['id'] or 'pre' in v['id'].lower() or 'rc' in v['id']:
                    snapshots.append(v)
                elif v['id'].startswith('a') or v['id'].startswith('b') or v['id'].startswith('c') or v['id'].startswith('inf') or v['id'].startswith('rd'):
                    betas.append(v)
                else:
                    vid = v['id'].split('-')[0].split('_')[0].split('.')
                    seenvid = f"{vid[0]}.{vid[1]}"
                    if seenvid not in seen:
                        vid = [int(x) for x in vid]

                        if min_ver and vid < [int(x) for x in min_ver.split('.')]:
                            print(f"{YELLOW}Skipping {v['id']} due to min version.")
                            seen.add(seenvid)
                            continue

                        if vid < [int(x) for x in "1.6.1".split('.')]:
                            betas.append(v)
                            continue

                        if max_ver and vid > [int(x) for x in max_ver.split('.')]:
                            print(f"{YELLOW}Skipping {v['id']} due to max version.")
                            seen.add(seenvid)
                            continue
                        print(f"{CYAN}Downloading {v['id']}")
                        download_json(v['url'])
                        url = parse_json(v['id'])
                        if url:
                            download_jar(url)
                            contents = parse_jar(v['id'])
                            if contents:
                                compare_contents(last_data, contents, last_version, v['id'])
                                last_data = contents
                                last_version = v['id']
                                seen.add(seenvid)
                        if count is not None:
                            if count > 1:
                                count -= 1
                                print(f"{YELLOW}Remaining: {count}")
                            else:
                                print(f"{YELLOW}Finished.")
                                return
                        r = random.randint(min_sleep, max_sleep)
                        for i in range(r, 0, -1):
                            print(f"\r{YELLOW}Sleeping for {i} seconds...  ", end="", flush=True)
                            time.sleep(1)
                        print()
                    else:
                        # print(f"{YELLOW}Skipping {v['id']} due to not being a major release")
                        minor_versions.append(v)

        else:
            print(f"{RED}Versions not found.")
    else:
        print(f"{RED}Manifest not found.")

    if len(betas) > 0:
        last_data = []
        last_version = None
        print(f"{YELLOW}Beta versions:")
        for v in betas:
            vid = v['id'].split('-')[0].split('_')[0].split('.')
            if len(vid) >= 2:
                seenvid = f"{vid[0]}.{vid[1]}"
            else:
                seenvid = v['id']
            if seenvid not in seen:
                print(f"{CYAN}Downloading {v['id']}")
                download_json(v['url'])
                url = parse_json(v['id'])
                if url:
                    download_jar(url)
                    contents = parse_jar(v['id'], is_beta=True)
                    if contents:
                        compare_contents(last_data, contents, last_version, v['id'])
                        last_data = contents
                        last_version = v['id']
                        seen.add(seenvid)
                if count is not None:
                    if count > 1:
                        count -= 1
                        print(f"{YELLOW}Remaining: {count}")
                    else:
                        print(f"{YELLOW}Finished.")
                        return
                r = random.randint(min_sleep, max_sleep)
                for i in range(r, 0, -1):
                    print(f"\r{YELLOW}Sleeping for {i} seconds...  ", end="", flush=True)
                    time.sleep(1)
                print()

    print(f"{YELLOW}Cleaning up...")
    path = Path("assets/info.json")
    if path.exists():
        os.remove(path)
    path = Path("assets/minecraft.jar")
    if path.exists():
        os.remove(path)
    print(f"{CYAN}Seen versions:")
    print(f"{CYAN}{", ".join(seen)}")
    print(f"{CYAN}Minor versions skipped: {len(minor_versions)}")
    print(f"{CYAN}Snapshots skipped: {len(snapshots)}")
    print(f"{GREEN}Finished.")


def debug_list_ver():
    version_manifest = Path("version_manifest.json")
    if version_manifest.exists():
        with open(version_manifest, 'r') as file:
            data = json.load(file)
        if 'versions' in data:
            for v in data['versions']:
                if 'snapshot' in v['id'] or 'w' in v['id'] or 'pre' in v['id'].lower() or 'rc' in v['id']:
                    continue
                elif v['id'].startswith('a') or v['id'].startswith('b') or v['id'].startswith('c') or v['id'].startswith('inf') or v['id'].startswith('rd'):
                    continue
                else:
                    print(v['id'])


def debug_download(version="rd-161348"):
    version_manifest = Path("version_manifest.json")
    if version_manifest.exists():
        with open(version_manifest, 'r') as file:
            data = json.load(file)
        if 'versions' in data:
            for v in data['versions']:
                if v['id'] == version:
                    download_json(v['url'])
                    url = parse_json(v['id'])
                    if url:
                        download_jar(url)
                    else:
                        print(f"{RED}No URL found for {version}")
        else:
            print(f"{RED}Versions not found.")
    else:
        print(f"{RED}Manifest not found.")


if __name__ == "__main__":
    # debug_download("1.5.2")
    main(max_ver="1.5.2", max_sleep=30)