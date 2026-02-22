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


def parse_jar(vid=None):
    """
    Finds all assets in the Minecraft JAR and returns their paths.
    :param vid: [Optional] The version ID for debugging purposes.
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
            if filename.startswith("assets/") and not "atlases" in filename and not "shaders" in filename:
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
        "json":    "file-json",
        "mcmeta":  "file-mcmeta",
        "fsh":     "file-shader",
        "vsh":     "file-shader",
        "ogg":     "file-audio",
    }
    return classes.get(ext, "file-unknown")


def tree_to_html(tree, is_added, indent=0):
    """Recursively builds HTML list items for the tree."""
    lines = []
    section_class = "added" if is_added else "removed"
    for key, subtree in sorted(tree.items()):
        if is_file(key, subtree):
            file_class = get_file_class(key)
            lines.append(f'<li class="file {section_class} {file_class}">{key}</li>')
        else:
            if is_added:
                li_id = f"{subtree}-{key}-added"
            else:
                li_id = f"{subtree}-{key}-removed"
            lines.append(f'<li class="folder" id="{li_id}">{key}')
            lines.append(f'<a href="#{li_id}"><ul>')
            lines.extend(tree_to_html(subtree, is_added, indent + 1))
            lines.append('</ul></a>')
            lines.append('</li>')
    return lines


def export_changes(removed_tree, added_tree, vid1, vid2):
    os.makedirs("assets", exist_ok=True)
    filepath = f"assets/{vid1}_to_{vid2}.html"

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
        li.file-unknown {{ color: #719f72; }}
        a {{ color: inherit; text-decoration: none; }}
        code {{ color: white; }}
        .hidden {{ display: none !important; }}
        .buttons {{ display: flex; flex-direction: row; }}
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
        <button id="hideJson">Hide JSON</button>
    </div>
""")

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

        f.write(f"""</body>
        <script>
            const jsonBtn = document.getElementById('hideJson');
            
            jsonBtn.addEventListener('click', () => {{
                document.querySelectorAll('.file-json').forEach(el => {{
                    el.classList.toggle('hidden');
                }});
        
                const isHidden = document.querySelector('.file-json')?.classList.contains('hidden') ?? false;
                
                jsonBtn.textContent = isHidden ? 'Show JSON' : 'Hide JSON';
            }});
        </script>
        </html>""")

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
        print(f"{CYAN}Baseline set.")
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


def main(count:int=None, max_ver:str=None, min_ver:str=None):
    """
    Download Minecraft version JARs and compare the assets to find changes.
    Creates .html files for each version pair, along with console output.
    :param count: Number of versions to compare. Primarily used for debugging.
    :param max_ver: The newest version to download.
    :param min_ver: The oldest version to download.
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
                    vid = v['id'].split('-')[0]
                    vid = vid.split('_')[0]
                    vid = vid.split('.')
                    seenvid = vid[0] + '.' + vid[1]
                    if seenvid not in seen:
                        if max_ver:
                            mv = max_ver.split('.')
                            if vid[0] > mv[0]:
                                print(f"{YELLOW}Skipping {v['id']} due to max version.")
                                seen.add(seenvid)
                                continue
                            elif vid[1] > mv[1]:
                                print(f"{YELLOW}Skipping {v['id']} due to max version.")
                                seen.add(seenvid)
                                continue
                            elif len(vid) >= 3 and vid[2] > mv[2]:
                                print(f"{YELLOW}Skipping {v['id']} due to max version.")
                                seen.add(seenvid)
                                continue
                        if min_ver:
                            mv = min_ver.split('.')
                            if vid[0] < mv[0]:
                                print(f"{YELLOW}Skipping {v['id']} due to min version.")
                                seen.add(seenvid)
                                continue
                            elif vid[1] < mv[1]:
                                print(f"{YELLOW}Skipping {v['id']} due to min version.")
                                seen.add(seenvid)
                                continue
                            elif len(vid) >= 3 and vid[2] < mv[2]:
                                print(f"{YELLOW}Skipping {v['id']} due to min version.")
                                seen.add(seenvid)
                                continue
                        print(f"{YELLOW}Downloading {v['id']}")
                        download_json(v['url'])
                        url = parse_json(v['id'])
                        if url:
                            download_jar(url)
                            contents = parse_jar(v['id'])
                            compare_contents(last_data, contents, last_version, v['id'])
                            last_data = contents
                            last_version = v['id']
                        if count is not None:
                            if count > 1:
                                count -= 1
                                print(f"{YELLOW}Remaining: {count}")
                            else:
                                print(f"{YELLOW}Finished.")
                                return
                        seen.add(seenvid)
                        r = random.randint(10, 60)
                        for i in range(r, 0, -1):
                            print(f"\r{YELLOW}Sleeping for {i} seconds...  ", end="", flush=True)
                            time.sleep(1)
                        print()
                    else:
                        minor_versions.append(v)

        else:
            print(f"{RED}Versions not found.")
    else:
        print(f"{RED}Manifest not found.")

    print(f"{CYAN}Minor versions: {len(minor_versions)}")
    print(f"{CYAN}Snapshots: {len(snapshots)}")
    print(f"{CYAN}Betas: {len(betas)}")
    print(f"{GREEN}Finished.")


if __name__ == "__main__":
    main(max_ver="1.14.4")