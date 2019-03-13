import cv2
import numpy as np
import math

def extract_frames(frame_list, base_width, base_height):
    images = []
    for filename in frame_list:
        print filename
        img = cv2.imread(filename)
        img_h, img_w = img.shape[:2]
        if (float(img_w)/img_h) > (float(base_width)/base_height):
            new_w = base_width
            new_h = new_w * img_h / img_w
            padding_l = 0
            padding_t = (base_height - new_h) / 2
            padding_r = 0
            padding_b = base_height - new_h - padding_t
            padding_color = cv2.mean(img[img_h-4:img_h,:,:])
        else:
            new_h = base_height
            new_w = new_h * img_w / img_h
            padding_l = (base_width - new_w) / 2
            padding_t = 0
            padding_r = base_width - new_w - padding_l
            padding_b = 0
            padding_color = cv2.mean(img[:,img_w-5:img_w,:])
        img = cv2.resize(img, (new_w, new_h))
        img = cv2.copyMakeBorder(img, left=padding_l, top=padding_t, right=padding_r, bottom=padding_b, borderType=cv2.BORDER_CONSTANT, value=padding_color)
        images.append(img)
    return images

def add_swipe_transition_frames_with_duration(image_info, n_steps=10, transit_duration=1):
    images = []
    for i in range(len(image_info)-1):
        images.append(image_info[i])
        img1 = image_info[i][0]
        img2 = image_info[i+1][0]
        step_duration = transit_duration * 30.0 / n_steps
        step_size = img1.shape[1] / n_steps
        for step in range(n_steps):
            img_transit = np.concatenate([img1[:,step*step_size:,:], img2[:,:step*step_size,:]], axis=1)
            images.append((img_transit, step_duration))
    images.append(image_info[-1])
    return images

def animate(order_input_path, video_output_path):
    frame_info = [line.split(',') for line in open(order_input_path).read().split('\n')[1:]]
    frame_list = [f[0] for f in frame_info]
    frame_duration = [int(f[1])*30 for f in frame_info]

    base_height, base_width = cv2.imread(frame_list[0]).shape[:2]
    for f in frame_info:
        if f[2] == '1':
            base_height, base_width = cv2.imread(f[0]).shape[:2]
            break

    print base_width, base_height
    print frame_list
    images = extract_frames(frame_list, base_width, base_height)
    image_info = [(images[i], frame_duration[i]) for i in range(len(images))]
    image_info = add_swipe_transition_frames_with_duration(image_info, 10, 0.5)

    video_output_path
    fps = 30
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    video_writer = cv2.VideoWriter(video_output_path, fourcc, fps, (base_width, base_height))
    for img, duration in image_info:
        # cv2.imshow(' ',img)
        # cv2.waitKey(0)
        for i in range(int(math.ceil(duration))):
            video_writer.write(img)
    video_writer.release()

if __name__ == '__main__':
    animate(order_input_path='order.csv', video_output_path='output.mp4')