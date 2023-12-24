import qrcode

texto = input("Que quieres poner en el QR?")

data = texto

qr = qrcode.QRCode(version = 1, box_size=100, border = 5)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = "black", back_color = "white")

img.save("C:/Users/gabri/Documents/Programacion/python/primer-hola/imagenes-qr/qr.png")