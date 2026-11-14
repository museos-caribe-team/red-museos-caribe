
# Análisis de requisitos 1 al 5

## Requisito 1. Crear un museo

**Entradas:** nombre del museo, aforo diario, año, mes y día de inicio.

**Salidas:** museo creado sin días registrados, o mensaje de error y regreso al menú.

**Reglas y validaciones:**
1. El nombre no puede estar vacío ni repetido.
2. El aforo debe ser un número entero.
3. El aforo debe ser de al menos un visitante.
4. Año, mes y día deben ser enteros y formar una fecha válida.
5. Las condiciones se revisan en ese orden y se informa solamente el primer error.

**Prueba propuesta:** crear el Museo del Café con aforo 150 y fecha 2026-11-01; verificar que no tenga días registrados. Probar también aforo 0 y fecha 2026-11-31.

## Requisito 2. Registrar los visitantes del día siguiente

**Entradas:** nombre de un museo y número de visitantes.

**Salidas:** fecha del siguiente día y registro actualizado, o mensaje de error.

**Reglas y validaciones:**
- El museo debe existir.
- La fecha siguiente es la fecha de inicio más la cantidad de días registrados.
- Los visitantes deben ser un entero entre 0 y el aforo diario, ambos incluidos.
- Ante una cantidad inválida, se vuelve a solicitar el dato para el mismo día.

**Prueba propuesta:** en un museo con aforo 150, ingresar 151 y luego 60; verificar que solo se registre 60.

## Requisito 3. Simular días

**Entradas:** nombre del museo, cantidad de días, visitantes mínimos y máximos.

**Salidas:** nuevos días con cantidades aleatorias de visitantes o mensaje de error.

**Reglas y validaciones:**
- El museo debe existir.
- La cantidad de días debe ser un entero mayor o igual a 1.
- Mínimo y máximo deben ser enteros entre 0 y el aforo diario.
- El mínimo no puede superar al máximo.
- Cada valor se valida al leerlo; ante un error se vuelve al menú sin agregar días.
- Los extremos mínimo y máximo están incluidos en la generación aleatoria.

**Prueba propuesta:** simular tres días con mínimo 75 y máximo 150; verificar las fechas y cantidades. Probar también mínimo 112 y máximo 75.

## Requisito 4. El informe de un museo

**Entradas:** nombre del museo y datos de sus días registrados.

**Salidas:** nombre, aforo diario, cantidad de días, visitantes totales, promedio diario y porcentaje de asistencia.

**Reglas y validaciones:**
- El museo debe existir.
- Visitantes totales = suma de visitantes registrados.
- Promedio = visitantes totales / días registrados.
- Porcentaje de asistencia = promedio / aforo diario × 100.
- Promedio y porcentaje se redondean con round a dos decimales.
- Sin días registrados, se muestra el aviso correspondiente y no se presentan indicadores adicionales.

**Prueba propuesta:** con visitantes 400, 120, 100, 450 y 350 y aforo 500, comprobar total 1420, promedio 284.0 y asistencia 56.8 %.

## Requisito 5. La desviación estándar

**Entradas:** cantidades de visitantes de cada día y promedio de visitantes.

**Salidas:** desviación estándar redondeada a dos decimales, incluida en el informe.

**Reglas y validaciones:**
- Restar el promedio a cada cantidad diaria y elevar cada diferencia al cuadrado.
- Sumar los cuadrados, dividir entre la cantidad de días y obtener la raíz cuadrada.
- Redondear el resultado a dos decimales.
- Con un solo día registrado, la desviación estándar es 0.0.
- Sin días registrados, se aplica la regla del requisito 4: no mostrar indicadores.

**Prueba propuesta:** para la Casa de la Música, con 50, 80, 130 y 180 visitantes, comprobar desviación estándar 49.5.
