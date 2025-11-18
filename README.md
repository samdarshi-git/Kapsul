# Kapsul-PlatformIo  
Firmware for the **Kapsul Real-Time Smart Medicine Dispenser**

## 🚀 Overview  
Kapsul-PlatformIo powers the hardware side of the **Kapsul Smart Medicine Dispenser** — a fully automated, real-time medicine dispensing system designed to help users take the correct medicine at the correct time **without manual interference**.

The ESP32 firmware controls all hardware components, communicates with the cloud dashboard, manages schedules, drives servos, senses user interactions, and provides visual feedback.

---

## 🧩 Hardware Components  
- **ESP32** – Main controller  
- **MG995 Servo** – High-torque mechanism for primary medicine movement  
- **SG90 Servos** – Micro adjustments + sub-modules  
- **Touch Sensors** – User confirmation, safety checks  
- **RGB LEDs** – Visual feedback for status, timing, cabinet cue  
- Optional: Basic wiring, power modules, stabilizers  

---

## ✨ Key Features  
- Automatic real-time medicine dispensing  
- Servo-based movement with MG995 + SG90  
- Capacitive touch input for user confirmation  
- RGB visual cues for guidance and feedback  
- WebSocket communication with the dashboard  
- Offline-first logic with local fallback  
- Simple, reliable, low-maintenance structure  

---

## 🧠 What This Firmware Does  
- Reads schedules from the portal  
- Controls servo positions to release the required medicine  
- Uses touch sensors to confirm interaction  
- Shows status using RGB lights  
- Syncs logs, status, and events to the portal in real time  
- Runs a timed “medicine engine” for morning/noon/evening/night routines  

---

## 🛠 Built With  
- **C++** (PlatformIO)  
- **ESP32 frameworks**  
- **WebSocket client**  
- **VS Code + PlatformIO**  

---

## 📡 Connectivity  
- Works offline with local logic  
- Syncs online using WebSockets  
- Portal triggers → device executes in real time  

---

## 🧪 Testing  
- Servo movement ranges  
- Touch sensor sensitivity  
- RGB animations  
- Online + offline fallback modes  

---

## 📝 Credits  
Help used: **ChatGPT**, YouTube, official hardware documentation.  

---

## 🧾 License  
MIT License  
