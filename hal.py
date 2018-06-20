#
# Copyright © 2018, "rupansh" <rupanshsekar@hotmail.com>
#
# This software is licensed under the terms of the GNU General Public
# License version 3, as published by the Free Software Foundation, and
# may be copied, distributed, and modified under those terms.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# Please maintain this if you use this script or any part of it

from git import *
import os

logo = """o  o   O  o          o-o o     o-o  o   o o--o o--o 
|  |  / \ |         /    |    o   o |\  | |    |   |
O--O o---o|        O     |    |   | | \ | O-o  O-Oo 
|  | |   ||         \    |    o   o |  \| |    |  \ 
o  o o   oO---o      o-o O---o o-o  o   o o--o o   o
~Brought to you by RUPANSHKEK
~GPL V3
~Made with love"""
print(logo)


def hal(link, directory, br):
    if os.path.isdir(directory):
        print(directory+" exists! It won't be cloned!")
    else:
        repo = Repo.clone_from(
            link, directory,
            branch=br
        )
        print(directory+" HAL cloned!")


audio = "hardware/qcom/audio"
display = "hardware/qcom/display"
media = "hardware/qcom/media"
camera = "hardware/qcom/camera"
fm = "hardware/qcom/fm"
gps = "hardware/qcom/gps"
power = "hardware/qcom/power"
keymaster = "hardware/qcom/keymaster"
display_caf = "hardware/qcom/display-caf/msm8996"
media_caf = "hardware/qcom/media-caf/msm8996"
audio_caf = "hardware/qcom/audio-caf/msm8996"

c_audio = "https://github.com/LineageOS/android_hardware_qcom_audio.git"
c_display = "https://github.com/LineageOS/android_hardware_qcom_display.git"
c_media = "https://github.com/LineageOS/android_hardware_qcom_media.git"
c_camera = "https://github.com/LineageOS/android_hardware_qcom_camera.git"
c_fm = "https://github.com/LineageOS/android_hardware_qcom_fm.git"
c_gps = "https://github.com/LineageOS/android_hardware_qcom_gps.git"
c_power = "https://github.com/LineageOS/android_hardware_qcom_power.git"
c_keymaster = "https://github.com/LineageOS/android_hardware_qcom_keymaster.git"


b = "lineage-15.1"
bc = "lineage-15.1-caf-8996"
kek = [(c_audio, audio, b), (c_display, display, b), (c_media, media, b), (c_camera, camera, b), (c_fm, fm, b), (c_gps, gps, b), (c_media, media_caf, bc), (c_display, display_caf, bc), (c_audio, audio_caf, bc), (c_power, power, b), (c_keymaster, keymaster, b)]
ask = raw_input("clone HALs? y/n ")

if ask == "y":
    for i in kek:
        hal(*i)
    print("Cloned the missing HALs")

elif ask == "n":
    print("k bye")

else:
    print("wrong input :C")
