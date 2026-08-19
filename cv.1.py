import cv2

# Read the image
image = cv2.imread(r"C:\Users\DELL\OneDrive\画像\input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display grayscale image
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    cv2.imwrite(r"C:\Users\DELL\OneDrive\画像\grayscale_image.jpg", gray)

    print("Image converted to grayscale successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
