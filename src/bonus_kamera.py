import cv2

def kamera():
        cam = cv2.VideoCapture(0)
        img_counter = 0

        while (True):
                ret, frame = cam.read()

                if not ret:
                        print("Tidak bisa membuka aplikasi")
                        break

                cv2.imshow("Penangkap Gambar untuk Python",frame)
                k = cv2.waitKey(1)

                if k%256 == 27:
                        print("Keluar dari kamera")
                        break
                elif k%256 == 32:
                        img_name = "gambar_muka{}.png".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        print("Gambar telah berhasil diambil")
                        img_counter = img_counter + 1

        cv2.destroyAllWindows()