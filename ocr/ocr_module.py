from imutils.perspective import four_point_transform
import imutils
from easyocr import Reader
import cv2


def make_scan_image(image, width, ksize=(5, 5), min_threshold=75, max_threshold=200):
    origin_image = image

    image = imutils.resize(image, width=width)
    ratio = origin_image.shape[1] / float(image.shape[1])

    # 이미지를 grayscale로 변환하고 blur를 적용
    # 모서리를 찾기위한 이미지 연산
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, ksize, 0)
    edged = cv2.Canny(blurred, min_threshold, max_threshold)

    image_list_title = ['gray', 'blurred', 'edged']
    image_list = [gray, blurred, edged]

    # contours를 찾아 크기순으로 정렬
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    findCnt = None

    # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영역으로 판단하고 break
        if len(approx) == 4:
            findCnt = approx
            break

    # 만약 추출한 윤곽이 없을 경우 그냥 기존꺼 반환
    if findCnt is None:
        return origin_image

    output = image.copy()
    cv2.drawContours(output, [findCnt], -1, (0, 255, 0), 2)

    image_list_title.append("Outline")
    image_list.append(output)

    # 원본 이미지에 찾은 윤곽을 기준으로 이미지를 보정
    transform_image = four_point_transform(origin_image, findCnt.reshape(4, 2) * ratio)

    return transform_image


def ocr(path):
    image = cv2.imread(path, cv2.IMREAD_COLOR)

    preprocessed_image = make_scan_image(image, width=200, ksize=(5, 5), min_threshold=20, max_threshold=100)

    print("[INFO] OCR'ing input image...")
    reader = Reader(lang_list=['ko', 'en'], gpu=True)

    simple_results = reader.readtext(preprocessed_image, detail=0)

    return simple_results

