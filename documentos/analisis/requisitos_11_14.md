## Análisis de los requisitos 11 al 14 

### Requisito 11: Porcentaje de asistencia más alto y más bajo

**Entradas**
- Ninguna tecleada. Usa los museos que ya están en el programa (opción 5 del menú).

**Salidas**
- Nombre y porcentaje de asistencia del museo con el porcentaje más alto.
- Nombre y porcentaje de asistencia del museo con el porcentaje más bajo.
- Porcentajes redondeados a 2 decimales.
- Si ningún museo tiene días registrados: aviso de que ningún museo tiene días registrados.

**Reglas del dominio**
- Porcentaje de asistencia = (promedio de visitantes por día / aforo diario) × 100.
- Solo participan los museos con al menos 1 día registrado.
- La comparación se hace con los valores **sin redondear**; el redondeo es solo al mostrar.
- En caso de empate gana el museo que se creó o se cargó primero (orden de creación).

**Validaciones**
- Filtrar los museos sin días registrados antes de comparar.
- Si la lista filtrada queda vacía (sin museos, o museos sin días): mostrar el aviso y volver al menú.

---

### Requisito 12: Cargar los museos desde un archivo

**Entradas**
- Ruta del archivo de museos (la ruta del de visitantes se lee después, en el req. 13).
- Contenido del archivo CSV (UTF-8, separado por `;`): línea 1 = encabezado; cada línea siguiente con 5 campos: `nombre;aforo_diario;año;mes;día`.

**Salidas**
- Cantidad de museos cargados.
- Por cada línea descartada: su número de línea y la causa.
- Avisos: "el archivo no existe" o "la carga solo se hace con el programa sin museos".

**Reglas del dominio**
- La carga solo se permite si el programa **no tiene ningún museo**; así una segunda carga no duplica nada. Si ya hay alguno: aviso, vuelve al menú y **no lee ninguna ruta**.
- Cada línea válida crea un museo sin días registrados.
- Los espacios al inicio o al final de cada campo no cuentan.
- Las líneas vacías se saltan sin aviso.
- Una línea inválida no detiene la carga: se descarta, se informa y se sigue con la siguiente.
- El número de línea cuenta el encabezado como línea 1 (en el ejemplo, "Museo del Tren" es la línea 4).

**Validaciones** (en este orden; se informa solo la primera que falla)
1. La línea no tiene 5 campos.
2. El nombre está vacío.
3. Ya existe un museo con ese nombre (incluye los cargados antes en el mismo archivo).
4. El aforo diario no es un número entero.
5. El aforo diario es menor que 1.
6. El año, mes y día no son enteros o no forman una fecha válida del calendario.
- Si el archivo de museos no existe: aviso, no se carga ningún museo y **no se lee** la ruta del archivo de visitantes.

---

### Requisito 13: Cargar los visitantes desde un archivo

**Entradas**
- Ruta del archivo de visitantes.
- Contenido del archivo CSV (UTF-8, separado por `;`): línea 1 = encabezado; cada línea siguiente con 2 campos: `museo;visitantes`.

**Salidas**
- Cantidad de días cargados.
- Por cada línea descartada: su número de línea y la causa.
- Aviso "el archivo no existe" si no se encuentra el archivo.

**Reglas del dominio**
- Las líneas de cada museo vienen en orden de días: cada línea válida agrega al museo **el día siguiente** de su registro.
- Los espacios alrededor de un campo no cuentan; las líneas vacías se saltan; una línea inválida se descarta con su número y causa, y la carga sigue.
- Si el archivo de visitantes no existe, los museos ya cargados se quedan en el programa **sin días registrados**.
- Como la carga (req. 12) solo funciona con el programa sin museos, para cargar el archivo de visitantes después hay que ejecutar el programa de nuevo.
- Una línea descartada no consume un día: la siguiente válida del mismo museo toma ese día (ejemplo: Casa de la Música queda con 50, 80, 130 y 180).

**Validaciones** (se informa solo la primera que falla)
1. La línea no tiene 2 campos.
2. No existe un museo con ese nombre (comparación exacta con mayúsculas y tildes, sin espacios en los extremos).
3. Los visitantes no son un número entero.
4. Los visitantes no están entre 0 y el aforo diario de ese museo.

---

### Requisito 14: El menú

**Entradas**
- La opción tecleada por el usuario (se lee como texto, porque puede no ser un número).

**Salidas**
- El menú con 7 opciones numeradas:
  1. Crear un museo
  2. Registrar los visitantes del día siguiente
  3. Simular días
  4. Ver el informe de un museo
  5. Ver el museo con el porcentaje de asistencia más alto y el más bajo
  6. Cargar los museos y los visitantes desde archivos
  7. Salir
- Aviso "la opción no es válida" cuando corresponda.

**Reglas del dominio**
- Después de atender cualquier opción distinta de 7, el programa vuelve a mostrar el menú.
- La opción 7 termina el programa.
- Cada opción ejecuta el requisito correspondiente (1 → req. 1, 2 → req. 2, 3 → req. 3, 4 → req. 4 al 9, 5 → req. 11, 6 → req. 12 y 13).
- Las opciones 2, 3 y 4 piden el nombre del museo; si no existe, avisan y vuelven al menú (req. 10).

**Validaciones**
- Si lo tecleado no es un entero (por ejemplo `dos`) o está fuera de 1 a 7 (por ejemplo `8`): avisar que la opción no es válida y volver a mostrar el menú.

---

### Dudas para aclarar con el grupo
- Una línea del archivo con solo espacios, ¿cuenta como vacía (se salta sin aviso)? Para el análisis la tratamos como vacía.
- Si el archivo de museos existe pero ninguna línea es válida (0 museos cargados), ¿se pide igual la ruta del archivo de visitantes? El enunciado solo corta la lectura cuando el archivo no existe, así que asumimos que sí se pide y todas sus líneas se descartan por "no hay un museo con ese nombre".
- En el menú, ¿una opción con espacios como ` 7 ` es válida? El enunciado no lo dice; se propone aceptarla quitando espacios, igual que con los nombres.
