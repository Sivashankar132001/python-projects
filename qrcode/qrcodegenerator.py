# import qrcode
# import image 


# qr = qrcode.QRCode(
#     version = 15,
#     box_size = 10,
#     border = 5
# )

# data = "https://g.page/r/CREn8ruc8xRnEAg/review"

# qr.add_data(data)
# qr.make(fit = True)
# img = qr.make_image(fill = "black",back_color = "white" )
# img.save("text.png")


import qrcode 
import image 

qr = qrcode.QRCode(
    version = 15,
    box_size = 5,
    border = 5
)

data = "https://g.page/r/CREn8ruc8xRnEAg/review"

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "white")
img.save('qrcode.png')

