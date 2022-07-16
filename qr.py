import qrcode

qr_date = 'http://www.naver.com'
qr_img = qrcode.make(qr_date)

save_path = 'myqr.png'
qr_img.save(save_path)
