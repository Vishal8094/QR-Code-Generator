import qrcode
#from PIL import Image

qr = qrcode.QRCode(version=None,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=15,border=1)

qr.add_data("https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil")
qr.make(fit=True)
img = qr.make_image()
img.save("stack.png")