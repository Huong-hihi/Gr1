import object_fake_new
def main():
    content = "BN 401 giới tính Nam 14 tuổi"

    if object_fake_new.checkObject(content):
        print("True New")
    else:
        print("Fake new")

if __name__ == '__main__':
    main()