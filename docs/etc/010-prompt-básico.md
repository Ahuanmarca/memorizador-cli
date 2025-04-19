Generar una aplicación CLI para entrenar para un examen con preguntas de opción múltiple.

Las preguntas estarán guardadas en un archivo json con la siguiente estructura:

```json
[
  {
    "id": 1,
    "libro": "Constitución Española",
    "capitulo": "Capítulo II - Derechos y libertades",
    "tema": "Tema 3 - Derechos fundamentales",
    "pagina": 42,
    "pregunta": "¿Cuál de los siguientes derechos está reconocido en el artículo 15 de la Constitución Española?",
    "respuesta_correcta": "El derecho a la vida y a la integridad física y moral",
    "respuestas_incorrectas": [
      "El derecho a la propiedad privada y a la herencia",
      "El derecho a fundar sindicatos",
      "El derecho a la libertad de empresa"
    ],
    "fragmento_original": "Artículo 15\nTodos tienen derecho a la vida y a la integridad física y moral, sin que, en ningún caso, puedan ser sometidos a tortura ni a penas o tratos inhumanos o degradantes.",
    "aciertos_consecutivos": 0,
    "fallos_totales": 0,
    "veces_vista": 0,
    "ultima_vez_vista": null,
    "ultima_vez_acertada": null,
    "descartada": false,
    "nivel_dificultad": "media",
    "etiquetas": ["constitución", "derechos", "artículo 15"],
    "proxima_revision": null,
    "notas_personales": ""
  },
  {
    "id": 2,
    "libro": "Constitución Española",
    "capitulo": "Capítulo III - Organización territorial del Estado",
    "tema": "Tema 2 - Organización territorial del Estado",
    "pagina": 35,
    "pregunta": "¿Cuál de los siguientes entes no forma parte de la organización territorial del Estado según la Constitución?",
    "respuesta_correcta": "Las regiones administrativas",
    "respuestas_incorrectas": [
      "Los municipios",
      "Las provincias",
      "Las comunidades autónomas"
    ],
    "fragmento_original": "Artículo 137\nEl Estado se organiza territorialmente en municipios, en provincias y en las Comunidades Autónomas que se constituyan.",
    "aciertos_consecutivos": 1,
    "fallos_totales": 2,
    "veces_vista": 3,
    "ultima_vez_vista": "2025-04-18T19:30:00",
    "ultima_vez_acertada": "2025-04-18T19:30:00",
    "descartada": false,
    "nivel_dificultad": "alta",
    "etiquetas": ["constitución", "territorio", "artículo 137"],
    "proxima_revision": "2025-04-21T19:30:00",
    "notas_personales": "Me confundo con 'regiones administrativas' porque suena real, revisar más adelante."
  }
]
```
