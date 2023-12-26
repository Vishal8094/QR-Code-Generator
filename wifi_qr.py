import qrcode 

ssid="ibe"
password = "edfdfwoorie"
security_type = "WPA"

wifi_data = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
img = qrcode.make(wifi_data)
img.save("wifii.png")
