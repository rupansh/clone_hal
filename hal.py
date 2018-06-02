
#
# Copyright © 2018, "rupansh" <rupanshsekar@hotmail.com>
#
# This software is licensed under the terms of the GNU General Public
# License version 2, as published by the Free Software Foundation, and
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
    repo = Repo.clone_from(
        link, directory,
        branch=br
    )


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
mm_core = "hardware/qcom/mm-core"
msm8960 = "hardware/qcom/msm8690"
display_mdss = "hardware/qcom/display-mdss"
mm_video = "hardware/qcom/mm-video"
media_v4l2 = "hardware/qcom/media-v4l2"

c_audio = "https://github.com/LineageOS/android_hardware_qcom_audio.git"
c_display = "https://github.com/LineageOS/android_hardware_qcom_display.git"
c_media = "https://github.com/LineageOS/android_hardware_qcom_media.git"
c_camera = "https://github.com/LineageOS/android_hardware_qcom_camera.git"
c_fm = "https://github.com/LineageOS/android_hardware_qcom_fm.git"
c_gps = "https://github.com/LineageOS/android_hardware_qcom_gps.git"
c_power = "https://github.com/LineageOS/android_hardware_qcom_power.git"
c_keymaster = "https://github.com/LineageOS/android_hardware_qcom_keymaster.git"
c_sensors = "https://github.com/LineageOS/android_hardware_qcom_sensors.git"
c_mm_core = "https://github.com/LineageOS/android_hardware_qcom_mm-core.git"
c_msm8960 = "https://github.com/LineageOS/android_hardware_qcom_msm8960.git"
c_display_mdss = "https://github.com/LineageOS/android_hardware_qcom_display-mdss.git"
c_mm_video = "https://github.com/LineageOS/android_hardware_qcom_mm-video.git"
c_media_v4l2 = "https://github.com/LineageOS/android_hardware_qcom_media-v4l2.git"

b = "lineage-15.1"
bc = "lineage-15.1-caf-8996"

ask = raw_input("clone HALs? y/n ")

if ask == "y":
    if os.path.isdir(audio):
        print("Audio HAL exists! It won't be cloned")
    else:
        hal(c_audio, audio, b)
        print("Audio HAL cloned")
    if os.path.isdir(display):
        print("Display HAL exists! It won't be cloned")
    else:
        hal(c_display, display, b)
        print("Display HAL cloned")
    if os.path.isdir(media):
        print("Media HAL exists! It won't be cloned")
    else:
        hal(c_media, media, b)
    if os.path.isdir(camera):
        print("Camera HAL exists! It won't be cloned")
    else:
        hal(c_camera, camera, b)
        print("Camera HAL cloned")
    if os.path.isdir(fm):
        print("FM HAL exists! It won't be cloned")
    else:
        hal(c_fm, fm, b)
        print("FM HAL cloned")
    if os.path.isdir(gps):
        print("GPS HAL exists! It won't be cloned")
    else:
        hal(c_gps, gps, b)
        print("GPS HAL cloned")
    if os.path.isdir(media_caf):
        print("Media CAF HAL exists! It won't be cloned")
    else:
        hal(c_media, media_caf, bc)
        print("Media CAF HAL cloned")
    if os.path.isdir(display_caf):
        print("Display CAF HAL exists! It won't be cloned")
    else:
        hal(c_display, display_caf, bc)
        print("Display CAF HAL cloned")
    if os.path.isdir(audio_caf):
        print("AUDIO CAF HAL EXISTS! It won't be cloned")
    else:
        hal(c_audio, audio_caf, bc)
    print("Cloned the missing HALs")

elif ask == "n":
    print("k bye")

else:
    print("wrong input bhsdk")
