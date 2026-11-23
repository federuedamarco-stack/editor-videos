# Reglas de estilo · ExoMov

Fuente: el sistema de diseño de la marca (`referencias/ExoMov-DESIGN.md`), pasado a reels de 1080×1920.
Si algo de la skill (por ejemplo, el «cristal líquido» violeta o el rebote de las tarjetas) choca con esta guía, **manda esta guía**.

## Marca y tono
- ExoMov acerca los exoesqueletos que se llevan puestos a personas de toda España: para caminar, trabajar, hacer senderismo y en rehabilitación.
- Tiene que sentirse **nueva, innovadora y cercana**: es tecnología que ayuda a una persona real a moverse, no un objeto de laboratorio.
- No debe parecer una start-up tecnológica genérica, un catálogo médico frío ni una marca de suplementos deportivos.
- Textos en español, tratando de «tú». Titulares cortos, de 2 a 6 palabras.

## Lienzo y zona segura
- 1080×1920, 30 fps.
- Nada importante en los 220 px de arriba, los 380 px de abajo ni los 140 px de la derecha.

## Tipografía (archivos en `tipografias/`)
- **Palabra clave y titulares**: Bebas Neue 400, siempre en mayúsculas, espaciado 0,01 em, de 160 a 200 px. Una palabra clave por frase. Nunca por debajo de 72 px.
- **Subtítulos y texto de apoyo**: Figtree 700, de 60 a 64 px. Las cifras y los datos van en Figtree 800.
- **Etiquetas**: Figtree 700, mayúsculas, 30 px, espaciado 0,06 em.
- **Datos técnicos o códigos** (rara vez): JetBrains Mono 600, 30 px.
- Como máximo 2 fuentes en pantalla a la vez.

## Color
- **El lima `#BEBD39` es el único acento.** Un solo elemento lima por escena: lo más importante (la palabra clave, la cifra o la llamada a la acción).
- El lima se usa **como relleno, con texto tinta `#121311` encima**, o como texto sobre fondo oscuro. Nunca como texto o línea fina sobre un fondo claro: ahí, el texto en lima va en `#5C5B16`.
- Tinta `#121311` · superficie oscura `#1B1C19` · superficie 2 `#262723` · borde `#3A3B35`.
- Blanco cálido `#F6F6F1` para el texto · gris cálido `#A9A99E` para el texto secundario.
- Colores de estado (`#6FCF97` éxito, `#F2867D` error) solo para estados, siempre acompañados de una palabra.
- **Sin degradados.**

## Subtítulos
- De 1 a 3 palabras a la vez, cada una cuando la digo. Mínimo 0,4 s en pantalla.
- Figtree 700, de 60 a 64 px, en blanco `#F6F6F1`. Para que se lea sobre el vídeo, sombra de tinta suave (`0 4px 18px rgba(18,19,17,.55)`), **sin brillo de color**.
- Palabra clave en Bebas Neue lima `#BEBD39`, más grande, con la misma sombra.
- Siempre a la altura del pecho, nunca encima de mi cara: caja con `top 1260`, alto 260, `left 80`, `right 150`.

## Motion graphics
- **Tarjetas planas**, no de cristal: fondo tinta `#121311` al 88 % de opacidad, borde de 2 px `#3A3B35`, radio de 28 px y relleno de 48 px. Sin degradados, sin brillo y sin barrido de luz.
- Tarjeta destacada (como mucho una por reel, para la cifra clave o la llamada a la acción): relleno lima `#BEBD39` con texto tinta `#121311`.
- Etiquetas en forma de píldora (radio 999 px), de 56 px de alto, con fondo `#262723` y texto `#F6F6F1`.
- **Movimiento «asistir, no empujar»**: el movimiento acompaña y se asienta suave, como el exoesqueleto.
  - Entrada de 0,32 a 0,48 s con `cubic-bezier(0.3, 0, 0.1, 1)` (en GSAP, `power3.out`): sube 40 px y aparece. **Sin rebote.**
  - Salida de 0,2 s con `cubic-bezier(0.3, 0, 1, 1)`.
  - Cifras y barras de progreso: cuentan o se llenan en 0,48 s con la misma curva.
- Una idea por escena. Las tarjetas empiezan por debajo de la barbilla, también con el zoom máximo (`top ≥ 1065`).
- Zoom suave del 6 % como mucho, con curva y nunca a saltos.
- Escena a pantalla completa: fondo liso tinta `#121311` o piedra `#ECECE4`, con una cuadrícula sutil de 1 px en `#262723`. Sin orbes ni degradados.

## Logo (archivos en `logos/`)
- `exomov-logo-blanco.png` sobre vídeo o fondos oscuros · `exomov-logo-negro.png` sobre lima o piedra · `exomov-simbolo-blanco.png` (solo el símbolo) para una firma pequeña.
- Al cierre: logo completo centrado, de 640 px de ancho, sobre tinta `#121311`.
- Durante el vídeo, si aparece: el símbolo arriba a la izquierda, de 96 px de alto y dentro de la zona segura.
- **Usa siempre el logo oficial, nunca lo recrees**, y no lo deformes, no le cambies los colores (solo blanco o tinta) ni le pongas efectos.

## Ritmo y cortes
- Sin pausas de más de 0,4 s. Un cambio visual cada 2 o 3 segundos.

## Sonido
- Tono cercano y con energía, sin dramatismo de tráiler: un golpe suave en el gancho, un clic en los checks, un whoosh en los cambios de escena y un cierre limpio.
- La voz siempre por encima. −14 LUFS y pico real por debajo de −1 dB.

## Imágenes
- Personas reales usando el dispositivo en sitios cotidianos de España (calle, casa, trabajo, montaña), a la altura de los ojos y con luz natural.
- Fotos del producto sobre fondo liso piedra `#ECECE4` o tinta `#121311`.

## Prohibido
- Emojis, degradados, brillos de neón y contornos blancos a mi alrededor.
- Tarjetas sobre mi cara.
- Cifras inventadas. Las especificaciones (peso, batería, par de asistencia) solo con el dato real; si no lo tengo, no aparece.
- Imágenes «futuristas» de stock, hologramas azules y clichés de hospital.
- Usar el lima para texto sobre fondo claro.
