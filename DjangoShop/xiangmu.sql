/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.6.23-log : Database - xiangmu
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`xiangmu` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `xiangmu`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add users',7,'add_users'),(20,'Can change users',7,'change_users'),(21,'Can delete users',7,'delete_users'),(22,'Can add types',8,'add_types'),(23,'Can change types',8,'change_types'),(24,'Can delete types',8,'delete_types'),(25,'Can add goods',9,'add_goods'),(26,'Can change goods',9,'change_goods'),(27,'Can delete goods',9,'delete_goods'),(28,'Can add users',10,'add_users'),(29,'Can change users',10,'change_users'),(30,'Can delete users',10,'delete_users'),(31,'Can add types',11,'add_types'),(32,'Can change types',11,'change_types'),(33,'Can delete types',11,'delete_types'),(34,'Can add goods',12,'add_goods'),(35,'Can change goods',12,'change_goods'),(36,'Can delete goods',12,'delete_goods');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `detail` */

DROP TABLE IF EXISTS `detail`;

CREATE TABLE `detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) DEFAULT NULL,
  `goodsid` int(11) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `detail` */

insert  into `detail`(`id`,`orderid`,`goodsid`,`name`,`price`,`num`) values (23,16,22,'牛顿',123.00,3),(22,16,21,'爱迪生',666.00,1);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'myadmin','users'),(8,'myadmin','types'),(9,'myadmin','goods'),(10,'myweb','users'),(11,'myweb','types'),(12,'myweb','goods');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-09-29 11:37:09.702238'),(2,'auth','0001_initial','2017-09-29 11:37:10.018238'),(3,'admin','0001_initial','2017-09-29 11:37:10.113291'),(4,'admin','0002_logentry_remove_auto_add','2017-09-29 11:37:10.159239'),(5,'contenttypes','0002_remove_content_type_name','2017-09-29 11:37:10.227473'),(6,'auth','0002_alter_permission_name_max_length','2017-09-29 11:37:10.236528'),(7,'auth','0003_alter_user_email_max_length','2017-09-29 11:37:10.282487'),(8,'auth','0004_alter_user_username_opts','2017-09-29 11:37:10.292258'),(9,'auth','0005_alter_user_last_login_null','2017-09-29 11:37:10.330015'),(10,'auth','0006_require_contenttypes_0002','2017-09-29 11:37:10.331932'),(11,'auth','0007_alter_validators_add_error_messages','2017-09-29 11:37:10.342989'),(12,'auth','0008_alter_user_username_max_length','2017-09-29 11:37:10.372837'),(13,'sessions','0001_initial','2017-09-29 11:37:10.386326');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('rt5sfmywnpu443ycoy77q5dgnxx6txk0','Nzk3N2IyNTVlOGJiYjg0YTQ1ZWE1YjFiZTUwNThhODkzNTE5ZWJjMjp7InZlcmlmeWNvZGUiOiJKVlo4IiwiYWRtaW51c2VyIjoiXHU3YmExXHU3NDA2XHU1NDU4Iiwic2hvcGxpc3QiOnt9LCJ1c2VyIjoiXHU1ZjIwXHU0ZTA5IiwiemlkIjoyOCwiYWRkcmVzcyI6Ilx1NTMxN1x1NGVhYyIsInBob25lIjoiMTU1MTg4OTUxOTMiLCJ2aXB1c2VyIjp7ImlkIjoyOCwidXNlcm5hbWUiOiIxNTUxODg5NTE5MyIsIm5hbWUiOiJcdTVmMjBcdTRlMDkiLCJhZGRyZXNzIjoiXHU1MzE3XHU0ZWFjIiwicGhvbmUiOiI2NjY2NjY2In0sInhuYW1lIjoiXHU1ZjIwXHU0ZTA5IiwieHBob25lIjoiMTU1MTg4OTUxOTMiLCJ4YWRkcmVzcyI6Ilx1NGUwYVx1NmQ3NyJ9','2017-10-18 13:37:30.791706');

/*Table structure for table `goods` */

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) DEFAULT NULL,
  `goods` varchar(32) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `descr` text,
  `price` double(6,2) DEFAULT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `state` tinyint(1) DEFAULT '1',
  `store` int(11) DEFAULT '0',
  `num` int(11) DEFAULT '0',
  `clicknum` int(11) DEFAULT '0',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `goods` */

insert  into `goods`(`id`,`typeid`,`goods`,`company`,`descr`,`price`,`picname`,`state`,`store`,`num`,`clicknum`,`addtime`) values (23,4,'哈时间的','阿萨德','阿萨德    ',20.00,'1507124104.8689804.jpg',1,10,0,0,1507124104),(21,6,'爱迪生','美国','没什么好解释的        ',666.00,'1507104621.9613175.jpg',1,222,0,1,1507104621),(22,10,'牛顿','美国','万有引力    ',123.00,'1507104697.8226473.jpg',1,132,0,3,1507104697),(20,3,'哥白尼','法国','没什么好说的          ',233.00,'1507104591.7447467.jpg',1,233,0,2,1507104591);

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `linkman` varchar(32) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `addtime` int(11) DEFAULT NULL,
  `total` double(8,2) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Data for the table `orders` */

insert  into `orders`(`id`,`uid`,`linkman`,`address`,`code`,`phone`,`addtime`,`total`,`status`) values (16,28,'张三','上海','','15518895193',1507124250,1035.00,2);

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) DEFAULT '0',
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `type` */

insert  into `type`(`id`,`name`,`pid`,`path`) values (1,'服装',0,'0,'),(2,'男装',1,'0,1,'),(3,'女装',1,'0,1,'),(4,'童装',1,'0,1,'),(5,'食品',0,'0,'),(6,'主食',5,'0,5,'),(7,'零食',5,'0,5,'),(8,'电子产品',0,'0,'),(9,'手机',8,'0,8,'),(10,'电脑',8,'0,8,'),(11,'相机',8,'0,8,');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) NOT NULL,
  `sex` tinyint(1) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `state` tinyint(1) DEFAULT '1',
  `addtime` int(11) DEFAULT NULL,
  `password` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `NewIndex1` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`name`,`sex`,`address`,`code`,`phone`,`email`,`state`,`addtime`,`password`) values (2,'wzz','管理员',1,'sd','sfgg','3456','cvxb',0,NULL,'e10adc3949ba59abbe56e057f20f883e'),(27,'17611393735','17611393735',1,'','','','',1,NULL,'4e2bc9cdbdd73ed6c7c0f61f64abb5d9'),(28,'15518895193','张三',1,'上海','16515','123','1337009726@163.com',1,NULL,'202cb962ac59075b964b07152d234b70');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
