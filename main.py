####### basic text  #############


# import qrcode
# img =qrcode.make("hello world !")
# img.save("myqr.png")

######### you can upload url ########################

# import qrcode
#
# qr = qrcode.QRCode(
# 	version=1,
# 	error_correction=qrcode.constants.ERROR_CORRECT_L,
# 	box_size=15,
# 	border=5
# )
#
# data = ' https ....' ## copy your url here
# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill='black', back_color='white')
# img.save('image1.png') # write image name in here

## to open in explorer
# do it open in explorer with right click.


# import qrcode
# import qrcode.image.svg
# factory = qrcode.image.svg.SvgPathImage
# svg_image = qrcode.make("hello world baybe ",image_factory = factory)
# svg_image.save("myqrcode.svg")


#### with gui ##########
# from tkinter import *
# import pyqrcode
# import qrcode
# import png
# from PIL import ImageTk , Image
# root=Tk()
#
# def generate():
#
#     link_name=name_entry.get()
#     link=link_entry.get()
#     file_name=link_name +".png"
#     url=pyqrcode.create(link)
#     url.png(file_name,scale=5)
#     image=ImageTk.PhotoImage(Image.open(file_name))
#     image_label=Label(image=image)
#     image_label.image=image
#     canvas.create_window(200,400,window=image_label)
#
#
#
#
# canvas=Canvas(root,width=400,height=600)
# canvas.pack()
# app_label=Label(root,text="QR Code Generator",font=("Arial",20))
# canvas.create_window(200,50,window=app_label)
# name_label=Label(root,text='Link Name')
# link_label=Label(root,text="Link")
# canvas.create_window(200,100,window=name_label)
# canvas.create_window(200,160,window=link_label)
# name_entry=Entry(root)
# link_entry=Entry(root)
# canvas.create_window(200,130,window=name_entry)
# canvas.create_window(200,180,window=link_entry)
# button=Button(text="Generate QR Code",command=generate)
# canvas.create_window(200,220,window=button)
#
#
# root.mainloop()