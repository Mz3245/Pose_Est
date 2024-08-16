from ultralytics import YOLO
import cv2

# Load the pre-trained model from ultralytics
model = YOLO('yolov8n-pose.pt')

# Function for processing image
def process_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return

    results = model(image, conf=0.3)
    annotated_image = results[0].plot()

    save_path = r'C:\gui\result.jpg'
    cv2.imwrite(save_path, annotated_image)

    saved_image = cv2.imread(save_path)
    if saved_image is None:
        print("Error: Could not load saved image.")
        return

    screen_width = 800
    screen_height = 800
    height, width = saved_image.shape[:2]

    if width > screen_width or height > screen_height:
        scaling_factor = min(screen_width / width, screen_height / height)
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        resized_image = cv2.resize(saved_image, (new_width, new_height))
    else:
        resized_image = saved_image

    cv2.imshow('Pose Estimation', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function for processing video
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(r'C:\gui\result_video.avi', fourcc, 20.0,
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.3)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

        cv2.imshow('Pose Estimation', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Function for using webcam
def process_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.3)
        annotated_frame = results[0].plot()

        cv2.imshow('Pose Estimation', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main program
def main():
    while True:
        print("Choose an option:")
        print("1. Process an image")
        print("2. Process a video")
        print("3. Use webcam")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            image_path = input("Enter the path to the image: ")
            process_image(image_path)
        elif choice == '2':
            video_path = input("Enter the path to the video: ")
            process_video(video_path)
        elif choice == '3':
            process_webcam()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
