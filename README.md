# Smile Detection and Attendance Marking

This repository contains a Python script (`main.py`) for smile detection and attendance marking using a webcam. The script uses OpenCV, face_recognition, and Tkinter libraries. Additionally, it includes the required files (`attendance.csv`, `haarcascade_frontalface_default.xml`, and `haarcascade_smile.xml`).
![image](https://github.com/agung-madani/smile-recognition-attendance/assets/121701309/def7f761-465c-4356-ba3d-33df56ecdb43)


## Files

1. **main.py**: Python script for smile detection and attendance marking. The script uses the webcam to detect faces, smiles, and mark attendance.

2. **attendance.csv**: CSV file to store attendance records. The file is updated with the name of individuals who smile during the webcam feed.

3. **haarcascade_frontalface_default.xml**: XML file containing the Haar Cascade classifier for face detection.

4. **haarcascade_smile.xml**: XML file containing the Haar Cascade classifier for smile detection.

5. **images/**: Folder containing close-up images of individuals. These images are used for face recognition during the webcam feed.


## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install the required Python libraries:

   ```bash
   pip install opencv-python face-recognition pillow
   ```

3. Run the `main.py` script:

   ```bash
   python main.py
   ```

4. The Tkinter GUI window will open, showing the webcam feed. The script will detect faces and smiles, mark attendance for smiling individuals, and display the results in the Tkinter window.

5. To close the application, click the "Close" button.

## Note

Make sure to have Python installed on your system along with the required libraries specified in the requirements

Feel free to customize the script and cascade files for your specific use case.
