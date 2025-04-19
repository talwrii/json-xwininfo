import argparse
import json
import subprocess

from Xlib import X, display

PARSER = argparse.ArgumentParser(description='similar function xwininfo but provides json output')
PARSER.add_argument('--focused', action='store_true', help="Operate on focused window")


MAPPINGS = {
    "Absolute upper-left X":  ("x", int),
    "Absolute upper-left Y":  ("y", int),
    "Width": ("width", int),
    "Height": ("height", int),
    "Depth": ("colorDepth", int),
}


def main():
    args = PARSER.parse_args()
    if args.focused:
        d = display.Display()
        root = d.screen().root
        active_windows = root.get_full_property(
            d.intern_atom('_NET_ACTIVE_WINDOW', True), X.AnyPropertyType).value
        win_id, = active_windows
    else:
        win_id = None


    if win_id:
        cmd = ["xwininfo", "-id", str(win_id)]
    else:
        cmd = ["xwininfo"]

    output = subprocess.check_output(cmd).decode('utf8')
    data = {}
    for line in output.splitlines():
        if line.startswith("xwininfo"):
            _, _, _, win_id, title = line.split(" ", 4)
            data["window_id"] = win_id
            data["title"] = title[1:-1]
            continue

        if ":" in line:
            name, value = line.split(":", 1)
            name = name.strip()

            if name == "Corners":
                top_left, top_right, bottom_right, bottom_left = value.split()
                data["top_left_geometry"] = top_left
                data["top_right_geometry"] = top_right
                data["bottom_right_geometry"] = bottom_right
                data["bottom_left_geometry"] = bottom_left
                continue

            if name in MAPPINGS:
                new_name, parse = MAPPINGS[name]
                data[new_name] = parse(value.strip())
                continue

            continue

        if line.strip().startswith("-geometry"):
            _, geometry = line.strip().split()
            data["geometry"] = geometry

    print(json.dumps(data, indent=2))
