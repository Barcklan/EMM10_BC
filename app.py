from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
import traceback

# Inicializar Flask
app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Cargar modelo
try:
    model = joblib.load("breast_cancer_model.pkl")
    logging.info("Modelo cargado correctamente ✅")
except Exception as e:
    logging.error(f"Error cargando el modelo: {e}")
    raise e

# GET / → estado del servicio
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "API funcionando correctamente ✅"
    })

# POST /predict → predicción
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validación de JSON
        if not data or "features" not in data:
            return jsonify({"error": "Debes enviar un JSON con la clave 'features'"}), 400

        features = data["features"]

        # Validar número de features
        if len(features) != 30:
            return jsonify({"error": f"Se esperaban 30 features, se recibieron {len(features)}"}), 400

        # Convertir a numpy array
        features_array = np.array(features).reshape(1, -1)

        # Hacer predicción
        prediction = model.predict(features_array)[0]
        probabilities = model.predict_proba(features_array)[0].tolist()

        return jsonify({
            "prediction": int(prediction),
            "probabilities": probabilities
        })

    except Exception as e:
        logging.error(traceback.format_exc())
        return jsonify({"error": "Ocurrió un error al procesar la predicción", "details": str(e)}), 500

# Ejecutar la app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
