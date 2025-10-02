# Evaluación Modular Módulo 10 - Breast Cancer Prediction API

## Descripción
Este proyecto implementa una **API REST** para la predicción de cáncer de mama utilizando un modelo entrenado con datos de tumores malignos y benignos. La API permite:

- Testar endpoints básicos (`GET /` y `POST /predict`).
- Realizar predicciones enviando características del tumor en formato JSON.

Además, el proyecto tiene **integración continua y despliegue continuo (CI/CD)** configurada con **GitHub Actions** y **Docker**, incluyendo pruebas automáticas de los endpoints y despliegue a Docker Hub.

---

## Flujo de CI/CD

1. **Push a GitHub**  
   Cada vez que se hace un push a `main` se dispara el workflow.

2. **Construcción y prueba de Docker**  
   - Construye la imagen Docker: `breast-cancer-api`
   - Levanta un contenedor temporal
   - Testea endpoints:
     - `GET /` devuelve un mensaje de disponibilidad
     - `POST /predict` devuelve predicción y probabilidades
   - Detiene el contenedor

3. **Publicación en Docker Hub**  
   - Inicia sesión usando secretos `DOCKER_USERNAME` y `DOCKER_PASSWORD`
   - Hace push de la imagen `latest` y con el tag del commit

---

## Ejemplo de uso

**Ejecutar contenedor localmente:**
```bash
docker run -d -p 5000:5000 --name breast-api barcklan/breast-cancer-api:latest
```
## Test GET /:
```bash
curl http://localhost:5000/
```

## Test POST /predict:
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features":[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]}'
```

Respuesta esperada:
```bash
{
  "prediction": 1,
  "probabilities": [6.05e-09, 0.99999999]
}
```

Donde `prediction = 1` indica `maligno` y `0` `benigno`.

## Requisitos

`Python 3.11+`

`Flask`

`Docker`

`Acceso a Docker Hub (para CI/CD)`

## Evidencias

En la carpeta `img/` se encuentran capturas de la ejecución de Git, Docker y GitHub Actions, demostrando que el CI/CD funciona correctamente.

## Autor

`Claudio Díaz Vargas`


---







