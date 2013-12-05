DROP DATABASE scsi;
CREATE DATABASE scsi;
USE scsi;

CREATE TABLE `adusr` (
  `adusrusrn` varchar(15) NOT NULL DEFAULT '',
  `adusrnomb` varchar(45) NOT NULL,
  `adusrmail` varchar(80) DEFAULT NULL,
  `adusradmn` smallint(6) DEFAULT NULL,
  `adusrclav` varchar(45) DEFAULT NULL,
  `adusrstat` smallint(1) DEFAULT NULL,
  `adusruser` varchar(15) DEFAULT NULL,
  `adusrhora` varchar(8) DEFAULT NULL,
  `adusrfpro` date DEFAULT NULL,
  `adusrflog` date DEFAULT NULL,
  `adusrhlog` varchar(8) DEFAULT NULL,
  `adusrfcla` date DEFAULT NULL,
  `adusrmrcb` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`adusrusrn`),
  UNIQUE KEY `adusrusrn_UNIQUE` (`adusrusrn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `cookie` (
  `cookcoid` varchar(50) NOT NULL,
  `cookuser` varchar(15) NOT NULL,
  `cookfpro` date NOT NULL,
  `cookaddr` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cookcoid`),
  UNIQUE KEY `cookcoid_UNIQUE` (`cookcoid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `grupo` (
  `grupongrp` int(7) NOT NULL,
  `grupodesc` varchar(100) NOT NULL,
  `grupouplo` decimal(10,2) NOT NULL,
  `grupodown` decimal(10,2) NOT NULL,
  `grupouser` varchar(3) NOT NULL,
  `grupofreg` date DEFAULT NULL,
  `grupofpro` date DEFAULT NULL,
  `grupohora` varchar(8) DEFAULT NULL,
  `grupomrcb` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`grupongrp`),
  UNIQUE KEY `grupongrp_UNIQUE` (`grupongrp`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `lista` (
  `listandip` smallint(6) NOT NULL,
  `listadesc` varchar(100) NOT NULL,
  `listadiip` varchar(13) NOT NULL,
  `listadmac` varchar(18) NOT NULL,
  `listangrp` smallint(6) NOT NULL,
  `listauser` varchar(15) NOT NULL,
  `listafreg` date DEFAULT NULL,
  `listafpro` date DEFAULT NULL,
  `listahora` varchar(8) DEFAULT NULL,
  `listamrcb` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`listandip`),
  UNIQUE KEY `listandip_UNIQUE` (`listandip`),
  UNIQUE KEY `listadiip_UNIQUE` (`listadiip`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `mdlos` (
  `mdlosnmod` int(11) NOT NULL AUTO_INCREMENT,
  `mdlosnomb` varchar(10) NOT NULL,
  `mdlosdesc` varchar(100) NOT NULL,
  `mdlosstat` int(1) NOT NULL,
  `mdlosuser` varchar(15) NOT NULL,
  `mdlosfreg` date DEFAULT NULL,
  `mdlosfpro` date DEFAULT NULL,
  `mdloshora` varchar(8) DEFAULT NULL,
  `mdlosmrcb` smallint(1) DEFAULT NULL,
  PRIMARY KEY (`mdlosnmod`),
  UNIQUE KEY `mdlosnmod_UNIQUE` (`mdlosnmod`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

CREATE TABLE `scmdt` (
  `scmdtnmod` decimal(2,0) DEFAULT NULL,
  `scmdtcorr` decimal(2,0) DEFAULT NULL,
  `scmdtdesc` char(35) DEFAULT NULL,
  `scmdtruta` char(100) DEFAULT NULL,
  `scmdtstat` decimal(1,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `scmod` (
  `scmodnmod` decimal(2,0) DEFAULT NULL,
  `scmoddesc` char(35) DEFAULT NULL,
  `scmodstat` decimal(1,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `scmop` (
  `scmopnmod` decimal(2,0) DEFAULT NULL,
  `scmopcorr` decimal(2,0) DEFAULT NULL,
  `scmopusrn` char(3) DEFAULT NULL,
  `scmopfpro` date DEFAULT NULL,
  `scmophora` char(8) DEFAULT NULL,
  `scmopuser` varchar(15) DEFAULT NULL,
  `scmopmrcb` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `adlog` (
  `adlognlog` integer(11) NOT NULL AUTO_INCREMENT,
  `adlogdesc` varchar(45) NOT NULL,
  `adloguser` varchar(15) NOT NULL,
  `adlogfpro` date NOT NULL,  
  `adloghora` varchar(8) NOT NULL,
  PRIMARY KEY (`adlognlog`),
  UNIQUE KEY `adlognlog_UNIQUE` (`adlognlog`)
) ;

/*Valores predeterminados*/
LOCK TABLES `adusr` WRITE;
INSERT INTO `adusr` VALUES ('admin','Administrador','admin@scsi',1,'d02a1c7defa7f13792975edc1204bd99',1,'admin','23:50:5','2013-09-17','','','2013-09-17',0);
UNLOCK TABLES;

LOCK TABLES `scmod` WRITE;
INSERT INTO `scmod` VALUES (1,'Administrador',0),(2,'Squid',0),(3,'SquidGuard',0),(4,'Monitoreo',0),(5,'IPTables',0);
UNLOCK TABLES;

LOCK TABLES `mdlos` WRITE;
INSERT INTO `mdlos` VALUES (1,'Squid','Squid Module',1,'gsa','2013-03-21','2013-03-21',' 0:5:8 ',0),(15,'IPTables','IPTables',1,'gsa','2013-04-18','2013-04-18',' 21:23:7',9),(16,'SquidGuard','SquidGuard',1,'gsa','2013-04-18','2013-04-18',' 22:6:16',0);
UNLOCK TABLES;

LOCK TABLES `scmdt` WRITE;
INSERT INTO `scmdt` VALUES (1,1,'Registrar Usuarios','Core/Admin/RegistrarUsuario/',0),(1,2,'Recuperar Clave','Core/Admin/RecuperarClave/',0),(1,3,'Adm. Modulos','Core/Admin/Menu/',0),(2,1,'Adm. Listas','Modulos/Squid/squid_administrar_listas.cgi',0),(2,2,'Adm.Bloqueo','Modulos/Squid/squid_bloqueo.cgi',0),(2,3,'Man.Delay','Modulos/Squid/squid_delay_pools.cgi',0),(2,4,'General','Modulos/Squid/squid_general.cgi',0),(2,5,'Config. Manual','Modulos/Squid/squid_general_m.cgi?filename=/etc/squid/squid.conf',0),(2,6,'Listas IP','Modulos/Squid/squid_lista_ips.cgi',0),(2,7,'Param. SquidGuard','Modulos/Squid/squid_squidguard.cgi',9),(3,1,'IP Administradores','Modulos/SquidGuard/squidguard_admin_ip.cgi',0),(3,2,'Param. General','Modulos/SquidGuard/squidguard_general.cgi',0),(3,3,'Config. Manual','Modulos/SquidGuard/squidguard_general_m.cgi?filename=/etc/squid/squidGuard.conf',0),(4,1,'Monitoreo','Modulos/Graph',0),(4,2,'Frecuentes','Modulos/Graph/frecuentes.cgi',0),(4,3,'Consumo por IP','Modulos/Graph/banda.cgi',0),(5,1,'Parametros','Modulos/IPTables/iptables_param.cgi',0),(5,2,'Bloqueo HTTPS','Modulos/IPTables/iptables_https.cgi',0),(6,1,'Reporte de usuarios','Modulos/Reportes/usuarios1.cgi',0),(1,4,'Alta/Baja Usuarios','Core/Admin/AltaBaja/',0),(6,2,'General del Logs','Modulos/Reportes/log.cgi',0),(6,3,'Usuarios Inactivos','Modulos/Reportes/usuarios9.cgi',0),(6,4,'Excepciones HTTPS','Modulos/Reportes/ips_https.cgi',0),(6,5,'Dominios bloqueados HTTPS','Modulos/Reportes/dom_https.cgi',0),(6,6,'Sitios Frecuentes','Modulos/Reportes/sitios_frecuentes.cgi',0),(6,7,'Consupo por IP','Modulos/Reportes/consumoip.cgi',0),(6,8,'Excepciones SquidGuard','Modulos/Reportes/admin_squidguard.cgi',0);
UNLOCK TABLES;
