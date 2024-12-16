# Distance Measurement Programs

Welcome to the **Distance Measurement Project**! This repository features two advanced programs for measuring the distance of an object using either a **camera** (Python) or an **ultrasonic sensor** (Arduino). Whether you're a developer, student, or hobbyist, these solutions are designed to provide accurate distance measurements in different scenarios.

---

## 📌 Features

### **Python Program**
- Measures distance using a camera and known object size.
- Displays the calculated distance in real-time on the video feed.
- Flexible for objects with known dimensions.

### **Arduino Program**
- Uses the HC-SR04 ultrasonic sensor to measure object distance.
- Outputs distance in both centimeters and inches.
- Lightweight and easy to integrate into IoT projects.

---

## 🛠️ Technologies Used

### Python Program:
- **Python**
- **OpenCV**
- **NumPy**

### Arduino Program:
- **Arduino IDE**
- **HC-SR04 Ultrasonic Sensor**

---

## 🚀 How to Get Started

### Clone the Repository
```bash
$ git clone https://github.com/<your-username>/distance-measurement.git
$ cd distance-measurement
```

### Running the Python Program

1. **Install Dependencies:**
   ```bash
   pip install opencv-python numpy
   ```

2. **Run the Script:**
   ```bash
   python distance_measurement.py
   ```

3. **Usage:**
   - Place an object with a known width in front of the camera.
   - The program will calculate and display the distance in centimeters.

4. **Stop the Program:**
   - Press `q` to quit.

### Running the Arduino Program

1. **Hardware Setup:**
   - Connect the **HC-SR04 Ultrasonic Sensor** to your Arduino as per the wiring diagram provided.

2. **Upload the Code:**
   - Open `distance_measurement.ino` in the Arduino IDE.
   - Upload the code to your Arduino board.

3. **View the Output:**
   - Open the Serial Monitor in the Arduino IDE.
   - View the measured distance in both centimeters and inches.

---

## 📚 Detailed Explanation

### Python Program Workflow
1. Captures video feed from your webcam.
2. Detects an object using contours and calculates its perceived width.
3. Computes the distance based on the object’s real width and camera focal length.

### Arduino Program Workflow
1. Sends ultrasonic pulses to measure the distance to the object.
2. Calculates the distance based on the speed of sound in air.
3. Outputs the distance in both meters and inches to the Serial Monitor.

---

## 🤖 Acronym-Based Interactive User Name

This project is maintained by **D.E.V.E.L.O.P.E.R**:
- **D**edicated
- **E**ngineer
- **V**isionary
- **E**nthusiast
- **L**ogician
- **O**ptimizer
- **P**assionate
- **E**xplorer
- **R**esourceful

Feel free to reach out for collaborations or suggestions!

---

## 🤝 Contribution Guidelines

We welcome contributions to enhance this project! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes and push them to the branch.
4. Create a pull request describing your changes.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For any queries or feedback, feel free to reach out:
- **Email:** your-email@example.com
- **GitHub:** [@your-username](https://github.com/your-username)

---

### ⭐ If you like this project, consider giving it a star! ⭐

