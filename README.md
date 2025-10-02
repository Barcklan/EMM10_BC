# EMM10_BC - Breast Cancer Prediction API

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
