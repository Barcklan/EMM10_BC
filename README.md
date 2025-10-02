# Proyecto: API de Predicción de Cáncer de Mama

# Introducción

Este proyecto implementa un modelo de predicción de cáncer de mama utilizando Regresión Logística entrenado con el dataset de Wisconsin. El modelo se despliega como una API REST con Flask, y está empaquetado en Docker para facilitar su escalabilidad y portabilidad. Además, se automatiza el flujo de CI/CD con GitHub Actions, asegurando pruebas automáticas y despliegue confiable de la imagen Docker a Docker Hub.

## **Descripción**

Este proyecto implementa un modelo de clasificación de cáncer de mama usando regresión logística sobre datos de tumores malignos y benignos, diseñado para integrarse en la infraestructura tecnológica de la startup de salud, cumpliendo con los requerimientos de:

* **Escalable localmente mediante contenedores**

* **Fácil de actualizar**

* **Accesible vía REST**

* **Documentado y probado con CI/CD**

Además, el modelo se despliega como una **API usando Flask**, se empaqueta con **Docker**, y se integra con **GitHub Actions** para **CI/CD** y push automático a **Docker Hub**.

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
   - Consultas de prueba usando `curl`, `Postman` o con jupyter notebook importando la librería `requests`.

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

## Ejemplo de Predicción con `features` como parámetros

Las features son las variables de entrada que el modelo usa para hacer predicciones. Cada feature representa un atributo medido o calculado sobre cada muestra (paciente o tumor, en este caso).

Una muestra pequeña de las variables del dataset de cáncer de mama de Wisconsin, incluyen medidas extraídas de imágenes de tumores:

* `radius_mean`: radio promedio del tumor

* `texture_mean`: textura promedio

* `perimeter_mean`: perímetro promedio

* `area_mean`: área promedio

* `smoothness_mean`: suavidad promedio

* `compactness_mean`: compacidad promedio

* `concavity_mean`: concavidad promedio

* `concave points_mean`: puntos cóncavos promedio

* `symmetry_mean`: simetría promedio

* `fractal_dimension_mean`: dimensión fractal promedio

Y hay más features que incluyen medidas de error estándar y valores “worst” (peores) de esas mismas métricas.

Cada valor corresponde a una de esas variables en el mismo orden que fueron usadas para entrenar el modelo.

El modelo toma todos estos valores y calcula:

`prediction: 0 = benigno, 1 = maligno`

`probabilities`: probabilidad de cada clase según el modelo

En resumen, las features son los “inputs” medibles que definen la muestra y que el modelo necesita para hacer su predicción.

**Request POST /predict:**
```json
{
  "features":[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,
                0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,
                0.04904,0.05373,0.01587,0.03003,0.006193,
                25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,
                0.2654,0.4601,0.1189]
}
```

## **Respuesta Esperada**
```json
{
  "prediction": 1,
  "probabilities": [6.0584655070528015e-09, 0.9999999939415345]
}
```
Donde `prediction = 1` indica `maligno` y `0` `benigno`.
### *Interpretación del manejo de resultado arrojado por el modelo:*

De acuerdo a lo visto en el resultado arrojado en el ejemplo anterior, el modelo nos predice que, con las características o parámetros establecidos por el cliente o el usuario interesado, el paciente tendría un tumor maligno (1) con una probabilidad del 100% (~0.999) de seguridad. Esto nos indica que el resultado no es ambigüo, sino que la clasificación es fuerte y clara hacia una condición maligna (100%).

## **Evidencia**

* Docker instalado y funcionando.

* API Flask probada localmente.

* Entrenamiento del modelo y métricas de precisión.

* Flujo CI/CD ejecutado exitosamente.

* Archivos ignorados y eliminados correctamente en GitHub.

* (Las capturas se encuentran en la carpeta img/)

# Conclusión

Este proyecto entrega un **modelo de predicción de cáncer de mama funcional** y listo para integrarse en la infraestructura tecnológica de startups de salud.  

Gracias al despliegue mediante **API REST con Flask** y la **contenedorización con Docker**, el servicio ofrece:

- **Escalabilidad local**: se puede replicar fácilmente en múltiples contenedores para soportar más tráfico o distintas instancias del servicio.
  
- **Facilidad de actualización**: nuevas versiones del modelo o cambios en la API pueden implementarse sin interrumpir el servicio, aprovechando CI/CD.

- **Acceso vía REST**: permite integración directa con otras aplicaciones, portales de pacientes o sistemas internos de salud.

- **Documentación y pruebas automatizadas**: con GitHub Actions, se asegura que cada cambio sea testeado y que la API funcione correctamente antes de actualizar Docker Hub.  

En resumen, este proyecto demuestra cómo un **modelo de machine learning** puede transformarse en un **servicio confiable, escalable y listo para producción**, cumpliendo con los estándares que requiere una startup de salud para integrar capacidades de predicción dentro de su ecosistema tecnológico.

## Requisitos

* `Python 3.11+`

* `Flask`

* `scikit-learn`

* `Docker`

* `Acceso a Docker Hub (para CI/CD)`


## Autor

`Claudio Díaz Vargas`


---







