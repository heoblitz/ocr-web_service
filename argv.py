# -*- coding:utf-8 -*-
from PIL import Image
import pytesseract
import argparse
import cv2

'''
커맨드 명령어
tesseract hangle.png o2 --oem 1 -l kor
'''
parser = argparse.ArgumentParser()
# 필수 옵션
parser.add_argument('img_arg', type=str, help='이미지 파일의 경로 입력')
parser.add_argument('text_arg', type=str, help='stdout 텍스트 파일 이름')
# 선택 옵션
parser.add_argument('-c', action='store_true', help='cv2로 OCR 정확도 올리기')
parser.add_argument('-stdout', action='store_true', help='cmd에 OCR 내용 출력하기')
parser.add_argument('-ko', action='store_true', help='한글로 된 이미지 OCR')
parser.add_argument('-all', action='store_true', help='한글과 영문이 포함된 이미지 OCR')               
args = parser.parse_args()

def main():
    config = '--oem 1 --psm 3'

    img_path = args.img_arg
    text_path = args.text_arg
    if args.ko: # OCR 언어 선택 옵션
        config = '-l kor ' + config
    elif args.all:
        config = '-l eng+kor ' + config
    else:
        config = '-l eng ' + config

    if args.c: # -c 옵션이 체크되어 있으면 cv2img()
        #print('cv2img()')
        text = cv2img(img_path, config)

    else: # 그 외에는 img2text()
        #print('img2text()')
        text = img2text(img_path, config)
    
    if args.stdout:
        print(text)

    text_save(text_path, text)

def cv2img(img_path, user_config):
    '''
    이미지 그레이 스케일로 변환 후 OCR

    img_path: 이미지 경로
    '''
    image = cv2.imread(img_path) # 이미지 로드
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이 스케일로 변환
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # 
    
    return pytesseract.image_to_string(gray, config=user_config) #not use Image.open

def img2text(img_path, user_config):
    '''
    이미지 OCR

    img_path: 이미지 경로
    '''
    return pytesseract.image_to_string(Image.open(img_path), config=user_config)

def text_save(text_path, text):
    '''
    텍스트 파일로 저장하기

    text_path: 텍스트 파일 저장 경로
    text: OCR 변환 텍스트
    '''
    with open(text_path, 'w', encoding='UTF8') as f:
        f.write(text)

if __name__ == '__main__':
    main()
