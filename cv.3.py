import cv2

# Read the input image
image = cv2.imread(r"C:\Users\DELL\OneDrive\画像\Screenshots")

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the outline/edges
    cv2.imshow("Canny Edge Image", edges)

    # Save the output image
    cv2.imwrite(r"C:\ImageProcessing\canny_edges.jpg", edges)

    print("Image outline detected successfully using Canny function.")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
