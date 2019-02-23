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
CREATE DATABASE IF NOT EXISTS `kumparan` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `kumparan`;

-- Dumping structure for table kumparan.tbl_details
CREATE TABLE IF NOT EXISTS `tbl_details` (
  `news_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  PRIMARY KEY (`news_id`,`topic_id`),
  KEY `tbl_details_ibfk_2` (`topic_id`),
  CONSTRAINT `tbl_details_ibfk_1` FOREIGN KEY (`news_id`) REFERENCES `tbl_news` (`news_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `tbl_details_ibfk_2` FOREIGN KEY (`topic_id`) REFERENCES `tbl_topics` (`topic_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_details: ~15 rows (approximately)
/*!40000 ALTER TABLE `tbl_details` DISABLE KEYS */;
INSERT INTO `tbl_details` (`news_id`, `topic_id`) VALUES
	(1, 1),
	(1, 2),
	(1, 3),
	(1, 4),
	(1, 5),
	(1, 6),
	(1, 7),
	(2, 1),
	(2, 2),
	(2, 8),
	(2, 9),
	(2, 10),
	(3, 1),
	(3, 2),
	(3, 11);
/*!40000 ALTER TABLE `tbl_details` ENABLE KEYS */;

-- Dumping structure for table kumparan.tbl_news
CREATE TABLE IF NOT EXISTS `tbl_news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `status_id` int(11) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `content` text,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`news_id`),
  KEY `status_id` (`status_id`),
  CONSTRAINT `tbl_news_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `tbl_news_status` (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_news: ~3 rows (approximately)
/*!40000 ALTER TABLE `tbl_news` DISABLE KEYS */;
INSERT INTO `tbl_news` (`news_id`, `status_id`, `title`, `content`, `created_date`, `modified_date`) VALUES
	(1, 1, 'Ancam Perang Dagang, Duterte Mulai Persulit Masuk  Kopi dan CPO RI', 'Ancaman perang dagang dari Filipina mendapat perhatian dari Kementerian Perdagangan. Buktinya, Menteri Perdagangan Enggartiasto Lukita mengaku akan segera menggelar bisnis forum dengan Filipina untuk menyelesaikannya.\r\nMenurut Enggar, ancaman Filipina tersebut harus segera ditanggapi. Karena Filipina sudah mempersulit masuknya produk kopi saset dan CPO asal Indonesia.\r\n“Ekspor kopi saset kita kesana mulai terganggu sejak Agustus 2018 lalu. Karena mereka menerapkan special safe guard untuk produk kopi dan minyak kelapa sawit (CPO) kita. Makanya kita akan gelar bisnis forum untuk menyelesaikannya,” kata Enggar saat bercerita kepada kumparan, seperti ditulis Sabtu (23/2). \r\nNamun, Enggar belum bisa memastikan kapan bisnis forum tersebut akan digelar. Pasalnya, saat ini pihaknya tengah melakukan persiapan untuk mengikuti India Asean Forum dalam waktu dekat. \r\nEnggar menjelaskan, salah satu pendekatan yang akan digunakan adalah akan melonggarkan impor sejumlah barang dari Filipina. Salah satunya adalah pisang cavendis. \r\n“Filipina itu kan mereka lihat dari defisit, nah kita akan lakukan pendekatan ke sana. Apa yang you mau kita beli. Mereka mau pisang cavendis. Kita akan coba,” imbuhnya. \r\n\r\nIlustrasi biji kelapa sawit Foto: Thinkstock\r\n\r\nSelama ini, kata Enggar, jumlah ekspor produk RI ke Filipina tercatat sekitar USD 600 juta. Sejak awal wacana perang dagang ini muncul, Enggar mengaku sudah melakukan berbagai upaya, yakni mengirim Direktur Jenderal Perdagangan Luar Negeri Oke Nurwan untuk berdiskusi hingga bersurat ke Menteri Perdagangan Filipina. \r\nNamun, Filipina disebut tetap menetapkan special safe guard terhadap produk RI untuk menekan defisit. Tak hanya itu, merek kopi saset merek asli Indonesia juga dianggap sebagai brand mereka.\r\n“Ekspor kita terganggu dan juga brand kita sering dianggap brand mereka. Kita berupaya menjaga kepentingan kita, duta besar kita sudah sampai bicara dengan Presiden Filipina, Rodrigo Duterte. Kita akan bikin Bisnis Forum juga,” pungkasnya. \r\nSebelumnya, pembatasan impor produk minyak kelapa sawit (CPO) dan kopi saset dari Indonesia kini tengah digemborkan Pemerintah Filipina yang dipimpin Presiden Rodrigo Duterte. Setidaknya ada dua faktor yang melatarbelakangi mencuatnya ancaman perang dagang Filipina dan Indonesia.\r\nPertama, Menteri Pertanian Filipina Manny Pinol ingin mencegah banjir produk minyak kelapa sawit Indonesia di pasar lokal. Lalu yang kedua, dikutip dari Philippine News Agency, Pinol meradang usai mendapati defisit perdagangan Filipina dengan Indonesia yang semakin melebar. ', '2019-02-23 11:53:18', NULL),
	(2, 2, 'Startup Bizhare Targetkan Raup Rp 40 M untuk Danai 80 Usaha di 2019', 'Perusahaan rintisan atau startup yang bergerak di bidang equity crowdfunding, Bizhare menargetkan dapat meraup pendanaan Rp 40 miliar pada tahun ini. Tahun lalu, pendanaan yang berhasil diraup Bizhare hanya Rp 6 miliar.\r\nChief Executive Officer Bizhare, Heinrich Vincent, menyampaikan bahwa perusahaannya fokus dalam mendanai bisnis waralaba, dan perusahaan konvensional yang telah berdiri di atas 2 tahun untuk melakukan ekspansi usaha.\r\n"Jadi target tahun ini Rp 40 miliar. Kami sedang mencari usaha yang kualitasnya bagus (untuk didanai)," katanya saat ditemui di Menara Kibar, Jakarta, Sabtu (23/2).\r\nDia menyampaikan pada tahun lalu, pihaknya baru menyalurkan investasi ke 12 gerai bisnis yang tersebar di Jakarta, Bekasi, Bogor, Lampung, dan Surabaya. Sementara pada tahun ini pihaknya menarget dapat mendanai 80 perusahaan.\r\n"Tahun ini mendanai 80 bisnis. Total pendanaan yang bisa kami berikan per usaha itu sekitar seratusan juta sampai Rp 10 miliar," beber Heinrich.\r\n\r\nIlustrasi Uang Rupiah Foto: Thinkstock\r\n?\r\nMenurut dia, pendanaan bisnis oleh Bizhare berasal dari investor ritel atau masyarakat yang berinvestasi melalui situs bizhare.id. Melalui situs itu, investor ritel dapat menanamkan modalnya minimal Rp 5 juta.\r\n"Investasi mulai dari Rp 5 juta, investasi itu nantinya dikonversi menjadi saham di perusahaan yang diinvest. Ada dividen yang diberikan, ada per bulan, per 3 bulan, per enam bulan," ucapnya.\r\nHeinrich menambahkan, Bizhare baru mulai aktif menjadi platform urun dana pada April 2018. Meski masih baru, namun investor yang telah berinvestasi melalui bizhare.id telah mencapai 400 orang hingga akhir 2018 lalu.\r\n"Yang sudah berhasil didanai itu seperti tambak udang vaname di Lampung, Smokey Kebab Baba Rafi di Kemang, Kebab Turki Baba Rafi, Indomaret, dan beberapa lainnya," kata Heinrich.\r\nSaat ini, dia menjelaskan, pihaknya tengah dalam proses mendanai ekspansi Rumah Makan Padang Sederhana Lintau. Ke depan, Bizhare menargetkan dapat mendanai gerai Alfamart, sebuah coffee shop, hingga ekspansi Primagama.', '2019-02-23 14:13:33', NULL),
	(3, 2, 'PUPR Incar Dana Investor Rp 5,1 T untuk Bangun Jalan dan Jembatan', 'Kementerian Pekerjaan Umum dan Perumahan Rakyat (PUPR) pada tahun ini menawarkan 4 proyek jalan dan jembatan senilai Rp 5,1 triliun kepada investor melalui skema Kerjasama Pemerintah dengan Badan Usaha Availability Payment (KPBU AP).\r\nMenurut Direktur Jenderal Bina Marga Kementerian PUPR, Sugiyartanto, KPBU AP merupakan skema di mana investor mendanai proyek tertentu sesuai kontrak, kemudian pemerintah mencicil investasi investor itu selama beberapa tahun.\r\n"Dana pemerintah ini kan terbatas, makanya ada KPBU AP. Ada 4 proyek jalan jembatan, nilainya Rp 5,1 triliun," bebernya kepada kumparan, Sabtu (23/2).\r\n\r\nPembangunan Infrastruktur Jalan Tol Foto: Kementrian Pekerjaan Umum dan Perumahan Rakyat\r\n?\r\nAdapun 4 proyek yang ditawarkan ke investor pada tahun ini, yakni proyek pembangunan dan preservasi jalan di Riau dan Palembang, pembangunan jalan Trans Papua rute Wamena-Momugu, dan perbaikan 14 jembatan tua yang berusia di atas 30 tahun.\r\n"Trans Papua itu nilainya sekitar Rp 1,9 triliun, nilainya masih bisa berubah. Perbaikan jembatan-jembatan tua sekitar Rp 800 miliar," kata Sugiyartanto.\r\nDia menambahkan dalam menjalankan KPBU AP, pihaknya menggandeng Kementerian Perencanaan Pembangunan Nasional (PPN)/Bappenas. Sebab kementerian itu memiliki lembaga yang mengurusi Pembiayaan Investasi Non-Anggaran Pemerintah (PINA).\r\n"Bappenas yang menghubungkan, artinya kerja sama ini tidak kami jalankan sendiri. Tapi ketika uang turun, baru setelahnya kami sendiri," ucapnya.', '2019-02-23 14:16:46', NULL);
/*!40000 ALTER TABLE `tbl_news` ENABLE KEYS */;

-- Dumping structure for table kumparan.tbl_news_status
CREATE TABLE IF NOT EXISTS `tbl_news_status` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `news_status` varchar(20) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_news_status: ~2 rows (approximately)
/*!40000 ALTER TABLE `tbl_news_status` DISABLE KEYS */;
INSERT INTO `tbl_news_status` (`status_id`, `news_status`, `created_date`) VALUES
	(1, 'Draft', '2019-02-23 10:52:41'),
	(2, 'Publish', '2019-02-23 10:52:48'),
	(3, 'Deleted', '2019-02-23 10:52:54');
/*!40000 ALTER TABLE `tbl_news_status` ENABLE KEYS */;

-- Dumping structure for table kumparan.tbl_topics
CREATE TABLE IF NOT EXISTS `tbl_topics` (
  `topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(200) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

-- Dumping data for table kumparan.tbl_topics: ~9 rows (approximately)
/*!40000 ALTER TABLE `tbl_topics` DISABLE KEYS */;
INSERT INTO `tbl_topics` (`topic_id`, `topic`, `created_date`, `modified_date`) VALUES
	(1, 'Ekonomi', '2019-02-23 14:08:32', '2019-02-23 14:09:29'),
	(2, 'Bisnis', '2019-02-23 14:09:46', NULL),
	(3, 'Perang Dagang', '2019-02-23 14:09:59', NULL),
	(4, 'Duterte', '2019-02-23 14:10:06', NULL),
	(5, 'Enggartiasto Lukita', '2019-02-23 14:10:19', NULL),
	(6, 'Kemendag', '2019-02-23 14:10:27', NULL),
	(7, 'Filipina', '2019-02-23 14:10:41', NULL),
	(8, 'Startup', '2019-02-23 14:14:08', NULL),
	(9, 'Waralaba', '2019-02-23 14:14:15', NULL),
	(10, 'UMKM', '2019-02-23 14:14:20', NULL),
	(11, 'Infrastruktur', '2019-02-23 14:16:28', NULL);
/*!40000 ALTER TABLE `tbl_topics` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
