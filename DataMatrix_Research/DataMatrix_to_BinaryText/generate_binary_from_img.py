import cv2
import numpy as np

def read_image(path):
    img = cv2.imread(path)
    return img

def show_img(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def datamatrix_to_binary(image_path):
    image = read_image(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    binary_image = cv2.bitwise_not(binary_image)

    # show_img(binary_image)

    binary_matrix = (binary_image / 255).astype(int)

    return binary_matrix

def convert_to_single_entry_matrix(binary_matrix):
    num_rows, num_cols = binary_matrix.shape
    block_size = 5

    num_row_blocks = num_rows // block_size
    num_col_blocks = num_cols // block_size

    new_matrix = np.zeros((num_row_blocks, num_col_blocks), dtype=int)

    for i in range(0, num_row_blocks * block_size, block_size):
        for j in range(0, num_col_blocks * block_size, block_size):
            block = binary_matrix[i:i+block_size, j:j+block_size]
            entry = 1 if np.any(block) else 0
            new_matrix[i//block_size, j//block_size] = entry

    return new_matrix

def convert_to_single_entry_matrix_max(binary_matrix):
    num_rows, num_cols = binary_matrix.shape
    block_size = 5

    num_row_blocks = num_rows // block_size
    num_col_blocks = num_cols // block_size

    new_matrix = np.zeros((num_row_blocks, num_col_blocks), dtype=int)

    for i in range(0, num_row_blocks * block_size, block_size):
        for j in range(0, num_col_blocks * block_size, block_size):
            block = binary_matrix[i:i+block_size, j:j+block_size]
            num_zeros = np.sum(block == 0)
            num_ones = np.sum(block == 1)
            entry = 0 if num_zeros >= num_ones else 1
            new_matrix[i//block_size, j//block_size] = entry

    return new_matrix

def convert_to_single_entry_matrix_max_skip(binary_matrix):
    num_rows, num_cols = binary_matrix.shape
    block_size = 5

    binary_matrix = binary_matrix[2:-2, :]

    binary_matrix = binary_matrix[:, 2:-2]

    num_row_blocks = num_rows // block_size
    num_col_blocks = num_cols // block_size

    new_matrix = np.zeros((num_row_blocks, num_col_blocks), dtype=int)

    for i in range(0, num_row_blocks * block_size, block_size):
        for j in range(0, num_col_blocks * block_size, block_size):
            block = binary_matrix[i:i+block_size, j:j+block_size]
            num_zeros = np.sum(block == 0)
            num_ones = np.sum(block == 1)
            entry = 0 if num_zeros >= num_ones else 1
            new_matrix[i//block_size, j//block_size] = entry

    return new_matrix



def write_new_data_to_file(file_path, new_data):
    try:
        new_data_str = "\n".join(" ".join(map(str, row)) for row in new_data)

        with open(file_path, 'w') as file:
            file.write(new_data_str)

        print("Data written successfully!")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    image_path = 'DataMatrixcode_ABCD.png'

    binary_matrix = datamatrix_to_binary(image_path)
    single_entry_matrix = convert_to_single_entry_matrix(binary_matrix)
    single_entry_matrix_max = convert_to_single_entry_matrix_max(binary_matrix)
    single_entry_matrix_max_skip = convert_to_single_entry_matrix_max_skip(binary_matrix)

    write_new_data_to_file("binary_text.txt", binary_matrix)
    write_new_data_to_file("binary_text_entry.txt", single_entry_matrix)
    write_new_data_to_file("binary_text_max.txt", single_entry_matrix_max)
    write_new_data_to_file("binary_text_max_skip.txt", single_entry_matrix_max_skip)
