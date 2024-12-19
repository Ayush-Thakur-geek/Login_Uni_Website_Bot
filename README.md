# **CuimsBot: Automated UIMS Login for CU (Chandigarh University)**

## **Overview**
CuimsBot is an automation script designed to streamline the login process for the University Information Management System (UIMS) of Chandigarh University (CU). This bot automates the login steps, including capturing and solving CAPTCHA challenges, to provide a seamless and faster login experience.

The script uses Selenium WebDriver to automate browser interactions, along with Python libraries like `Pillow` (PIL) for image processing and `pytesseract` for Optical Character Recognition (OCR) to solve CAPTCHAs.

---

## **Features**
- **Automatic Login:** Logs into UIMS with a student ID and password.
- **CAPTCHA Handling:** Solves CAPTCHA using OCR to bypass manual intervention.
- **Cross-Browser Compatibility:** Currently using ChromeDriver, but can be extended to other browsers.
- **Image Processing:** Captures CAPTCHA image, processes it with OCR, and enters the CAPTCHA value.
  
---

## **Requirements**
- **Python 3.x** (Preferably Python 3.8+)
- **Selenium**: For web automation.
- **Pillow (PIL)**: For image processing (used to open and manipulate CAPTCHA images).
- **pytesseract**: Python binding for Google's Tesseract OCR, used to solve CAPTCHA.
- **ChromeDriver**: Ensure that the `chromedriver` version is compatible with your installed version of Google Chrome.
  
You can install the necessary dependencies by running the following command:

```bash
pip install selenium Pillow pytesseract
```
Additionally, you need to install Tesseract on your machine. You can download it from the official repository: [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract).

---

## **Setup**

### **1. Clone this repository:**

```bash
git clone https://github.com/Ayush-Thakur-geek/Login_To_Uni_Website_Bot.git
```

### **2. Setup Tesseract:**
Ensure that Tesseract is properly installed on your system. If you're on a Linux system, you can install it using:
```bash
sudo apt install tesseract-ocr
```

### **3. Add your credentials:**
Create a file named essentials.py to store your UID and Password securely.
```bash
# essentials.py
uid = "your_student_id"
pwd = "your_password"
```

### **4. Run the Bot:**
Execute the script to perform the automated login:

```bash
python -i cuims_bot.py
```
**Note**: Make sure to run it in interactive mode

---

## **How It Works**

1. **Navigate to the UIMS Website:**  
   The bot opens the UIMS login page and clicks on the student login button.

2. **Switch to Login Window:**  
   It switches to the new window (after clicking "Login").

3. **Fill in Student ID and Password:**  
   It automatically inputs the student ID and password stored in the `essentials.py` file.

4. **Solve CAPTCHA:**  
   The bot takes a screenshot of the CAPTCHA, processes it with Tesseract to extract the text, and enters it into the CAPTCHA input field.

5. **Login:**  
   Finally, it clicks the "Login" button to complete the login process.

---

## **Troubleshooting**

- **Captcha Image Not Clear:**  
   Sometimes Tesseract may not be able to accurately solve the CAPTCHA if the image quality is low. You can try adjusting the image quality using Pillow methods like resizing or enhancing the contrast.

- **ChromeDriver Compatibility Issues:**  
   Ensure the version of ChromeDriver installed matches the version of Google Chrome you have.

- **Missing Dependencies:**  
   If you face issues with missing libraries, ensure you have all the required dependencies installed via `pip`.

---

## **Future Improvements**

- **Browser Profile Management:**  
   Automating browser sessions with saved credentials and session management for a faster login experience.

- **Error Handling:**  
   Improve error handling and retries in case of failed CAPTCHA recognition or login.

- **GUI Version:**  
   A graphical interface where students can enter their credentials and interact with the bot without modifying code.

---

## **License**

This project is open-source and available under the MIT License.

---

## **Contributors**

- Ayush Thakur

Feel free to fork, contribute, or make modifications to the project!


