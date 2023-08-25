import cv2
import pickle

scaler = pickle.load(open('model\standardscaler.pkl','rb'))
model = pickle.load(open('model\model.pkl','rb'))

img = cv2.imread("output.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
X_data = thresh1/255
X_data = scaler.transform(X_data)
X_data = X_data.reshape((-1,784))
prediction = model.predict(X_data)

print(prediction)
cv2.imwrite("image_cv2.jpg", thresh1)
