import cv2

# Load images
reference = cv2.imread("reference.jpg")
test = cv2.imread("test.jpg")

if reference is None or test is None:
    print("Images not found!")
    exit()

# Resize
test = cv2.resize(test, (reference.shape[1], reference.shape[0]))

# Convert to grayscale
gray_ref = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
gray_test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

# Blur to reduce noise
gray_ref = cv2.GaussianBlur(gray_ref, (5,5), 0)
gray_test = cv2.GaussianBlur(gray_test, (5,5), 0)

# Difference
diff = cv2.absdiff(gray_ref, gray_test)

# Threshold
_, thresh = cv2.threshold(diff, 15, 255, cv2.THRESH_BINARY)

# Dilate to join nearby pixels
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
thresh = cv2.dilate(thresh, kernel, iterations=2)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw defect rectangle
for c in contours:
    if cv2.contourArea(c) > 200:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(test, (x, y), (x+w, y+h), (0,0,255), 3)
        cv2.putText(test, "Defect", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

# Show output
cv2.imshow("Reference Image", reference)
cv2.imshow("Test Image", test)
cv2.imshow("Difference", diff)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
