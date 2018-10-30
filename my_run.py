import cv2
import os
import sys

def main(argv):
    content = argv[0]
    style = argv[1]
    output = argv[2]
    interim_content = "img_without_alpha.jpg"
    interim_output = "image_output/result/result.png"
    format_string = "python neural_style.py --content_img {} --style_imgs {} --max_size 1000 --max_iterations 100 --original_colors --device /gpu:0 --verbose"

    img_with_alpha = cv2.imread(content, -1);
    height, width, channels = img_with_alpha.shape

    if channels >= 4:
        alpha = img_with_alpha[:,:,3]
        img_without_alpha = img_with_alpha[:,:,:3]
    else:
        img_without_alpha = img_with_alpha

    cv2.imwrite("image_input/" + interim_content, img_without_alpha);
    exec_string = format_string.format(interim_content, style)
    print(exec_string)
    os.system(exec_string)

    processed = cv2.imread(interim_output)

    try:
        os.remove(interim_output)
    except:
        pass

    original_resized = cv2.resize(processed, (width, height))

    if channels >= 4:
        merged = cv2.merge((original_resized, alpha))
    else:
        merged = original_resized

    cv2.imwrite(output, merged)

if __name__ == "__main__":
    main(sys.argv[1:])

