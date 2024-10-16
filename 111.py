import cv2
import numpy as np
import os
import glob

def create_output_folder(folder_name):
    absolute_path = os.path.abspath(folder_name)
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
        print(f"已创建文件夹：{absolute_path}")
    else:
        print(f"文件夹已存在：{absolute_path}")
    return absolute_path

def get_image_files(supported_formats=['.jpg', '.png', '.jpeg', '.bmp', '.tiff']):
    files = []
    for ext in supported_formats:
        files.extend(glob.glob(f"*{ext}"))
    return files

def is_rectangle(contour, epsilon_ratio=0.02, min_area=1000):
    perimeter = cv2.arcLength(contour, True)
    epsilon = epsilon_ratio * perimeter
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4 and cv2.isContourConvex(approx):
        area = cv2.contourArea(approx)
        if area > min_area:
            return True, approx
    return False, None

def process_image(image_path, output_folder, image_id):
    image = cv2.imread(image_path)
    if image is None:
        print(f"无法读取图像：{image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 使用自适应阈值以处理不同光照条件
    thresh = cv2.adaptiveThreshold(blurred, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # 使用形态学操作填补小洞
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rect_count = 0
    for idx, contour in enumerate(contours):
        is_rect, approx = is_rectangle(contour)
        if is_rect:
            x, y, w, h = cv2.boundingRect(approx)
            # 可根据需要调整裁剪的区域，例如增加边距
            margin = 5
            x_start = max(x - margin, 0)
            y_start = max(y - margin, 0)
            x_end = min(x + w + margin, image.shape[1])
            y_end = min(y + h + margin, image.shape[0])

            # 打印裁剪区域信息
            print(f"裁剪区域：x_start={x_start}, y_start={y_start}, x_end={x_end}, y_end={y_end}, width={x_end - x_start}, height={y_end - y_start}")

            cropped = image[y_start:y_end, x_start:x_end]

            # 检查 cropped 是否有效
            if cropped.size == 0:
                print(f"裁剪后的图像为空，跳过保存：{image_path} 中的轮廓 {idx}")
                continue

            # 可视化长方形
            cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)

            # 生成唯一的文件名
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            cropped_filename = f"{base_name}_rect_{rect_count + 1}.png"
            save_path = os.path.join(output_folder, cropped_filename)
            absolute_save_path = os.path.abspath(save_path)
            print(f"将保存到：{absolute_save_path}")
            success = cv2.imwrite(absolute_save_path, cropped)
            if success:
                rect_count += 1
                print(f"已保存：{save_path}")
            else:
                print(f"保存失败：{save_path}")

    # 保存带有检测到的长方形的图像，以便检查
    annotated_image_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_annotated.png")
    annotation_success = cv2.imwrite(annotated_image_path, image)
    if annotation_success:
        print(f"已保存带注释的图像：{annotated_image_path}")
    else:
        print(f"保存带注释的图像失败：{annotated_image_path}")

    if rect_count == 0:
        print(f"在图像 {image_path} 中未检测到长方形。")
    else:
        print(f"在图像 {image_path} 中检测并保存了 {rect_count} 个长方形。")

def main():
    print(f"当前工作目录：{os.getcwd()}")
    output_folder = "MahjongImages"  # 使用英文文件夹名，确保编码兼容
    absolute_output_folder = create_output_folder(output_folder)

    image_files = get_image_files()
    if not image_files:
        print("当前目录下没有支持的图片文件。")
        return

    print(f"找到 {len(image_files)} 张图片。开始处理...")

    for idx, image_file in enumerate(image_files):
        print(f"\n处理 {idx + 1}/{len(image_files)}: {image_file}")
        process_image(image_file, absolute_output_folder, idx + 1)

    print("\n所有图片处理完成。")

if __name__ == "__main__":
    main()
