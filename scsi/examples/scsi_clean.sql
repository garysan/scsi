-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: scsi
-- ------------------------------------------------------
-- Server version	5.5.31-0+wheezy1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adlog`
--

DROP TABLE IF EXISTS `adlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adlog` (
  `adlognlog` int(11) NOT NULL AUTO_INCREMENT,
  `adlogdesc` varchar(45) NOT NULL,
  `adloguser` varchar(15) NOT NULL,
  `adlogfpro` date NOT NULL,
  `adloghora` varchar(8) NOT NULL,
  PRIMARY KEY (`adlognlog`),
  UNIQUE KEY `adlognlog_UNIQUE` (`adlognlog`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adlog`
--

--
-- Table structure for table `adusr`
--

DROP TABLE IF EXISTS `adusr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adusr`
--

LOCK TABLES `adusr` WRITE;
/*!40000 ALTER TABLE `adusr` DISABLE KEYS */;
INSERT INTO `adusr` VALUES ('admin','Administrador','admin@scsi',1,'d02a1c7defa7f13792975edc1204bd99',1,'admin','23:50:5','2013-09-17','2013-11-28','9:2:10','2013-09-17',0);
/*!40000 ALTER TABLE `adusr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cookie`
--

DROP TABLE IF EXISTS `cookie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cookie` (
  `cookcoid` varchar(50) NOT NULL,
  `cookuser` varchar(15) NOT NULL,
  `cookfpro` date NOT NULL,
  `cookaddr` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cookcoid`),
  UNIQUE KEY `cookcoid_UNIQUE` (`cookcoid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cookie`
--

LOCK TABLES `cookie` WRITE;
/*!40000 ALTER TABLE `cookie` DISABLE KEYS */;
INSERT INTO `cookie` VALUES ('rfIeZAlzoyoVgr93jIdQKgM9fzw4rsFF','fsandi','2013-11-27','190.129.12.210');
/*!40000 ALTER TABLE `cookie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupo`
--

DROP TABLE IF EXISTS `grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lista`
--

DROP TABLE IF EXISTS `lista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista`
--

LOCK TABLES `lista` WRITE;
/*!40000 ALTER TABLE `lista` DISABLE KEYS */;
/*!40000 ALTER TABLE `lista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mdlos`
--

DROP TABLE IF EXISTS `mdlos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mdlos`
--

LOCK TABLES `mdlos` WRITE;
/*!40000 ALTER TABLE `mdlos` DISABLE KEYS */;
INSERT INTO `mdlos` VALUES (1,'Squid','Squid Module',1,'gsa','2013-03-21','2013-03-21',' 0:5:8 ',0),(15,'IPTables','IPTables',1,'gsa','2013-04-18','2013-04-18',' 21:23:7',9),(16,'SquidGuard','SquidGuard',1,'gsa','2013-04-18','2013-04-18',' 22:6:16',0);
/*!40000 ALTER TABLE `mdlos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scmdt`
--

DROP TABLE IF EXISTS `scmdt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scmdt` (
  `scmdtnmod` decimal(2,0) DEFAULT NULL,
  `scmdtcorr` decimal(2,0) DEFAULT NULL,
  `scmdtdesc` char(35) DEFAULT NULL,
  `scmdtruta` char(100) DEFAULT NULL,
  `scmdtstat` decimal(1,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scmdt`
--

LOCK TABLES `scmdt` WRITE;
/*!40000 ALTER TABLE `scmdt` DISABLE KEYS */;
INSERT INTO `scmdt` VALUES (1,1,'Registrar Usuarios','Core/Admin/RegistrarUsuario/',0),(1,2,'Recuperar Clave','Core/Admin/RecuperarClave/',0),(1,3,'Adm. Modulos','Core/Admin/Menu/',0),(2,1,'Adm. Listas','Modulos/Squid/squid_administrar_listas.cgi',0),(2,2,'Adm.Bloqueo','Modulos/Squid/squid_bloqueo.cgi',0),(2,3,'Man.Delay','Modulos/Squid/squid_delay_pools.cgi',0),(2,4,'General','Modulos/Squid/squid_general.cgi',0),(2,5,'Config. Manual','Modulos/Squid/squid_general_m.cgi?filename=/etc/squid/squid.conf',0),(2,6,'Listas IP','Modulos/Squid/squid_lista_ips.cgi',0),(2,7,'Param. SquidGuard','Modulos/Squid/squid_squidguard.cgi',9),(3,1,'IP Administradores','Modulos/SquidGuard/squidguard_admin_ip.cgi',0),(3,2,'Param. General','Modulos/SquidGuard/squidguard_general.cgi',0),(3,3,'Config. Manual','Modulos/SquidGuard/squidguard_general_m.cgi?filename=/etc/squid/squidGuard.conf',0),(4,1,'Monitoreo','Modulos/Graph',0),(4,2,'Frecuentes','Modulos/Graph/frecuentes.cgi',0),(4,3,'Consumo por IP','Modulos/Graph/banda.cgi',0),(5,1,'Parametros','Modulos/IPTables/iptables_param.cgi',0),(5,2,'Bloqueo HTTPS','Modulos/IPTables/iptables_https.cgi',0),(6,1,'Reporte de usuarios','Modulos/Reportes/usuarios1.cgi',0),(1,4,'Alta/Baja Usuarios','Core/Admin/AltaBaja/',0),(6,2,'General del Logs','Modulos/Reportes/log.cgi',0),(6,3,'Usuarios Inactivos','Modulos/Reportes/usuarios9.cgi',0),(6,4,'Excepciones HTTPS','Modulos/Reportes/ips_https.cgi',0),(6,5,'Dominios bloqueados HTTPS','Modulos/Reportes/dom_https.cgi',0),(6,6,'Sitios Frecuentes','Modulos/Reportes/sitios_frecuentes.cgi',0),(6,7,'Consupo por IP','Modulos/Reportes/consumoip.cgi',0),(6,8,'Excepciones SquidGuard','Modulos/Reportes/admin_squidguard.cgi',0);
/*!40000 ALTER TABLE `scmdt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scmod`
--

DROP TABLE IF EXISTS `scmod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scmod` (
  `scmodnmod` decimal(2,0) DEFAULT NULL,
  `scmoddesc` char(35) DEFAULT NULL,
  `scmodstat` decimal(1,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scmod`
--

LOCK TABLES `scmod` WRITE;
/*!40000 ALTER TABLE `scmod` DISABLE KEYS */;
INSERT INTO `scmod` VALUES (1,'Administrador',0),(2,'Squid',0),(3,'SquidGuard',0),(4,'Monitoreo',0),(5,'IPTables',0),(6,'Reportes',0);
/*!40000 ALTER TABLE `scmod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scmop`
--

DROP TABLE IF EXISTS `scmop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scmop` (
  `scmopnmod` decimal(2,0) DEFAULT NULL,
  `scmopcorr` decimal(2,0) DEFAULT NULL,
  `scmopusrn` char(3) DEFAULT NULL,
  `scmopfpro` date DEFAULT NULL,
  `scmophora` char(8) DEFAULT NULL,
  `scmopuser` varchar(15) DEFAULT NULL,
  `scmopmrcb` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scmop`
--

LOCK TABLES `scmop` WRITE;
/*!40000 ALTER TABLE `scmop` DISABLE KEYS */;
/*!40000 ALTER TABLE `scmop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-11-28 18:05:12
