# Formato de preguntas en json que debe generar GPT

```json
{
  "libro": "Condiciones Generales",
  "capitulo": "Título Preliminar",
  "formulaciones": [
    {
      "texto": "¿Cuál de las siguientes actividades forma parte del objeto social de Renfe Viajeros?",
      "modo": "una_correcta",
      "tipo": "positiva"
    },
    {
      "texto": "¿Qué actividad NO forma parte del objeto social de Renfe Viajeros?",
      "modo": "una_correcta",
      "tipo": "negativa"
    },
    {
      "texto": "¿Cuál de las siguientes actividades forma parte del objeto social de Renfe Viajeros?",
      "modo": "todas_correctas",
      "tipo": "positiva"
    }
  ],
  "respuestas_correctas": [
    "La prestación de servicios de transporte de viajeros por ferrocarril nacional e internacional",
    "La mediación en la prestación de servicios turísticos",
    "La organización y comercialización de productos turísticos o viajes combinados",
    "La prestación de servicios o actividades complementarias vinculadas al transporte ferroviario"
  ],
  "respuestas_incorrectas": [
    "La gestión directa de hoteles en destinos turísticos",
    "El control aduanero en estaciones internacionales",
    "La certificación técnica de infraestructuras ferroviarias",
    "La regulación del tráfico ferroviario en coordinación con AENA",
    "La formación de maquinistas ferroviarios comerciales"
  ],
  "fragmento_original": "RENFE VIAJEROS SOCIEDAD MERCANTIL ESTATAL, S.A. (en adelante Renfe Viajeros) tiene por objeto social la prestación de servicios de transporte de viajeros por ferrocarril, tanto nacional como internacional, la mediación en la prestación de cualesquiera servicios turísticos, organización, oferta y/o comercialización de viajes combinados o productos turísticos, así como la prestación de otros servicios o actividades complementarias o vinculadas al transporte ferroviario.",
  "etiquetas": ["objeto social"]
}
```

# Formato de preguntas luego de concatenarlas

```json

```
