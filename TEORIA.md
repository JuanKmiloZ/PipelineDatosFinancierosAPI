# Parte 1 — Teórica

1.1.  Arquitectura y Principios de Diseño

a) Hace poco realicé un proyecto MVP llamado "USistemadePagos" el cual incluye
   simulando ERP, BASE DEDATOS, PYTHON, POWER AUTOMATE, TEAMS, OUTLOOK, POWER BI.

   En el se realiza el supuesto de estar conectados a dos fuentes, sin modificar la logica del negocio

   class PagosBD(ProveedorPagos):
    def obtener_pagos(self):
        # consultar base de datos
        pass


class PagosAPI(ProveedorPagos):
    def obtener_pagos(self):
        # consumir API REST
        pass



b) Evita sobrecostos futuros(costo de oportunidad)  


1.2 Fundamentos de IA & NLP

      R//.  a) Discriminativo vs Generativo

Discriminativo: clasifica . Ej: dice si una factura cumple con una norma.
Generativo: crea . Ej: redacta una carta.

 R//. b) Embedding
componente indispensable del RAG

 R//. c) Fine-tuning vs RAG vs Prompting

Prompting es primero,solo instrucciones claras cada vez, la evolución es el RAG, el modelo busca en tus documentos antes de responder; y el caso optimo es Fine-tuning, Reentrenar el modelo. 
