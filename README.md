# Smart Shopping Cart System

A robust, demo‑ready smart shopping cart project integrating **ESP32‑CAM QR decoding** with a **PHP/MySQL backend**, real‑time dashboard, and **WhatsApp Cloud API** for receipt delivery.

---

## 📌 Features
- **ESP32‑CAM QR Scanner**  
  Decodes product QR codes and sends data to backend via HTTP requests.

- **PHP/MySQL Backend**  
  - Modular files (`db_connection.php`, `cart_logic.php`, `receipt_generator.php`)  
  - Secure database connection and cart table management  
  - PDF receipt generation

- **Dashboard & Visualization**  
  - Itemized cart view  
  - Spending analytics with **Chart.js**  
  - Professional CSS styling

- **WhatsApp Cloud API Integration**  
  - Automatic receipt delivery in PDF format  
  - Sandbox/testing support with Facebook Developer credentials

---

## 🛠️ Tech Stack
- **Hardware:** ESP32‑CAM module  
- **Firmware:** Arduino IDE (C++ sketch for QR decoding + webhook integration)  
- **Backend:** PHP 8, MySQL (Laragon/XAMPP/WampServer)  
- **Frontend:** HTML, CSS, Chart.js  
- **API:** WhatsApp Cloud API (Meta Developer Platform)

---

## ⚙️ Setup Instructions

### 1. Hardware
- Flash ESP32‑CAM with provided Arduino sketch.
- Connect to Wi‑Fi and configure webhook endpoint.

### 2. Backend
- Install **Laragon** or **XAMPP**.  
- Create database `shopping_cart`.  
- Import `cart.sql` to set up tables.  
- Place PHP files in `/www` or `/htdocs`.

### 3. Dashboard
- Access `index.php` in browser.  
- Scan QR codes → items appear in cart.  
- View analytics on dashboard.

### 4. WhatsApp API
- Set up **Meta Developer App**.  
- Configure Phone Number ID & Access Token.  
- Update `receipt_generator.php` with credentials.  
- Test sending receipts via sandbox.

---

---

## 🚀 Demo Workflow
1. Customer scans product QR code with ESP32‑CAM.  
2. Product details sent to backend → added to cart.  
3. Dashboard updates with cart + analytics.  
4. On checkout, PDF receipt generated.  
5. Receipt automatically sent via WhatsApp.

---

## 📄 Documentation
- Step‑by‑step setup guide included in project report.  
- Troubleshooting logs available in `/logs`.  
 

---

## ✅ Current Status
- Hardware integration tested and stable.  
- Backend fully functional with Laragon.  
- Dashboard + receipt generation implemented.  
- WhatsApp API integration in progress (requires valid credentials).

---

## 📌 Next Steps
- Deploy backend to cloud server for remote access.  
- Expand QR database with product categories.  
- Optimize ESP32 firmware for faster decoding.  
- Add user authentication for secure checkout.


## 📂 Project Structure
