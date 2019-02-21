-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.37-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for kumparan
DROP DATABASE IF EXISTS `kumparan`;
CREATE DATABASE IF NOT EXISTS `kumparan` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `kumparan`;

-- Dumping structure for table kumparan.tbl_details
DROP TABLE IF EXISTS `tbl_details`;
CREATE TABLE IF NOT EXISTS `tbl_details` (
  `news_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  PRIMARY KEY (`news_id`,`topic_id`),
  KEY `fk_details_topics1` (`topic_id`),
  KEY `fk_details_news1` (`news_id`),
  CONSTRAINT `fk_details_news1` FOREIGN KEY (`news_id`) REFERENCES `tbl_news` (`news_Id`),
  CONSTRAINT `fk_details_topics1` FOREIGN KEY (`topic_id`) REFERENCES `tbl_topics` (`topic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_details: ~3 rows (approximately)
/*!40000 ALTER TABLE `tbl_details` DISABLE KEYS */;
INSERT INTO `tbl_details` (`news_id`, `topic_id`) VALUES
	(1, 1),
	(1, 2),
	(1, 3),
	(2, 1);
/*!40000 ALTER TABLE `tbl_details` ENABLE KEYS */;

-- Dumping structure for table kumparan.tbl_news
DROP TABLE IF EXISTS `tbl_news`;
CREATE TABLE IF NOT EXISTS `tbl_news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `status_id` tinyint(2) NOT NULL DEFAULT '1',
  `title` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`news_id`),
  UNIQUE KEY `title` (`title`),
  KEY `fk_news_news_status1` (`status_id`),
  CONSTRAINT `fk_news_news_status1` FOREIGN KEY (`status_id`) REFERENCES `tbl_news_status` (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_news: ~3 rows (approximately)
/*!40000 ALTER TABLE `tbl_news` DISABLE KEYS */;
INSERT INTO `tbl_news` (`news_id`, `status_id`, `title`, `content`, `created_date`, `modified_date`) VALUES
	(1, 1, 'Judul 1a', 'Isi Konten Judul 5', '2019-02-19 21:42:00', '2019-02-22 03:49:29'),
	(2, 1, 'Judul 2', 'pasca debat masih panas', '2019-02-19 21:42:00', '2019-02-22 02:24:12'),
	(4, 1, 'Judul 3', 'Isi Konten Judul 3', '2019-02-22 03:04:10', NULL);
/*!40000 ALTER TABLE `tbl_news` ENABLE KEYS */;

-- Dumping structure for table kumparan.tbl_news_status
DROP TABLE IF EXISTS `tbl_news_status`;
CREATE TABLE IF NOT EXISTS `tbl_news_status` (
  `status_id` tinyint(2) NOT NULL AUTO_INCREMENT,
  `news_status` varchar(20) NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_news_status: ~3 rows (approximately)
/*!40000 ALTER TABLE `tbl_news_status` DISABLE KEYS */;
INSERT INTO `tbl_news_status` (`status_id`, `news_status`, `created_date`) VALUES
	(1, 'Draft', '2019-02-19 21:49:06'),
	(2, 'Publish', '2019-02-19 21:49:06'),
	(3, 'Deleted', '2019-02-19 21:49:06');
/*!40000 ALTER TABLE `tbl_news_status` ENABLE KEYS */;

-- Dumping structure for table kumparan.tbl_topics
DROP TABLE IF EXISTS `tbl_topics`;
CREATE TABLE IF NOT EXISTS `tbl_topics` (
  `topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(50) DEFAULT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_topics: ~3 rows (approximately)
/*!40000 ALTER TABLE `tbl_topics` DISABLE KEYS */;
INSERT INTO `tbl_topics` (`topic_id`, `topic`, `created_date`, `modified_date`) VALUES
	(1, 'pilpres', '2019-02-19 21:48:38', NULL),
	(2, 'politik', '2019-02-19 21:48:38', NULL),
	(3, 'pemilu', '2019-02-19 21:48:38', NULL);
/*!40000 ALTER TABLE `tbl_topics` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
