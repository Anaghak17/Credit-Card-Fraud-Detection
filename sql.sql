/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - frauddetection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`frauddetection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `frauddetection`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT 'add_to_cart',
  `payment_methods` varchar(20) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`bid`,`userid`,`status`,`payment_methods`,`amount`) values (1,7,'booked','Online','134.0'),(2,7,'booked','Online','134.0'),(10,7,'booked','pending','134.0');

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `card_no` int(11) DEFAULT NULL,
  `cvv` int(11) DEFAULT NULL,
  `expiry` varchar(20) DEFAULT NULL,
  `holder` varchar(20) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `card` */

insert  into `card`(`cid`,`uid`,`card_no`,`cvv`,`expiry`,`holder`,`amount`) values (1,7,2147483647,122,'12-09-2022','ANU','8829'),(2,7,12253333,345,'12-09-2022','TOM','500'),(3,7,142533666,122,'12-02-20222','ANU','4812'),(4,15,2147483647,199,'12-09-2023','simi','82984'),(5,2,2147483647,988,'12-08-2024','john','46277');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cartid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(20) DEFAULT NULL,
  `bid` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`cartid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cartid`,`pid`,`bid`,`quantity`) values (1,1,1,2),(2,4,2,2),(3,6,3,2),(4,4,4,15),(5,1,5,3),(6,1,6,3),(7,4,7,2),(8,1,8,2),(9,1,9,2),(10,1,10,2);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `cmid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(20) DEFAULT NULL,
  `complaint` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `reply` varchar(20) DEFAULT NULL,
  `replydate` date DEFAULT NULL,
  PRIMARY KEY (`cmid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`cmid`,`userid`,`complaint`,`date`,`pid`,`reply`,`replydate`) values (1,'7','Bad product','2022-06-05',1,'We are resend good o','2022-06-05'),(2,'7','Not Good Quality','2022-06-05',1,'pending','0000-00-00');

/*Table structure for table `dealer` */

DROP TABLE IF EXISTS `dealer`;

CREATE TABLE `dealer` (
  `did` int(11) DEFAULT NULL,
  `dealer` varchar(20) DEFAULT NULL,
  `shope` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dealer` */

insert  into `dealer`(`did`,`dealer`,`shope`,`place`,`district`,`phone`) values (4,'TOM','Tea shop','Pala','Kottayam','9858693625'),(9,'TOM','Tea shop','KANNUR','Kannur','8909878889'),(13,'Kiran','Kiran Restaurant','Thalassery','Kannur','9785635825'),(14,'TOM','Tea shop','KANNUR','Kannur','9684125365');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `feedback` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`uid`,`feedback`,`date`) values (1,7,'Good Service','2022-06-05');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'john1@gmail.com','john','user'),(3,'anu23@gmail.com','anu','user'),(4,'TOM','7566','dealer'),(5,'sam','7164','dealer'),(6,'aa','2416','dealer'),(7,'tom90@gmail.com','tom','user'),(8,'tom90@gmail.com','tom','user'),(9,'TOM','8143','dealer'),(10,'anu28@gmail.com','Anagha','user'),(11,'Sanju','4426','dealer'),(12,'robin@gmail.com','robin','user'),(13,'Kiran','5590','dealer'),(14,'TOM','3861','dealer'),(15,'simi@gmail.com','simi','user');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(20) DEFAULT NULL,
  `pname` varchar(20) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `stock` varchar(20) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  `did` int(11) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`pid`,`category`,`pname`,`price`,`stock`,`image`,`did`) values (1,'Fruits','mango',67,'-31','/static/pic/220605-211830.jpg',4),(4,'Vegitables','Broccoli',67,'-168','/static/pic/220605-212247.jpg',4),(6,'Fruits','Apple',100,'23','/static/pic/220606-210341.jpg',4),(7,'Fruits','Potato',50,'2000','/static/pic/220618-140040.jpg',5),(8,'Fruits','Apple',200,'400','/static/pic/220618-140125.jpg',5),(9,'Vegitables','laddyfinger',60,'400','/static/pic/220618-140213.jpg',5);

/*Table structure for table `transaction` */

DROP TABLE IF EXISTS `transaction`;

CREATE TABLE `transaction` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_id` int(11) NOT NULL,
  `date` varchar(10) NOT NULL,
  `time` varchar(10) NOT NULL,
  `finished` varchar(20) NOT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `transaction` */

insert  into `transaction`(`transaction_id`,`bill_id`,`date`,`time`,`finished`) values (1,1,'2022-06-18','15:34:24','success'),(2,2,'2022-06-18','15:35:57','success'),(7,1,'2022-06-18','16:17:58','fake');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `housename` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`name`,`housename`,`place`,`post`,`district`,`phone`) values (7,'Tom','Green villa','payyanur','Thalassery','Kannur','8757876555'),(8,'Tom','Green villa','payyanur','Thalassery','Kannur','8757876555'),(10,'Anagha','Seashore','payyanur','payyanur','Kannur','9087675655'),(12,'Robin','Yellow hut','kanjagad','Kanjagad','Kasargod','8909878889'),(15,'SIMI','Green villa','panoor','panoor','Kannur','9785263525');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
