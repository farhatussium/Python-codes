import qrcode

link = input("Enter the link/URL: ")

qr = qrcode.make(link)

qr.save("qrcode.png")
print("QR Code saved as qrcode.png")
qr.show()