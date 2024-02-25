import cv2
import win32api

# Define your icon path (replace with your actual icon file)
icon_path = "path/to/your/icon.ico"

# Load the icon using win32api functions
icon_handle = win32api.LoadIconFromFile(icon_path)

# Function to set the window icon (requires window handle)
def set_window_icon(window_handle, icon_handle):
    if not win32api.IsWindow(window_handle):
        raise ValueError("Invalid window handle")
    win32api.SendMessage(window_handle, win32api.WM_SETICON, win32api.ICON_SMALL, icon_handle)
    win32api.SendMessage(window_handle, win32api.WM_SETICON, win32api.ICON_BIG, icon_handle)

# Create an OpenCV window
image = cv2.imread("image.jpg")
cv2.imshow("My Window", image)

# Get the window handle using win32api functions
window_handle = win32api.FindWindow(None, "My Window")

# Set the window icon (assuming successful handle retrieval)
if window_handle:
    set_window_icon(window_handle, icon_handle)
else:
    print("Failed to retrieve window handle")

cv2.waitKey(0)
cv2.destroyAllWindows()
