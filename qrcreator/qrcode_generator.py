import qrcode
import os

def create_qr(link, save_name, folder_path):
    img = qrcode.make(link)
    img.save(f"{folder_path}/{save_name}.png")

 
    