"""
pip debug --verbose

cd 12.10.4/

pyenv local 3.8.10

python win_amd64.py
"""

import zipfile

version = "12.10.4"
tag = "py38-none-win_amd64"

egg_file = f"frida-{version}-py3.8-win-amd64.egg"
wheel_file = f"frida-{version}-{tag}.whl"

dist_info = f"frida-{version}.dist-info"

with zipfile.ZipFile(egg_file, "r") as egg, zipfile.ZipFile(wheel_file, "w", zipfile.ZIP_DEFLATED) as whl:
    for item in egg.infolist():
        whl.writestr(item, egg.read(item.filename))

    whl.writestr(f"{dist_info}/WHEEL", f"Wheel-Version: 1.0\nTag: {tag}\n")
    whl.writestr(f"{dist_info}/METADATA", f"Metadata-Version: 2.1\nName: frida\nVersion: {version}\n")
    whl.writestr(f"{dist_info}/RECORD", "")

print(f"$ pip install {wheel_file} --force-reinstall")
