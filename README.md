SCSI
==================================
Requerimientos:
	- Perl
	- Apache con soporte CGI
	- Squid o squid3
	- Navegador WEB
        - libapache2-mod-perl2
        - libmime-lite-perl
        - sendmail o sendmail-bin
        - libemail-valid-perl
        - libjson-any-perl
        - mysql-server-5.5
        - bind9
        - iptables

Puede instalarse de la siguiente forma:
    apt-get install bind9 libpdf-table-perl libapache2-mod-perl2 apache2 libmime-lite-perl sendmail-bin libemail-valid-perl libjson-any-perl mysql-server-5.5

Opcional:
	- squidguard
          apt-get install squidguard

=====================INSTALAR SQUIDGUARD====================

1. apt-get install squidguad
2. crear la base de datos de listas negras
    cd /var/lib/squidguard/db/
    wget -c http://squidguard.mesd.k12.or.us/blacklists.tgz
    tar xvzf blacklists.tgz
    chmod -R 777 blacklists
3. copiar el archivo squidGuard.conf incluido en este programa a:
    cp squidGuard.conf /etc/squid/squidGuard.conf
    chmod 770 /etc/squid/squidGuard.conf
4. construir la base de datos de bloqueos con:
    squidGuard -b -C all -c /etc/squid/squidGuard.conf
5. SquidGuard listo para funcionar con SCSI

============================================================
PROCEDIMIENTO DE INSTALACIÓN SCSI
============================================================

1.Configurar los MIME Tipes
	1. Modificar el archivo /etc/apache2/mods-enabled/mime.conf
	Especificamente descomentar:
            #AddHandler cgi-script .cgi
	a	
            AddHandler cgi-script .cgi .pl
	Luego 
            a2enmod cgi
            service apache2 restart
            
2.Configurar Apache 2 
    a) Debian 6 y 7
	1. Crear un archivo de apache en /etc/apache2/sites-available/
            o simplemente edite el archivo default
	2. Archivo con el nombre deseado con el siguiente contenido:
        <VirtualHost *:80>
        ServerAdmin gary@sandi.com
        DocumentRoot /scsi/scsi
        <Directory />
                Options FollowSymLinks
                AllowOverride None
        </Directory>
        <Directory /scsi/scsi>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>
        ScriptAlias /scsi/scsi /scsi/scsi
        <Directory "/scsi/scsi">
                AllowOverride All
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                Order allow,deny
                Allow from all
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>
    4. /etc/init.d/apache2 restart
    
    b) Debian 8
        1. Crear un archivo de apache en /etc/apache2/sites-available/
            o simplemente edite el archivo 000-default.conf
	2. Archivo con el nombre deseado con el siguiente contenido:
        <VirtualHost *:80>
        #ServerName www.example.com

        ServerAdmin gary@sandi-ti.com
        DocumentRoot /scsi/scsi
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>

        3. Edite el archivo /etc/apache2/apache2.conf
           en la zona de directorios añada:
            <Directory /scsi/scsi>
            AllowOverride All
            Options Indexes FollowSymLinks MultiViews
            Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
            Order allow,deny
            Allow from all
            </Directory>    
        4. /etc/init.d/apache2 restart
           

3. Extraer scsi
	1. Obtenga el src en .tar.gz desde la web del proyecto scsi.sf.net
	2. Cambiar permisos del directorio:
		chown www-data:www-data /scsi/scsi -R
		chmod 777 /scsi/scsi -R

4. Compilación previa. (Ejecutar como root)
    cd Tools/bin/
    sh RUN_AS_ROOT.sh

5. Base de datos ingresar con mysql -u root -p :
    Crear usuario con:

    CREATE USER scsi@localhost IDENTIFIED BY 'scsi';
    GRANT ALL PRIVILEGES ON scsi.* TO scsi@'localhost' IDENTIFIED BY 'scsi';
    FLUSH PRIVILEGES;

    Subir la base de datos estandar ejecutando el script scsi.sql:
    mysql -u root -p < scsi_clean.sql 

6. Configurar scsi.
	1. En consola
		1. Ir al directorio del scsi.
		2. nano configuracion.pm modificar los parametros
		3. Debe crear el directorio /scsi para como ruta de trabajo
			mkdir /scsi
		   Otorgar los permisos 777 solamente a ese directorio
		   Asi tambien cambiar el propietario
		   	chmod 777 /scsi
		   	chown www-data:www-data /scsi -R
		
7. Interfase WEB.
        1. En un navegador WEB http://localhost/scsi/index.cgi (o la ruta pre-elegida)
        2. El usuario por defecto es admin y el password es admin
		
8.Configurar Squid.
	1. Verifique que squid esta instalado
	2. Edite el archivo de configuracion /etc/squid/squid.conf
	   añada "### SCSI_START ###" sin las comillas.
	3. Otorgue los permisos de read/write al archivo /etc/squid/squid.conf
	4. Otorgue el permiso chmod +s /usr/sbin/squid
	
9. Uso de scsi.
	1. El uso es intuitivo y simple.
