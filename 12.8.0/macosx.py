"""
arch -x86_64 bash

cd 12.8.0/

pyenv local 3.6.15

python macosx.py

pip install frida-12.8.0-cp36-cp36m-macosx_10_9_x86_64.whl --force-reinstall
"""

import zipfile

egg_file = "frida-12.8.0-py3.6-macosx-10.6-intel.egg"
wheel_file = "frida-12.8.0-cp36-cp36m-macosx_10_9_x86_64.whl"

dist_info = "frida-12.8.0.dist-info"

with zipfile.ZipFile(egg_file, "r") as egg, zipfile.ZipFile(wheel_file, "w", zipfile.ZIP_DEFLATED) as whl:
    for item in egg.infolist():
        whl.writestr(item, egg.read(item.filename))

    whl.writestr(f"{dist_info}/WHEEL", "Wheel-Version: 1.0\nTag: cp36-cp36m-macosx_10_9_x86_64\n")
    whl.writestr(f"{dist_info}/METADATA", "Metadata-Version: 2.1\nName: frida\nVersion: 12.8.0\n")
    whl.writestr(f"{dist_info}/RECORD", "")

print(f"$ pip install {wheel_file} --force-reinstall")
