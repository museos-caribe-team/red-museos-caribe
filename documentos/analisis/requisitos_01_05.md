
# Análisis de requisitos

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

## Requisito 6. El día de más y el de menos visitantes

**Entradas:** cantidades de visitantes de cada día y fecha de inicio del registro.

**Salidas:** fecha del día con más visitantes y fecha del día con menos visitantes, incluidas en el informe.

**Reglas y validaciones:**
- Recorrer la lista de registros diarios desde el primer día hasta el último, asociando a cada índice $i$ la fecha $\text{fecha de inicio} + i\text{ días}$.
- Identificar el valor máximo y el valor mínimo de visitantes.
- Si varios días empatan en el máximo o en el mínimo, conservar el primero que ocurrió (comparación estricta `>` para el máximo y `<` para el mínimo).
- Con un solo día registrado, esa misma fecha corresponde tanto al día de más visitantes como al de menos visitantes.
- Sin días registrados, se aplica la regla del requisito 4: no mostrar indicadores.

**Prueba propuesta:** en un museo con aforo diario de 500 que registra 250, 500, 500, 100 y 100 visitantes desde el 1 de noviembre de 2026, comprobar que el día de más visitantes es `2026-11-02` y el de menos visitantes es `2026-11-04`.

---

## Requisito 7. Los días en cada nivel de asistencia

**Entradas:** cantidades de visitantes de cada día y aforo diario del museo.

**Salidas:** cantidad de días en cada uno de los cuatro niveles de asistencia (Baja, Media, Alta y Plena), incluida en el informe.

**Reglas y validaciones:**
- Calcular el porcentaje de ocupación de cada día sin redondear: $(\text{visitantes del día} / \text{aforo diario}) \times 100$.
- Clasificar cada día en un único nivel:
  - Baja: menos del 30 %.
  - Media: desde el 30 % hasta menos del 60 %.
  - Alta: desde el 60 % hasta menos del 85 %.
  - Plena: el 85 % o más.
- Mostrar los cuatro niveles en el orden exacto: baja, media, alta y plena, incluyendo los niveles con 0 días.
- Sin días registrados, se aplica la regla del requisito 4: no mostrar indicadores.

**Prueba propuesta:** para el Museo del Mar (aforo 500, registros 400, 120, 100, 450 y 350), comprobar 2 días en asistencia baja, 0 en media, 2 en alta y 1 en plena.

---

## Requisito 8. La racha más larga en asistencia baja

**Entradas:** cantidades de visitantes de cada día, aforo diario y fecha de inicio del registro.

**Salidas:** duración en días de la racha más larga en asistencia baja y fecha del día en que empezó, o aviso de que no hubo días en asistencia baja, incluida en el informe.

**Reglas y validaciones:**
- Contar las secuencias de días consecutivos cuyo nivel de asistencia sea Baja (menos del 30 % del aforo).
- Reiniciar el contador de la racha actual a 0 cada vez que aparezca un día con asistencia media, alta o plena.
- Si dos rachas empatan en la mayor longitud, conservar la que empezó primero (comparación estricta `>`).
- Si ningún día registrado tuvo asistencia baja, mostrar el aviso correspondiente en lugar de días y fecha.
- Sin días registrados, se aplica la regla del requisito 4: no mostrar indicadores.

**Prueba propuesta:** en un museo con aforo de 500 que registra 120, 90, 350, 140, 60, 100 y 420 visitantes desde el 1 de noviembre de 2026, comprobar racha más larga de 3 días con inicio el `2026-11-04`.

---

## Requisito 9. Los días sin registrar

**Entradas:** fecha de inicio del registro, cantidad de días registrados y fecha actual tomada del reloj del computador.

**Salidas:** fecha del último día registrado y cantidad de días que faltan por registrar (o aviso de que el registro está al día), incluida en el informe.

**Reglas y validaciones:**
- Calcular la fecha del último día registrado como $\text{fecha de inicio} + (\text{días registrados} - 1)\text{ días}$.
- Calcular los días sin registrar desde el día siguiente al último registrado hasta el día anterior a la fecha actual ($\text{fecha actual} - 1\text{ día}$).
- Si el último día registrado es igual o posterior al día anterior a la fecha actual (incluyendo fechas futuras por simulación), indicar que el registro está al día.
- Sin días registrados, se aplica la regla del requisito 4: no mostrar indicadores.

**Prueba propuesta:** ejecutando el programa el 20 de noviembre de 2026 para el Museo del Mar (último día registrado `2026-11-05`), comprobar que faltan por registrar 14 días, del `2026-11-06` al `2026-11-19`.

---

## Requisito 10. Varios museos en el mismo programa

**Entradas:** nombre de un museo ingresado por teclado para cualquier operación (crear, registrar día, simular días o mostrar informe).

**Salidas:** ejecución de la operación sobre el museo encontrado, o aviso de que no existe (o que ya existe al intentar crearlo) y retorno al menú.

**Reglas y validaciones:**
- Almacenar todos los museos creados o cargados en una colección durante la sesión del programa.
- Eliminar los espacios al principio y al final del nombre leído antes de buscar o comparar.
- Comparar el nombre de forma exacta, respetando mayúsculas, minúsculas y tildes.
- Impedir la creación de un museo con un nombre ya existente sin alterar los datos del museo original.

**Prueba propuesta:** con el Museo del Mar registrado, buscar `"museo del mar"` en minúsculas y comprobar el aviso de que no existe; luego intentar crear otro `"Museo del Mar"` y comprobar el aviso de duplicado sin perder los datos previos.

**Prueba propuesta:** para la Casa de la Música, con 50, 80, 130 y 180 visitantes, comprobar desviación estándar 49.5.
