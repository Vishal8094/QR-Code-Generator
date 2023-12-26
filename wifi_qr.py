import qrcode 

ssid="JioFiber-CNrfC_5G"
password = "Aihohiewoorie0Ph"
security_type = "WPA"

wifi_data = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
img = qrcode.make(wifi_data)
img.save("wifii.png")