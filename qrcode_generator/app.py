# Importing library
import qrcode
import cv2

def generate_qrcode(data):
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    # Adding data to the instance 'qr'
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='red',
                        back_color='white')
    return  img


#img = generate_qrcode("chandima")
#img.save('MyQRCode.png')

def reade_qrcode(filepath):
    image = cv2.imread(filepath)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    return data

#print(reade_qrcode("MyQRCode.png"))