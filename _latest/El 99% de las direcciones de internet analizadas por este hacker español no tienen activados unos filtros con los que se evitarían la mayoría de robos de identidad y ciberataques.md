--- 
extends: _layouts.post 
section: content 
image: https://cdn.businessinsider.es/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2020/09/hacker-vegas-2083795.jpg?itok=hUrXJc6- 
title: > 
  El 99% de las direcciones de internet analizadas por este hacker español no tienen activados unos filtros con los que se evitarían la mayoría de robos de identidad y ciberataques 
description: > 
  El phising es una de las puertas de entrada más comunes por la que los ciberdelincuentes son capaces de atacar empresas privadas y administraciones públicas.Los expertos insisten desde hace años en que los trabajadores son el eslabón "más débil" en la cadena de la ciberseguridad.Lo cierto es que, efectivamente, los profesionales son la primera línea de defensa de las organizaciones frente a ciberataques.Quiere huir del vendehumismo y es consciente de que en el sector "todo es muy complicado".Con este trabajo, del que el propio Marc irá informando paulatinamente, el especialista espera "hacer una fotografía global" de este problema. 
date: 1602310301.2820983 
--- 
El phising es una de las puertas de entrada más comunes por la que los ciberdelincuentes son capaces de atacar empresas privadas y administraciones públicas. Los expertos insisten desde hace años en que los trabajadores son el eslabón "más débil" en la cadena de la ciberseguridad. Algunos profesionales del Instituto Nacional de Ciberseguridad prefieren plantear que los empleados son el eslabón más "importante".

Lo cierto es que, efectivamente, los profesionales son la primera línea de defensa de las organizaciones frente a ciberataques. Por más soluciones de seguridad informática que apliquen sus responsables —perimetrar sus sistemas, escalar y fragmentar privilegios, aplicar la doble autenticación—, si un usuario entrega su contraseña en un correo suplantado o si se descarga un malware pensando que es una carta de un superior, todo saltará igualmente por los aires.

Pero esta problemática no se puede zanjar descargando toda la responsabilidad únicamente en los empleados. Al menos eso piensa Marc Almeida, un profesional de la programación y un apasionado de la ciberseguridad que reside en Salou, Cataluña.

Almeida —Cibernicola, en redes sociales— ya llamó la atención de buena parte de la comunidad de la seguridad informática española hace unos meses cuando presentó los avances y las ambiciones que traían su proyecto Obelix Teh Honeypot, un sistema de 'sondas' capaces de detectar ataques en tiempo real en el ciberespacio. Estas sondas se camuflan en la red como si fuesen dispositivos o servidores abandonados, a expensas de los ataques de enjambres de bots.

Leer más: Estos hackers españoles están instalando una red de balizas digitales para estudiar cómo es la ciberguerra que se está librando de forma invisible a tus ojos

Con Obelix, Marc Almeida pudo empezar a dibujar algunos famosos pew pew maps, una socarrona forma que tiene el argot de la ciberseguridad para referirse a los habituales mapas del mundo con el que las compañías de ciberseguridad tratan de impresionar a sus clientes. Pero sobre todo, y lo más importante: con Obelix, Almeida pudo empezar a hacerse nuevas preguntas.

Marc lleva 20 años trabajando en el sector técnico y siempre ha mantenido un perfil discreto. Quiere huir del vendehumismo y es consciente de que en el sector "todo es muy complicado". Pero dado que en los últimos meses se han registrado diversas suplantaciones con phising —en las últimas semanas, al Ministerio de Trabajo o a Correos—, este especialista se plantea una cosa. "Hablemos de los problemas en su origen".

'Spoofing', el fenómeno detrás de muchas estafas e incidentes

Mientras que el phising es un intento fraudulento de hacer creer a una víctima que está recibiendo y tratando un correo electrónico genuino, el spoofing va un paso más allá. Supone, de facto, la suplantación de una identidad en la red con fines espúreos.

El phising, por un lado, puede ser un correo electrónico que recibas supuestamente de la Dirección General de Tráfico. La DGT no va a enviarte nunca un correo electrónico a altas horas de la noche recordándote ninguna supuesta multa impagada. Y menos te va a decir que para abrir la información sobre la penalización vas a tener que usar un sistema operativo Windows, como es el caso.

