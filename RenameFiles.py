import os

## Rename all fieles in a directory without floder

workspace = 'F:\Download\BLSBookDetailStyle\FormatedImages\qrcode'

for i, filename in enumerate(os.listdir(workspace)):
    os.rename(os.path.join(workspace, filename), os.path.join(workspace, 'qrcode_' + filename))
    print('rename ' + filename + ' to ' + 'qrcode_' + filename)