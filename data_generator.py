
def duplicate_images(file_path, nums):
    labels = []
    src_file = file_path + "apple.png"
    with open(src_file, 'rb') as f_in:
        context = f_in.read()
        for index in range(1000*nums):
            new_file = file_path+"images/"+"apple_" + str(index) + ".png"
            labels.append("images/apple_" + str(index) + ".png")
            with open(new_file, 'wb') as f_out:
                f_out.write(context)
    return labels


if __name__ == '__main__':
    each_dumplicated = 20
    label = duplicate_images(
        "/data00/chengyang.cy/project/data/", each_dumplicated)
    x_count = 0
    with open("/data00/chengyang.cy/project/data/train.txt", "w") as f:
        for x in label:
            f.write(x + "   " + str(x_count // each_dumplicated)+"\n")
            x_count += 1
