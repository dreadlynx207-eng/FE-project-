from flask import Flask, request, jsonify
import cv2
import numpy as np

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

# product database
products = {
    "9418504885103": {"name": "Milk", "price": 50},
    "6009186141426": {"name": "Bread", "price": 30}
}

cart = {}

@app.route('/upload', methods=['POST'])
def upload():
    file_bytes = np.frombuffer(request.data, np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    print("Image received")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector = cv2.barcode.BarcodeDetector()
    decoded_info, decoded_type, points = detector.detectAndDecode(gray)

    if decoded_info:
        code = decoded_info[0]
        print("Detected:", code)

        if code in products:
            if code in cart:
                cart[code]["qty"] += 1
            else:
                cart[code] = {
                    "name": products[code]["name"],
                    "price": products[code]["price"],
                    "qty": 1
                }

            return jsonify({"status": "added", "code": code})

    return jsonify({"status": "not found"})

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

print("Starting server...")
app.run(host='0.0.0.0', port=5000)
@app.route('/clear', methods=['POST'])
def clear():
    cart.clear()
    return {"status": "cleared"}

@app.route('/bill', methods=['GET'])
def generate_bill():
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet

    file_path = "bill.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("🛒 Smart Cart Bill", styles['Title']))
    elements.append(Spacer(1, 10))

    total = 0

    for code, item in cart.items():
        line = f"{item['name']} - ₹{item['price']} x {item['qty']}"
        elements.append(Paragraph(line, styles['Normal']))

        total += item['price'] * item['qty']

    elements.append(Spacer(1, 10))
    elements.append(Paragraph(f"Total: ₹{total}", styles['Heading2']))

    doc.build(elements)

    from flask import send_file
    return send_file(file_path, as_attachment=True)    