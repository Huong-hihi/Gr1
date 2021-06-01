import object_fake_new
def main():
    new = {}
    new['timestamp'], new['content'] = None, None
    #new['content'] = "BN386 53 tuổi địa chỉ tại Thanh Tuyền, TP Phủ Lý, Hà Nam"
    # new['content'] = "Bệnh nhân 250 - nữ, 50 tuổi, trú tại Hạ Lôi, Mê Linh, Hà Nội. Bệnh nhân là hàng xóm và có tiếp xúc gần BN243"
    #new['content'] = "BN30410 giới tính nam - 80  tuổi"
    new['content'] =" Bệnh nhân 401 giới tính Nam 14 tuổi"
    if object_fake_new.checkObject(new['content']):
        print("Tin thật !!!!!!")
    else:
        print("Tin giả !!!")

if __name__ == '__main__':
    main()