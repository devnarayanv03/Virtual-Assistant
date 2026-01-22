# J.A.R.V.I.S (Just A Rather Very Intelligent System)

A powerful Python-based AI assistant designed to automate tasks, provide information, and control your system through voice commands. Inspired by Iron Man's legendary assistant.

## 🚀 Features

*   **Voice Interaction**: Seamless Speech-to-Text (STT) and Text-to-Speech (TTS) capabilities.
*   **AI Brain**: Powered by `webscout` (PhindSearch) for intelligent conversations and query resolution.
*   **Automation**:
    *   Open applications and web tabs.
    *   Control system volume and media playback.
    *   Scroll through pages and content.
    *   Check battery status and plug connection.
*   **Productivity Tools**:
    *   Set alarms and reminders.
    *   Create files and manage data.
    *   Check internet speed and connectivity status.
    *   Get weather updates.
*   **Vision**: Basic computer vision capabilities (via `opencv-python`).
*   **System Integration**: Windows notifications and system monitoring.

## 🛠️ Tech Stack

*   **Language**: Python 3.x
*   **Core Libraries**:
    *   `selenium`: For web-based STT interface.
    *   `webscout`: For AI processing.
    *   `playsound` & `requests`: For TTS generation (StreamElements API).
    *   `PyAutoGUI` & `automation`: For system control.
    *   `opencv-python`: For vision tasks.
    *   `winotify`: For Windows notifications.

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

1.  **Python 3.10+**
2.  **Google Chrome** (for Selenium-based features)
3.  **ChromeDriver**:
    *   Download the ChromeDriver version matching your Chrome browser.
    *   Place `chromedriver.exe` in the project root directory.

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/J.A.R.V.I.S.git
    cd J.A.R.V.I.S
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🎮 Usage

1.  Run the main script:
    ```bash
    python jarvis.py
    ```
2.  The system will initialize, check for internet connectivity, and start the listening interface.
3.  **Voice Commands**: Speak naturally to J.A.R.V.I.S.
    *   *"Tell me the time"*
    *   *"Set an alarm for 7 AM"*
    *   *"Check internet speed"*
    *   *"Open YouTube"*
    *   *"Play music"*

## 📂 Project Structure

*   `jarvis.py`: Main entry point of the application.
*   `Brain/`: Contains the AI logic and core processing units.
*   `Automation/`: Scripts for controlling system functions (apps, music, scrolling).
*   `Features/`: specific utilities like internet speed test, weather, file creation.
*   `STT/` & `TTS/`: Speech recognition and synthesis modules.
*   `UI/`: User interface assets and scripts.
*   `Data/`: Data storage for dialogs and logs.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
