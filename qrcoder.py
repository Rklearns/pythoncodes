import qrcode
upid=input("input your UPI id: ")


phonepe_url=f"upi://pay?pa={upid}&pn=Recipient%20Name&mc=1234"
paytm_url=f"upi://pay?pa={upid}&pn=Recipient%20Name&mc=1234"
gpay_url=f"upi://pay?pa={upid}&pn=Recipient%20Name&mc=1234"

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
gpay_qr=qrcode.make(gpay_url)

phonepe_qr.save('phonepe_qr.png')#saving the qr codes in the form of images
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

#pillow has been used here so as to display the qr code 
phonepe_qr.show()
gpay_qr.show()
paytm_qr.show()
