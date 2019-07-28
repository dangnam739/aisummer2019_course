#Phuong phap dau vao Window(SM2)
import numpy as np
from PIL import Image

def stereo_matching_ssd(left_img, right_img, kernel_size, disparity_range):

    #doc anh trai va phai roi chuyen sang grayscale
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    #cho truoc hcieu rong va chieu cao cua anh
    height = 288
    width = 384

    #tao disparity_map
    depth = np.zeros((height, width), np.uint8)

    kernel_half = int((kernel_size - 1) / 2)
    scale = 255 / disparity_range

    for y in range(kernel_half, height - kernel_half):
        for x in range(kernel_half, width - kernel_half):

            #tim gia tri j tai do cost co gia tri min
            disparity = 0
            cost_min = 65534

            for j in range(disparity_range):
                ssd = 0
                ssd_temp = 0

                for v in range(-kernel_half, kernel_half):
                    for u in range(-kernel_half, kernel_half):
                        ssd_temp = (int(left[y + v, x + u]) - int(right[y + v, (x + u) - j])) ** 2
                        ssd += ssd_temp

                if ssd < cost_min:
                    cost_min = ssd
                    disparity = j

            #gan j cho cost_min vao disparity map
            depth[y, x] = disparity * scale
    #Chuyen du lieu tu ndarray sang kieu Imang va luu xuong file
    Image.fromarray(depth).save('disparity_map_ssd.png')

if __name__ == '__main__':
    disparity_range = 16
    kernel_size = 5
    stereo_matching_ssd('left.png', 'right.png', kernel_size, disparity_range)
