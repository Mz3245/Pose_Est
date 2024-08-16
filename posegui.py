import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pose_est import process_image, process_video, process_webcam

class PoseDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pose Detection GUI")

        # Load the background image
        self.background_image = Image.open(r"C:\gui\ai.jpg")  # Replace with your image path
        self.background_image = self.background_image.resize((800, 600), Image.LANCZOS)  # Resize as needed
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  # Make it fill the entire window

        # Create a frame for buttons
        self.button_frame = tk.Frame(root, bg='black')
        self.button_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.label = tk.Label(self.button_frame, text="Choose an option:", bg='lightblue', fg='black')
        self.label.pack(pady=10)

        # Pack buttons vertically
        self.btn_image = tk.Button(self.button_frame, text="Process Image", command=self.load_image, bg='yellow', fg='black')
        self.btn_image.pack(pady=5)

        self.btn_video = tk.Button(self.button_frame, text="Process Video", command=self.load_video, bg='yellow', fg='black')
        self.btn_video.pack(pady=5)

        self.btn_webcam = tk.Button(self.button_frame, text="Use Webcam", command=self.use_webcam, bg='yellow', fg='black')
        self.btn_webcam.pack(pady=5)

        self.btn_exit = tk.Button(self.button_frame, text="Exit", command=root.quit, bg='red', fg='white')
        self.btn_exit.pack(pady=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", 
                                                filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            process_image(file_path)

    def load_video(self):
        file_path = filedialog.askopenfilename(title="Select a Video", 
                                                filetypes=[("Video Files", "*.mp4 *.avi")])
        if file_path:
            process_video(file_path)

    def use_webcam(self):
        process_webcam()

if __name__ == "__main__":
    root = tk.Tk()
    app = PoseDetectionApp(root)
    root.mainloop()
