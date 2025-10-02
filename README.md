# EMM10_BC - Breast Cancer Prediction API

## Descripción
Este proyecto implementa una **API REST** para la predicción de cáncer de mama utilizando un modelo entrenado con datos de tumores malignos y benignos. La API permite:

- Testar endpoints básicos (`GET /` y `POST /predict`).
- Realizar predicciones enviando características del tumor en formato JSON.

Además, el proyecto tiene **integración continua y despliegue continuo (CI/CD)** configurada con **GitHub Actions** y **Docker**, incluyendo pruebas automáticas de los endpoints y despliegue a Docker Hub.

---

## Estructura del proyecto
EMM10_BC/
├── .github/
│ └── workflows/ci-cd.yml # Flujo de CI/CD
├── img/ # Capturas de evidencia
├── app.py # API Flask
├── breast_cancer_model.pkl # Modelo entrenado
├── Dockerfile # Construcción de imagen Docker
├── requirements.txt # Dependencias Python
└── README.md # Este archivo
