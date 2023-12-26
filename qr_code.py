import qrcode as qr

img = qr.make("https://drive.google.com/drive/folders/1kXXvUM6cGYTBUW5DBM0pYudLKlZpxGo1")
img.save("drive.png")