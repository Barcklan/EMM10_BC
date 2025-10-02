# Proyecto: API de Predicción de Cáncer de Mama

## **Descripción**

Este proyecto desarrolla un modelo de clasificación para predecir cáncer de mama utilizando **regresión logística** sobre el conjunto de datos de cáncer de mama en relación a tumores malignos y benignos.  
El modelo se despliega como una **API usando Flask**, se empaqueta con **Docker**, y se integra con **GitHub Actions** para **CI/CD** y push automático a **Docker Hub**.

---

## **Flujo del Proyecto**

1. **Entrenamiento del modelo**
   - Se entrena un modelo de **regresión logística** usando los datos de características tumorales.
   - El modelo entrenado se guarda en `breast_cancer_model.pkl`.

2. **Despliegue local con Flask**
   - API Flask en `app.py` con endpoints:
     - `GET /` → prueba que la API está corriendo.
     - `POST /predict` → recibe un JSON con las características y devuelve la predicción.
   - Ejecutar localmente:
     ```bash
     python app.py
     ```
     y acceder a `http://localhost:5000`.

3. **Empaquetado y prueba con Docker**
   - Construir imagen Docker:
     ```bash
     docker build -t breast-cancer-api .
     ```
   - Levantar contenedor de prueba:
     ```bash
     docker run -d -p 5000:5000 --name test-api breast-cancer-api
     ```
   - Consultas de prueba usando `curl` o Postman.

4. **Integración continua y despliegue con GitHub Actions**
   - Flujo configurado en `.github/workflows/ci-cd.yml`:
     - Ejecuta ante **push** o **pull request** a la rama `main`.
     - Construye la imagen Docker.
     - Levanta contenedor temporal y realiza tests de los endpoints (`GET /` y `POST /predict`).
     - Detiene contenedor.
     - Hace login en Docker Hub usando secretos.
     - Taggea y sube imagen a Docker Hub (`latest` y commit hash).

---

## **Estructura del repositorio**

```bash
EMM10_BC/

├─ .github/workflows/ci-cd.yml   # Flujo CI/CD

├─ app.py                        # API Flask

├─ breast_cancer_model.pkl       # Modelo entrenado

├─ Dockerfile                    # Instrucciones para construir la imagen Docker

├─ requirements.txt              # Librerías necesarias

├─ .gitignore                    # Archivos y carpetas ignoradas por Git

├─ img/                          # Capturas de evidencia

└─ README.md                     # Documentación
```

---

## Ejemplo de Predicción

**Request POST /predict:**
```json
{
  "features": [14.2, 10.1, 92.3, 600, 0.1, 0.2, 0.3, 0.15, 0.2, 0.06,
               0.9, 0.85, 7.2, 120, 0.005, 0.04, 0.05, 0.015, 0.03, 0.006,
               20.0, 15.0, 130, 1700, 0.14, 0.55, 0.65, 0.2, 0.4, 0.11]
}
```

## **Respuesta Esperada**
```json
{
  "prediction": 1,
  "probabilities": [0.01, 0.99]
}
```
Donde `prediction = 1` indica `maligno` y `0` `benigno`.

## **Evidencia**

* Docker instalado y funcionando.

* API Flask probada localmente.

* Entrenamiento del modelo y métricas de precisión.

* Flujo CI/CD ejecutado exitosamente.

* Archivos ignorados y eliminados correctamente en GitHub.

* (Las capturas se encuentran en la carpeta img/)

# Conclusión

Este proyecto demuestra cómo pasar de un modelo de machine learning a un servicio desplegable en producción, incluyendo pruebas automáticas, CI/CD y publicación en Docker Hub.

## Requisitos

* `Python 3.11+`

* `Flask`

* `scikit-learn`

* `Docker`

* `Acceso a Docker Hub (para CI/CD)`


## Autor

`Claudio Díaz Vargas`


---







