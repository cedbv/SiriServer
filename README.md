Siri Server
===========

IMPORTANT
---------

Si vous avez des problèmes pour installer ce serveur ou quelque chose d'autre, lisez d'abord ce document jusqu'au bout et si vous avez encore des problèmes, visitez [le forum de SiriServer](http://hack.silentspark.net/phpbb/index.php) (en).
Merci de NE PAS utiliser la section Issues de GitHub pour rapporter des problèmes concernant l'installation du serveur.

Il y a actuellement quelques plugins installés ici. La plupart sont traduits en français et pour certains, c'est même la seule langue disponible.
Vous pouvez parler un peu à Siri, lui demander la météo, l'heure, régler l'alarme et le minuteur, prendre des notes, définir des mots, indiquer l'emplacement actuelle et des commerces à proximité, d'afficher des images, de rechercher sur le Web et sur Wikipedia, de traduire en près de 50 langues, d'obtenir des renseignements sur vos films préférés, et plus encore...
Spécifiquement pour la Belgique, Siri est capable de vous dire le programme TV, les horaires de train, de rechercher dans l'annuaire, et les résultats du lotto et de l'EuroMillions.
Dans une moindre mesure, Siri peut également répondre à des questions diverses grâce à Wolfram Alpha (personnalités, calculs, etc.).
Vous pouvez trouver [le détail de mes plugins sur le wiki](https://github.com/cedbv/SiriServer/wiki/French-Plugins).

Vous pouvez contribuer en créant vous même vos propres plugins !

Qu'est ce que c'est ?
----------------------

C'est une version très précoce d'un serveur pour Siri (à ne pas confondre avec un proxy).

Siri d'Apple est un assistant contrôlé par la voix disponible uniquement sur l'iPhone 4S.

Grâce au jailbreak, vous pouvez l'installer sur d'autres appareils iOS.
Cependant, Siri nécessite un serveur avec lequel communiquer pour le traitement de la voix.
Apple autorise uniquement les iPhone 4S sur leurs serveurs.

Ce projet tente de recréer le serveur Siri d'Apple pour pouvoir l'utiliser sur d'autres appareils iOS.

Ce serveur utilise l'API Speech-To-Text (transcription de la voix) de Google. 
De plus, nous sommes actuellement limité à des commandes durant maximum 10 secondes (peut-être que cette limite pourra être supprimée plus tard).

Plus spécifiquement, vous êtes sur la version française la plus aboutie pour le moment de l'excellent [SiriServer de Eichhoernchen](https://github.com/Eichhoernchen/SiriServer).
C'est à lui que nous devons ce serveur. Je n'ai fais que la traduction française et le développement de plugins (et quelques améliorations légères dans le coeur).

Quoi de neuf ?
--------------
Nous avons un nouveau système de plugins :
Regardez le dossier [plugins](https://github.com/cedbv/SiriServer/tree/master/plugins) et le [plugin d'exemple](https://github.com/cedbv/SiriServer/blob/master/plugins/examplePlugin.py) pour plus d'informations.
Il permet le support de plusieurs langues.

Vous pouvez également regarder le fichier [plugin.py](https://github.com/cedbv/SiriServer/blob/master/plugin.py) pour voir les méthodes prédéfinies pour les plugins.
Vous pouvez également regarder le plugin horloge ([time.py](https://github.com/cedbv/SiriServer/blob/master/plugins/time.py)). Il utilise des objets plus complexes et est localisé en plusieurs langues. Et il parse de façon plus complexe, les commandes données par l'utilisateur.

Qu'est ce qu'il y a d'autre ici ?
----------------------------------
Le document [SiriProtocol](https://github.com/cedbv/SiriServer/blob/master/SiriProtocol) qui inclus tout ce que Eichhoernchen (et d'autres) ont trouvé à propos du protocole de Siri.


Setup, Notes and Instructions
-----------------------------

**Installer**

There is an experimental installer by [johanberglind](https://github.com/johanberglind) which does the steps described below, you may try it instead of the manual method.
You can get it here: [Installer on Github](https://github.com/johanberglind/InstallSiriServer)

**Install audio libraries**

For the audio handling you need [libspeex](http://www.speex.org/) and [libflac](http://flac.sourceforge.net/)

On Linux simply install it via you packet manager e.g. (or see instructions and note for OS X):

	sudo apt-get install libspeex1 libflac8

On OS X download libspeex and libflac from the websites above (the sources, not the binaries)
and compile and install them, or simply follow the following steps:

	wget http://downloads.xiph.org/releases/speex/speex-1.2rc1.tar.gz
	tar -xf speex-1.2rc1.tar.gz
	cd speex-1.2rc1
	./configure
	make
	sudo make install
	cd ..
	
	wget http://sourceforge.net/projects/flac/files/flac-src/flac-1.2.1-src/flac-1.2.1.tar.gz/download -O flac-1.2.1.tar.gz
	tar -xf flac-1.2.1.tar.gz
	./configure --disable-asm-optimizations
	make
	sudo make install
Note: you can also install libspeex via MacPorts, but libflac is not available in 64bit through MacPorts, to make it build with 64bit support you need to supply `--disable-asm-optimizations` in configure of libflac to make it compile

**Python requirements**

As this project is coded with python you need a python interpreter (this is usually already installed).
I work with python 2.6.6 and 2.7.2 and both work.

You also need some python packages to make it work:

	biplist
	M2Crypto

You can install both via `easy_install`,
easy_install is available at [http://pypi.python.org/pypi/setuptools](http://pypi.python.org/pypi/setuptools),
on Linux you can also get it via your packet manager:

	sudo apt-get install python-setuptools

After you installed it, run:

	easy_install biplist
	easy_install M2Crypto

**Certificate Generation**

We also need to generate certificates for`guzzoni.apple.com` or any other domain

	cd gen_certs
then

	./gen_certs.sh
or

	./gen_certs.sh 192.168.1.1
or

	./gen_certs.sh domain.com
this will generate a certifcaite for `guzzoni.apple.com`, `192.168.1.1` or `domain.com`

When you use Spire, just enter as address what ever parameter you supplied to `gen_certs.sh` e.g.:

	https://guzzoni.apple.com
or

	https://domain.com
or

	https://192.168.1.1

In case you don't have Spire or want to use `guzzoni.apple.com`
you need to setup a DNS spoofing or manipulate you hosts file

Please make sure to install the CA certificate on your iDevice (you can simply mail it to yourself).
It is the CA.pem file that was copied by gen_certs.sh to the servers root. 
In your mail, just click on the certificate and install it.

**Installing API Keys**


Some of the plugins included require API/APPID keys to use. You'll need to register with the respective websites to obtain these keys.

The general format is as follows:

	apiName="PLUGIN-API-KEY"

The apiName is usually printed in error messages when you miss a certain API Key.

***Where to obtain API Keys***

Register and sign up for an API with the following sites:

- Wolfram Alpha : [http://products.wolframalpha.com/developers/](http://products.wolframalpha.com/developers/)
- Wordnik : [http://developer.wordnik.com/](http://developer.wordnik.com/)
- Weather Wunderground : [http://www.wunderground.com/weather/api/](http://www.wunderground.com/weather/api/)

***Why don't you give me your key?***

The API (Application Programming Interface) keys are necessary to allow some plugins to use different services on the internet. Those api keys are like a username password combination and grant access to several resources online, like wolframalpha, they make it very easy to use the resources in a computer program. As you must buy a API key if you want to use it for multiple users or commercially (That are usually the terms for APIs) we cannot distribute the keys here in github and must require users to create them on their own, they are usually free for noncommercial and personal use.

**Running the server**

Now you are ready to go, start the server with:

	sudo python siriServer.py
Note: You need to run it as root, as we use https port 443
(non root can only use ports > 1024) for incomming connections.

**Running the server as a service**
For Ubuntu/Debian/...

1. Copy the script from startupScripts/siriserver to /etc/init.d "sudo cp startupScripts/siriserver /etc/init.d/siriserver"
2. Edit the script, fill in the path to your SiriServer folder "sudo nano /etc/init.d/siriserver"
3. Make executable "sudo chmod a+x /etc/init.d/siriserver"
4. Add it to the startup items: "sudo update-rc.d siriserver defaults"
5. Start with "sudo service siriserver start" You can now start, restart and stop SiriServer just as you started it in step 5.

For Mac

1. "sudo cp startupScripts/net.siriserver.plist /Library/LaunchDaemons"
2. "sudo launchctl load /Library/LaunchDaemons/net.siriserver.plist"

Common Errors
-------------
If we had the mid 90s this section would glow and sparkle to get your attention.
There are some errors that might occur even though you did everything that was written above...

**The server just crashes after a SpeechPacket**

You are running Linux right? Probably debian?
There is probably already a libspeex on your machine which is optimized for SSE2 which does not work with python (reason???)
Check if there is a `/usr/lib/sse2/libspeex.so.1`.

Option A: delete it (there should also be a version in /usr/lib if you installed via apt, or in /usr/local/lib if you compiled by hand)

Option B: ToDo

**This M2Crypto thing is not working**

Did you install all [dependencies](http://chandlerproject.org/Projects/MeTooCrypto#Requirements) of M2Crypto?

**I cannot get a connection from device to server**

Do you access your server over the internet? You need to setup your firewall and NAT to allow traffic for tcp port 443 directed to your server
Do you have a local firewall on the machine running the server? Also check if tcp port 443 is allowed for incomming connections


**There is an exception with something around a database lock**

	error: uncaptured python exception, closing channel <main.HandleConnection connected xxx.xxx.xxx.xxx:XXXX at 0xa65c368> (:database is locked
Solution: delete the .sqlite3 file and restart server

**There is something with SSL in the error**

Have you installed the ca.pem file on your phone? Do you have more than one CA certificate installed for the same domain?

=> Try deleting all certificates on the device and install the one created by gen_certs

Can I somehow verify the correct certificate? YES!

start siriServer.py, then take your ca.pem you think belongs to your servers certificate and run:

	 echo | openssl s_client -connect [DOMAIN]:443 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' | openssl verify -CAfile ca.pem 
Make sure to replace [DOMAIN] with the actual domain of the machine running siriServer.py (e.g. an IP address)
If your ca.pem matches your server certificate you should see `stdin: OK` as output!

OK, what else?
We can also setup a small test server using openssl to check if SSL is working (and to check if the iPhone correctly validates the server certificate):

	sudo openssl s_server -cert server.passless.crt -key server.passless.key -accept 443 -state
When you run this (siriServer should NOT run) it opens a basis server on port 443 using your servers certificate.

Now you can connect with your iPhone as if you would use Siri (of course Siri won't work, we are just testing the SSL layer)
It should output something like this, note the Ace http request near the end:

	 Using default temp DH parameters
	 Using default temp ECDH parameters  
	 ACCEPT
	 SSL_accept:before/accept initialization
	 SSL_accept:SSLv3 read client hello A
	 SSL_accept:SSLv3 write server hello A
	 SSL_accept:SSLv3 write certificate A
	 SSL_accept:SSLv3 write server done A
	 SSL_accept:SSLv3 flush data
	 SSL_accept:SSLv3 read client key exchange A
	 SSL_accept:SSLv3 read finished A
	 SSL_accept:SSLv3 write change cipher spec A
	 SSL_accept:SSLv3 write finished A
	 SSL_accept:SSLv3 flush data
	 -----BEGIN SSL SESSION PARAMETERS-----
	 MIGKAgEBAgIDAQQCAC8EIJ3DOw2nTgOAjdCNMqiFi+OmYU1fszwfH3jDk4q1P/mq
	 BDB7vM4nKFiGjLHpExNf4F1HZQ7ekRPaG/2X9EI/mqtpeWPp8vU1a/Em5JWomauK
	 jDShBgIETyr5oaIEAgIBLKQGBAQBAAAAphMEEWVob2VybmNoZW4uYXRoLmN4
	 -----END SSL SESSION PARAMETERS-----
 	 Shared ciphers:ECDHE-ECDSA-AES256-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-ECDSA-RC4-SHA:ECDHE-      ECDSA-DES-CBC3-SHA:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-RC4-SHA:ECDHE-RSA-DES-CBC3-SHA:ECDH-ECDSA-AES128-SHA:ECDH-ECDSA-AES256-SHA:ECDH-ECDSA-RC4-SHA:ECDH-ECDSA-DES-CBC3-SHA:ECDH-RSA-AES128-SHA:ECDH-RSA-AES256-SHA:ECDH-RSA-RC4-SHA:ECDH-RSA-DES-CBC3-   SHA:AES128-SHA:RC4-SHA:RC4-MD5:AES256-SHA:DES-CBC3-SHA:DHE-RSA-AES128-SHA:DHE-RSA-AES256-  SHA:EDH-RSA-DES-CBC3-SHA
	 CIPHER is AES128-SHA
	 Secure Renegotiation IS supported
	 ACE /ace HTTP/1.0
	 Host: DOMAIN REMOVED
	 User-Agent: Assistant(iPhone/iPhone3,1; iPhone OS/5.0.1/9A405) Ace/1.0
	 Content-Length: 2000000000

AIDE
-----
Si vous avez suivi toutes les étapes de l'installation et que vous avez encore besoin d'aide pour faire fonctionner SiriServer, rejoignez #SiriServer sur Freenode (IRC).

Remerciements
--------------
Un grand merci à [Applidium](http://applidium.com/en/news/cracking_siri/) et aussi à [plamoni](https://github.com/plamoni/SiriProxy/) pour SiriProxy, ainsi qu'à [Eichhoernchen](https://github.com/Eichhoernchen/SiriServer) qui a créé SiriServer.
Merci également à tous ceux qui ont contribué au code ou apportés des idées.

Licence
---------
C'est un logiciel libre. SiriServer a été créé par [Eichhoernchen](https://github.com/Eichhoernchen/SiriServer), qui a distribué son travail sous licence [Creative Commons Attribution-NonCommercial-ShareAlike 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.fr) et par conséquent, cette adaptation en français vous est livrée sous la même licence.
Vous pouvez faire ce que vous voulez de ce logiciel, mais vous n'êtes pas autorisé à le vendre, à vous l'attribuer ou à le partager sous une licence non identique ou similaire à celle-ci.

Disclaimer
----------
Apple détient tous les droits sur Siri. Personne ne fournit de garantie de fonctionnement ou de support pour ce logiciel. Utilisez le comme il est.
