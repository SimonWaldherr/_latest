--- 
extends: _layouts.post 
section: content 
image: https://cdn.businessinsider.es/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2020/08/app-rastreo-coronavirus-espana-radar-covid-2041415.jpg?itok=IbdSSxvB 
title: > 
  Brecha de seguridad en RadarCOVID: incluso Amazon pudo acceder a los códigos de los ciudadanos que confirmaron su contagio en la plataforma 
description: > 
  Las apps para ayudar en el rastreo de contactos y detener las cadenas de contagios de coronavirus están implementadas ya en varios países europeos.La mayoría siguen un protocolo desarrollado por Apple y Google que garantiza la seguridad y la privacidad de los usuarios.El problema es que estos códigos aleatorios pueden interceptarse, en el caso de que un ciberdelincuente pueda acceder al tráfico por el que se transmiten estos códigos.RadarCOVID liberó su código a principios de septiembre, varias semanas después de que se desplegara a nivel nacional.Algunos expertos apuntan en que si se hubiera liberado antes, esta brecha se podría haber subsanado antes. 
keywords: > 
  su, plataforma, la, códigos, en, pudo, los, radarcovid, se, seguridad, al, y, incluso, por, que, el 
date: 1603378326.5709558 
--- 
<div><p>Al final no era tan segura.</p>

<p>RadarCOVID ha sufrido <strong>un grave problema de privacidad</strong>, seg&#250;n ha adelantado este jueves <a href="https://elpais.com/tecnologia/2020-10-22/la-app-radar-covid-ha-tenido-una-brecha-de-seguridad-desde-su-lanzamiento.html" rel="nofollow" target="_blank">el diario El Pa&#237;s.</a> Las apps para ayudar en el rastreo de contactos y detener las cadenas de contagios de coronavirus est&#225;n implementadas ya en varios pa&#237;ses europeos. La mayor&#237;a siguen un protocolo desarrollado por Apple y Google que garantiza la seguridad y la privacidad de los usuarios.</p>

<p>Bajo este protocolo, los tel&#233;fonos pr&#243;ximos comparten una serie de c&#243;digos generados de forma aleatoria para que cada usuario pueda llevar un historial de personas con las que ha estado cerca. Si un paciente da positivo por COVID-19, su m&#233;dico le entregar&#225; una clave que, al introducirse en la app, har&#225; que todos los tel&#233;fonos con los que se ha cruzado &#8212;a menos de metro y medio y durante m&#225;s de 15 minutos&#8212; <strong>reciban una alarma</strong> por posible exposici&#243;n al virus.</p>

 

<p>El problema es que estos c&#243;digos aleatorios <strong>pueden interceptarse</strong>, en el caso de que un ciberdelincuente pueda acceder al tr&#225;fico por el que se transmiten estos c&#243;digos. Para evitarlo, muchos gobiernos europeos suben al servidor paquetes de c&#243;digos falsos, a fin de que estas claves sean mucho m&#225;s dif&#237;ciles de deanonimizar.</p>

<p>RadarCOVID <strong>no implement&#243; esta caracter&#237;stica </strong>hasta que se actualiz&#243; a una nueva versi&#243;n el pasado 8 de octubre. Los servicios sanitarios de las comunidades aut&#243;nomas comenzaron a implementar esta herramienta tecnol&#243;gica a finales de agosto.</p>

<blockquote class="twitter-tweet">
<p dir="ltr" lang="es">Adem&#225;s, protege a&#250;n m&#225;s tu privacidad al comunicar tu positivo por <a href="https://twitter.com/hashtag/COVID19?src=hash&amp;ref_src=twsrc%5Etfw">#COVID19</a> para que nadie pueda saber que fuiste t&#250;:<br>
<br>
&#128274; La app enviar&#225; de forma autom&#225;tica positivos ficticios al servidor<br>
<br>
&#128567; De esa manera, ser&#225; imposible distinguir qu&#233; positivos son reales en caso de ataque</p>
&#8212; S.E. Digitalizaci&#243;n e Inteligencia Artificial (@SEDIAgob) <a href="https://twitter.com/SEDIAgob/status/1314252631649456128?ref_src=twsrc%5Etfw">October 8, 2020</a>

<p>&#160;</p>
</blockquote>

<p>El diario El Pa&#237;s <a href="https://elpais.com/tecnologia/2020-10-22/la-app-radar-covid-ha-tenido-una-brecha-de-seguridad-desde-su-lanzamiento.html" rel="nofollow" target="_blank">avanza este jueves</a> que, adem&#225;s de un posible ciberdelincuente con capacidad de acceder a ese tr&#225;fico de c&#243;digos, <strong>empresas como Amazon tienen acceso.</strong> La raz&#243;n es que Minsait, la compa&#241;&#237;a de Indra responsable del desarrollo, utiliza un software del gigante estadounidense para subir los c&#243;digos de los infectados al servidor central.</p><p class="ad-container"></p>

<p>Como explica el periodista Jordi Perez Colom&#233;, aunque estos c&#243;digos se generan de forma aleatoria y est&#225;n cifrados, solo se suben al citado servidor los c&#243;digos de infectados. "Quien tenga acceso al tr&#225;fico, por tanto, sabe qui&#233;n lo es".</p>

 

<p>El Gobierno ha defendido en declaraciones a El Pa&#237;s que la vulnerabilidad no se comunic&#243; al p&#250;blico en general porque la brecha ten&#237;a <strong>"un alcance muy limitado"</strong>, "dado que pod&#237;a ser explotada solo por el operador de comunicaciones". El peri&#243;dico detalla, aun as&#237;, que el problema exist&#237;a y "deb&#237;a ser reparado".&#160;</p>

<p>La <strong>Secretar&#237;a de Estado de Digitalizaci&#243;n e Inteligencia Artificial</strong> es la &#250;ltima responsable de la app. Tambi&#233;n lo fue de comunicarle la existencia de este agujero de seguridad a la <strong>Agencia Espa&#241;ola de Protecci&#243;n de Datos</strong> (AEPD), que se produjo "de alg&#250;n modo" seg&#250;n ha podido saber Colom&#233;. Adem&#225;s, fuentes de la propia Secretar&#237;a de Estado le remachan que la brecha no se hizo p&#250;blica porque "no ha habido constancia de una violaci&#243;n de la seguridad de los datos personales".</p>

<p>La introducci&#243;n de c&#243;digos falsos se introdujo <a href="https://github.com/RadarCOVID/radar-covid-backend-verification-server/commit/2958d3d13203ed2373eb032281ef4d67ab6e3e59" rel="nofollow" target="_blank">a principios de octubre</a> y es una de las caracter&#237;sticas que ya se recog&#237;a <a href="https://www.businessinsider.es/rastreo-contactos-claves-app-ayudara-desescalada-644557" title='Por qu&#233; es importante que el Gobierno prepare su app de rastreo "interoperable", seg&#250;n una investigadora clave en el desarrollo de esta tecnolog&#237;a'>en el protocolo DP-3T</a> que desarrollaron investigadores europeos antes de que Apple y Google trabajasen en su desarrollo propio.</p>

<p>RadarCOVID liber&#243; su c&#243;digo a principios de septiembre, varias semanas despu&#233;s de que se desplegara a nivel nacional. Algunos expertos <a href="https://twitter.com/sergiocm/status/1319246426921181184" rel="nofollow" target="_blank">apuntan</a> en que si se hubiera liberado antes, esta brecha se podr&#237;a haber subsanado antes.</p>
</div>