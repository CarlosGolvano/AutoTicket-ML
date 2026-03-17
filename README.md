# Sistema de clasificación automatíca de tickets

> [!WARNING]  
> Este proyecto tiene como propósito poner en práctica el conocimiento aprendido de backend.

Aplicación para automatizar el enriquecimiento de tickets de soporte técnico. Cuando un cliente envía un ticket, el sistema lo analiza automáticamente en segundo plano determinando su categoría, el sentimiento del cliente y su urgencia. Con esos datos calcula una prioridad final que ayuda a los agentes a gestionar su cola de trabajo de forma más eficiente.

Este repositorio constituye el sistema de etiquetado de los tickets mediante modelos de lenguaje. La aplicación de entrada se está ubicada en [Autoticket-app](https://github.com/CarlosGolvano/AutoTicket-app).

## Stack tecnológico

| Capa | Tecnología           |
|---|----------------------|
| Backend principal | Java + Spring Boot   |
| Mensajería | Apache Kafka         |
| Servicio ML | Python (Huggingface) |
| Base de datos | PostgreSQL           |
| Autenticación | Spring Security      |
