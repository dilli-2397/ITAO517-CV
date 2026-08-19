import cv2

# Read the input image
image = cv2.imread(r"C:\ImageProcessing\input.jpg")

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the blurred image
    cv2.imshow("Gaussian Blurred Image", blurred)

    # Save the blurred image
    cv2.imwrite(r"C:\ImageProcessing\blurred_image.jpg", blurred)

    print("Image blurred successfully using Gaussian Blur.")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
