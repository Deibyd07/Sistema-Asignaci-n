# Definition of Done (DoD)
**Sistema de Asignacion de Salones - Universidad del Valle, Seccional Zarzal**

Version: 1.0  
Fecha: 12 de abril de 2026  
Estado: Aprobado para uso del equipo Scrum

---

## 1. Proposito
La Definition of Done (DoD) define formalmente cuando una tarea, historia de usuario o incremento de sprint puede considerarse terminado.  
Un item solo se marca como Done si cumple todos los criterios aplicables de esta lista.

---

## 2. Alcance de aplicacion
Esta DoD aplica a:
- Tareas tecnicas (issues TEC)
- Historias de usuario (HU)
- Incrementos de sprint
- Entrega final del MVP

---

## 3. DoD por nivel

### A. Nivel Tarea (Task / Issue Tecnica)
Para marcar una tarea como Done, debe cumplir:

- [ ] Implementacion completa segun criterio tecnico definido (issue, HU o sub-tarea de sprint).
- [ ] Codigo en backend y/o frontend funcionando localmente sin errores bloqueantes.
- [ ] Estilo y convenciones del proyecto respetadas (Python: PEP8, frontend: lint/formato del equipo).
- [ ] Codigo revisado por al menos una persona del equipo (peer review).
- [ ] Sin credenciales ni secretos expuestos en codigo o commits.
- [ ] Pruebas unitarias o tecnicas minimas ejecutadas y en verde para el cambio realizado.
- [ ] Documentacion tecnica breve actualizada si el cambio afecta arquitectura, endpoint, modelo o flujo.
- [ ] Estado actualizado en GitHub Issues/Projects (enlace, responsable, estado Done).

### B. Nivel Historia de Usuario (HU)
Para marcar una HU como Done, debe cumplir:

- [ ] Todos los criterios de aceptacion (Conversation/Confirmation) verificados.
- [ ] Flujo end-to-end funcional (frontend + backend + datos).
- [ ] Validaciones funcionales y de negocio implementadas (ejemplo: rol, capacidad, conflictos, estados).
- [ ] Pruebas de integracion del flujo principal ejecutadas sin errores criticos.
- [ ] Evidencia de funcionamiento disponible (capturas, video corto o registro de prueba).
- [ ] Aprobacion funcional del Product Owner en Sprint Review.

### C. Nivel Sprint
Para considerar un sprint como Done, debe cumplir:

- [ ] Historias comprometidas finalizadas o desvio comunicado y aceptado por Product Owner.
- [ ] Build e integracion continua en estado exitoso (lint, test, build) en rama principal.
- [ ] Incremento desplegado y accesible en entorno definido (staging o produccion academica).
- [ ] Sprint Review realizada con demostracion funcional.
- [ ] Retrospectiva realizada y al menos una accion de mejora definida.
- [ ] Backlog y tablero actualizados con trazabilidad de decisiones.

### D. Nivel Entrega Final (MVP)
Para considerar la entrega final como Done, debe cumplir:

- [ ] Modulos MVP operativos: acceso, configuracion, maestros, programacion, ejecucion algoritmo, visualizacion y publicacion.
- [ ] Pruebas de aceptacion con usuarios reales ejecutadas y documentadas.
- [ ] Tasa de resolucion de conflictos de asignacion >= 90% con datos reales de la seccional.
- [ ] Cobertura objetivo alcanzada para servicios criticos del backend (>= 95%, segun definicion del proyecto).
- [ ] Cero errores criticos abiertos al cierre de entrega.
- [ ] Documentacion minima completa: instalacion, arquitectura, alcance/MVP y trazabilidad funcional.
- [ ] Repositorio entregado con historial y pipeline de CI/CD activo.

---

## 4. Criterios de bloqueo (No Done)
Un item no puede cerrarse como Done si ocurre cualquiera de estos casos:
- Tiene criterios de aceptacion pendientes.
- Rompe funcionalidad existente o introduce regresiones criticas.
- Tiene fallos en pruebas clave o pipeline en rojo.
- No fue revisado o no tiene evidencia de prueba.
- Carece de trazabilidad en tablero/issue.

---

## 5. Responsables de validacion
- Equipo de Desarrollo: valida cumplimiento tecnico.
- Scrum Master: valida proceso y ceremonias.
- Product Owner: valida cumplimiento funcional y aprueba cierre de HU/incremento.

---

## 6. Regla de uso
Si hay duda sobre cerrar un item, se aplica esta regla:

**Si no cumple todos los checks aplicables, no esta Done.**

---

## 7. Revision de la DoD
Esta DoD es un artefacto vivo y puede ajustarse en retrospectiva por acuerdo entre Product Owner, Scrum Master y Equipo de Desarrollo.
Frecuencia recomendada de revision: al cierre de cada sprint.
