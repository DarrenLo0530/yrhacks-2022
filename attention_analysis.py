import cv2

eye_cascade = cv2.CascadeClassifier('./datasets/haarcascade_eye.xml')

def outline_eyes(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
  for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


def is_focused(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
  for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

