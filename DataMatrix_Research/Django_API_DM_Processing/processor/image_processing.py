import cv2
import numpy as np
import base64
import io

def load_image(image):
    return cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)

def edge_detection(image):
    return cv2.Canny(image, 50, 150, apertureSize=3)

def hough_transform(edges):
    return cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)

def polar_to_cartesian(rho, theta):
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    return ((x1, y1), (x2, y2))

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('Lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def draw_lines_and_intersection(image, lines):
    # Create a copy of the image to draw lines and intersections
    image_copy = np.copy(image)

    line_1 = polar_to_cartesian(*lines[0][0])
    line_3 = polar_to_cartesian(*lines[2][0])

    cv2.line(image_copy, line_1[0], line_1[1], (0, 0, 255), 2)
    cv2.line(image_copy, line_3[0], line_3[1], (0, 0, 255), 2)

    x, y = line_intersection(line_1, line_3)
    intersection_point = (int(x), int(y))

    if 0 <= x < image_copy.shape[1] and 0 <= y < image_copy.shape[0]:
        cv2.circle(image_copy, intersection_point, 5, (0, 255, 255), -1)  # Highlight the intersection point in yellow color
        cv2.line(image_copy, (intersection_point[0], 0), (intersection_point[0], image_copy.shape[0]), (0, 255, 0), 2)  # Vertical line
        cv2.line(image_copy, (0, intersection_point[1]), (image_copy.shape[1], intersection_point[1]), (0, 255, 0), 2)  # Horizontal line

    # Create a copy of the image without the lines and intersections
    image_without_lines = np.copy(image)
    cv2.circle(image_without_lines, intersection_point, 5, (0, 0, 0), -1)  # Set the intersection point to black
    cv2.line(image_without_lines, line_1[0], line_1[1], (255, 255, 255), 2)  # Set line 1 to black
    cv2.line(image_without_lines, line_3[0], line_3[1], (255, 255, 255), 2)  # Set line 3 to black

    return image_copy, image_without_lines


def calculate_rotation_angle(lines):
    line_1_angle = np.degrees(lines[0][0][1])
    diff_angle = abs(line_1_angle - 90) % 180
    angle_clockwise = 360 - diff_angle if line_1_angle > 90 else diff_angle
    angle_anticlockwise = diff_angle if line_1_angle > 90 else 360 - diff_angle

    if angle_clockwise < angle_anticlockwise:
        rotation_angle = angle_clockwise
    else:
        rotation_angle = angle_anticlockwise

    return rotation_angle

def rotate_image(original_image, rotation_angle):
    center = (original_image.shape[1] // 2, original_image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1)
    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (original_image.shape[1], original_image.shape[0]))
    return rotated_image

def process_image(image):
    original_image = load_image(image)
    edges = edge_detection(original_image)
    lines = hough_transform(edges)
    processed_image, image_without_lines = draw_lines_and_intersection(original_image, lines)
    rotation_angle = calculate_rotation_angle(lines)
    rotated_image = rotate_image(image_without_lines, rotation_angle)

    # Convert the processed image to base64
    is_success, buffer = cv2.imencode(".jpg", rotated_image)
    base64_str = base64.b64encode(buffer).decode('utf-8')

    return base64_str