Este tipo de correos llegan además de emisores con direcciones de correo falsas. Por ejemplo, @interior.gov. Los correos del Gobierno de España usan los dominios .gob, con 'b'.

Leer más: Google y el INCIBE lanzan un curso de formación gratuito y en línea para ayudar a las empresas a formar a sus trabajadores en ciberseguridad

Pero, ¿qué ocurre si un ciberdelincuente está enviando emails desde una dirección aparentemente real del Gobierno de España? Lo que está haciendo ese ciberdelincuente es aprovecharse de un dominio mal configurado.

Aquí, Marc Almeida pone el dedo en la llaga.

SPF, DKIM y DMARC: protocolos tan básicos como olvidados

Si has recibido un correo procedente de una dirección aparentemente legítima y estás seguro de que es falso, es muy probable que estés ante un caso por el cual los ciberdelincuentes han conseguido aprovecharse de la vulnerabilidad de un dominio. Un dominio por lo general "aparcado" —en desuso— pero que no se ha segurizado debidamente.

Esta vulnerabilidad existe cuando los propietarios de las direcciones web no han activado de forma efectiva tres filtros esenciales en la ciberseguridad: los filtros SPDF, DKIM y DMARC.

El Instituto Nacional de Ciberseguridad abunda en un artículo publicado en su página web que el SPF es un protocolo para autenticar correos electrónicos que permite al propietario de un dominio "especificar qué servidores usará para el envío del email". El DKIM es otro protocolo que "asocia un nombre de dominio a un mensaje mediante técnicas criptográficas". Y el DMARC es "un estándar de autenticación de correos que verifica tanto SPF como DKIM".

A pesar de que resulta una obviedad para los expertos del INCIBE, una investigación del proyecto personal de Marc Almeida demuestra que menos del 2% de los dominios que ha podido analizar tienen activados estos filtros. De una muestra provisional de cerca de 40 millones de dominios.

Todo esto lo está haciendo Marc acompañado de varios de sus colaboradores. Como detalla en su propia web, el proyecto se conoce como Domain Hunter DMARC Edition, y funciona mediante un pequeño script —un código ejecutable de una categoría inferior a un programa informático— que es capaz de leer la información que extrae de los dominios que analiza para saber si tienen convenientemente configurados estos filtros que el propio INCIBE recomienda.

Marc lleva semanas trabajando con este proyecto. Tiene una base de 250 millones de dominios que consiguió adquiriéndosela a una compañía estadounidense. Es muy difícil cuantificar cuántos dominios puede haber en la red. Algunas estimaciones los elevan a los 1.200 millones.

Un análisis masivo que revela importantes agujeros de seguridad

En una conversación con Business Insider España, Marc Almeida revela que solo ha estudiado hasta ahora algo menos del 10% de toda la muestra total con la que cuenta. Es decir, de cerca de 250 millones de dominios, solo ha podido acceder a casi 40 millones. De esos 40 millones de dominios analizados, menos de 53.000 tenían bien configurados estos filtros.

En otras palabras: el 1% de los dominios de la muestra analizada por Marc cuentan con los parámetros de seguridad informática que recomiendan los expertos del INCIBE. En otras palabras: el 99% de la muestra examinada es vulnerable a técnicas de spoofing y suplantación de identidad.

De todos los dominios investigados, casi 680.000 de ellos están ligados a España. Son los dominios cuyas terminaciones son .es, .cat, .com.es, .gob.es, .eus, o .gal. De la muestra analizada hasta ahora, menos de 850 dominios —solo 850 dominios— están segurizados con los filtros anteriormente mencionados.

Con este trabajo, del que el propio Marc irá informando paulatinamente, el especialista espera "hacer una fotografía global" de este problema. "La idea es manejar mucha información, muchos datos, generar nueva información y hacerse más preguntas", reconoce.

En el ámbito de la seguridad informática, reconoce, hay "millones de frentes". "Y todos ellos son importantes". "Lo que no entiendo, y me gustaría entenderlo de forma fehaciente, es por qué esto no se está haciendo ya en todos lados".

El filtro DMARC, precisamente, es uno de los proyectos a implantar en el ámbito de la seguridad informática para este 2020 y 2021, según la consultora Gartner. Y, a tenor de lo que reflejan los primeros resultados de Domain Hunter de Marc Almeida, su implantación es prácticamente nula.