-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 07, 2015 at 11:37 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `marks2`
--

-- --------------------------------------------------------

--
-- Table structure for table `cs1234`
--

CREATE TABLE IF NOT EXISTS `cs1234` (
  `StudentName` varchar(30) DEFAULT NULL,
  `Test1` float DEFAULT NULL,
  `Test2` float DEFAULT NULL,
  `Test3` float DEFAULT NULL,
  `Test4` float DEFAULT NULL,
  `Test5` float DEFAULT NULL,
  `Test6` float DEFAULT NULL,
  `Test7` float DEFAULT NULL,
  `Test8` float DEFAULT NULL,
  `Test9` float DEFAULT NULL,
  `Test10` float DEFAULT NULL,
  `Test11` float DEFAULT NULL,
  `Test12` float DEFAULT NULL,
  `Test13` float DEFAULT NULL,
  `Test14` float DEFAULT NULL,
  `Test15` float DEFAULT NULL,
  `pred` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs1234`
--

INSERT INTO `cs1234` (`StudentName`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`, `pred`) VALUES
('120126K', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120116F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120237C', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120306M', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cs2022`
--

CREATE TABLE IF NOT EXISTS `cs2022` (
  `StudentName` varchar(10) NOT NULL,
  `Test1` int(11) DEFAULT NULL,
  `Test2` int(11) DEFAULT NULL,
  `Test3` int(11) DEFAULT NULL,
  `Test4` int(11) DEFAULT NULL,
  `Test5` int(11) DEFAULT NULL,
  `Test6` int(11) DEFAULT NULL,
  `Test7` int(11) DEFAULT NULL,
  `Test8` int(11) DEFAULT NULL,
  `Test9` int(11) DEFAULT NULL,
  `Test10` int(11) DEFAULT NULL,
  `Test11` int(11) DEFAULT NULL,
  `Test12` int(11) DEFAULT NULL,
  `Test13` int(11) DEFAULT NULL,
  `Test14` int(11) DEFAULT NULL,
  `Test15` int(11) DEFAULT NULL,
  UNIQUE KEY `StudentName` (`StudentName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs2022`
--

INSERT INTO `cs2022` (`StudentName`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`) VALUES
('120006T', 80, 85, 90, 60, 75, 93, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120010B', 50, 54, 95, 60, 40, 70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120025B', 60, 51, 90, 85, 70, 83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120028L', 60, 90, 95, 95, 74, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120029P', 64, 90, 90, 95, 80, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120074X', 80, 95, 95, 0, 50, 86, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120083A', 95, 85, 90, 0, 60, 56, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120111K', 60, 90, 0, 90, 78, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120113T', 100, 48, 40, 80, 0, 53, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120128T', 70, 78, 90, 0, 55, 60, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120132B', 70, 80, 80, 0, 60, 83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120143J', 50, 55, 100, 0, 83, 70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120162P', 70, 60, 100, 40, 60, 65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120165D', 60, 60, 80, 0, 90, 60, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120182C', 50, 55, 90, 0, 52, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120195T', 70, 65, 90, 50, 100, 65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120197C', 60, 40, 85, 100, 90, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120217P', 70, 60, 95, 0, 43, 45, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120221X', 60, 40, 85, 100, 90, 70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120222H', 60, 40, 90, 100, 85, 38, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120228B ', 60, 57, 85, 100, 63, 80, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120236X', 70, 65, 95, 95, 80, 85, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120237C', 50, 50, 90, 100, 60, 60, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120260N ', 60, 45, 95, 60, 70, 70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120271A', 68, 50, 85, 50, 83, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120281E', 70, 60, 100, 40, 55, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120282H', 70, 65, 80, 40, 80, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120284P', 70, 95, 0, 85, 60, 75, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120287D', 60, 70, 85, 0, 40, 95, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120306M', 70, 60, 95, 0, 43, 45, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120309B', 60, 55, 100, 90, 72, 90, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120323L', 70, 60, 100, 90, 87, 90, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120337H', 70, 50, 95, 85, 70, 96, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120342T', 50, 85, 0, 74, 70, 65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120343X', 70, 41, 95, 0, 75, 60, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120345F', 50, 48, 95, 35, 68, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120353D', 50, 60, 15, 15, 58, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120357T', 70, 40, 100, 80, 100, 95, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120374R', 75, 100, 40, 40, 80, 58, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120375V', 0, 10, 40, 0, 65, 53, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120391P', 85, 60, 100, 90, 85, 89, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120399X', 80, 100, 40, 85, 0, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120410C', 60, 59, 95, 0, 80, 87, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120418H', 51, 65, 100, 40, 76, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120445L', 50, 64, 95, 40, 65, 76, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120448A', 60, 30, 100, 95, 40, 43, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120450X', 42, 47, 90, 90, 90, 93, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120452F', 70, 72, 95, 90, 80, 78, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120460D', 70, 65, 85, 60, 75, 73, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120470H', 60, 73, 95, 90, 78, 73, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120488U', 3, 68, 95, 40, 85, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120496R', 64, 88, 100, 60, 95, 93, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120507F', 70, 60, 85, 40, 80, 83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120538B', 50, 55, 95, 90, 47, 93, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120542G', 60, 88, 100, 85, 85, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120548F', 0, 10, 90, 85, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120586T', 60, 88, 95, 90, 45, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120594P', 70, 60, 75, 50, 60, 96, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120606H', 45, 85, 95, 78, 55, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120612X', 50, 55, 95, 88, 45, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120615J', 80, 75, 95, 50, 85, 83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120633L', 60, 50, 20, 40, 73, 33, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120638G', 70, 80, 100, 80, 85, 83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120665K', 50, 50, 35, 40, 65, 36, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120694X', 50, 65, 95, 95, 55, 70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120699R', 0, 55, 90, 80, 45, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120702A ', 65, 68, 95, 95, 83, 86, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120706N', 65, 75, 90, 95, 80, 91, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120710V', 80, 72, 100, 90, 78, 90, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120721F', 50, 40, 95, 75, 70, 83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120749X', 60, 65, 60, 20, 60, 70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

--
-- Triggers `cs2022`
--
DROP TRIGGER IF EXISTS `after_cs2022_update`;
DELIMITER //
CREATE TRIGGER `after_cs2022_update` AFTER UPDATE ON `cs2022`
 FOR EACH ROW begin
IF (new.pred<35) THEN
    INSERT INTO `warnings`(`Subject`, `Student`, `Marks`) VALUES('cs2022',new.StudentName,new.pred);
END IF;
END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `cs2052`
--

CREATE TABLE IF NOT EXISTS `cs2052` (
  `StudentName` varchar(10) NOT NULL,
  `Test1` int(11) DEFAULT NULL,
  `Test2` int(11) DEFAULT NULL,
  `Test3` int(11) DEFAULT NULL,
  `Test4` int(11) DEFAULT NULL,
  `Test5` int(11) DEFAULT NULL,
  `Test6` int(11) DEFAULT NULL,
  `Test7` int(11) DEFAULT NULL,
  `Test8` int(11) DEFAULT NULL,
  `Test9` int(11) DEFAULT NULL,
  `Test10` int(11) DEFAULT NULL,
  `Test11` int(11) DEFAULT NULL,
  `Test12` int(11) DEFAULT NULL,
  `Test13` int(11) DEFAULT NULL,
  `Test14` int(11) DEFAULT NULL,
  `Test15` int(11) DEFAULT NULL,
  `pred` float DEFAULT NULL,
  PRIMARY KEY (`StudentName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs2052`
--

INSERT INTO `cs2052` (`StudentName`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`, `pred`) VALUES
('120006T', 100, 100, 100, 100, 100, 100, 100, 100, 75, 95, 100, NULL, NULL, NULL, NULL, NULL),
('120026L', 100, 100, 100, 80, 100, 0, 90, 90, 65, 100, 67, NULL, NULL, NULL, NULL, NULL),
('120028L', 100, 100, 100, 100, 100, 100, 90, 100, 85, 100, 100, NULL, NULL, NULL, NULL, NULL),
('120029P', 100, 80, 60, 100, 0, 0, 90, 60, 70, 65, 100, NULL, NULL, NULL, NULL, NULL),
('120111K', 80, 80, 100, 100, 100, 90, 70, 40, 80, 100, 83, NULL, NULL, NULL, NULL, NULL),
('120427J', 100, 100, 100, 100, 100, 100, 90, 100, 100, 100, 100, NULL, NULL, NULL, NULL, NULL),
('120526L', 100, 80, 100, 100, 100, 0, 60, 0, 85, 0, 67, NULL, NULL, NULL, NULL, NULL),
('120594P', 100, 100, 100, 100, 100, 80, 60, 80, 55, 85, 65, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cs2202`
--

CREATE TABLE IF NOT EXISTS `cs2202` (
  `StudentName` varchar(50) NOT NULL,
  `Test1` int(11) NOT NULL,
  `Test2` int(11) NOT NULL,
  `Test3` int(11) NOT NULL,
  `Test4` int(11) NOT NULL,
  `Test5` int(11) NOT NULL,
  `Test6` int(11) NOT NULL,
  `Test7` int(11) NOT NULL,
  `Test8` int(11) NOT NULL,
  `Test9` int(11) NOT NULL,
  `Test10` int(11) NOT NULL,
  `Test11` int(11) NOT NULL,
  `Test12` int(11) NOT NULL,
  `Test13` int(11) NOT NULL,
  `Test14` int(11) NOT NULL,
  `Test15` int(11) DEFAULT NULL,
  `pred` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs2202`
--

INSERT INTO `cs2202` (`StudentName`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`, `pred`) VALUES
('M.D.N Dilini', 50, 70, 75, 85, 86, 78, 72, 80, 85, 86, 88, 84, 90, 95, 90, NULL),
('J.A.A.M Jayanetti', 80, 82, 85, 80, 85, 86, 84, 83, 82, 86, 83, 85, 84, 86, 100, NULL),
('A.Y Dissanayake', 75, 80, 85, 83, 80, 78, 75, 70, 65, 60, 50, 45, 35, 30, 60, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cs2952`
--

CREATE TABLE IF NOT EXISTS `cs2952` (
  `StudentName` varchar(10) DEFAULT NULL,
  `Test1` int(11) DEFAULT NULL,
  `Test2` int(11) DEFAULT NULL,
  `Test3` int(11) DEFAULT NULL,
  `Test4` int(11) DEFAULT NULL,
  `Test5` int(11) DEFAULT NULL,
  `Test6` int(11) DEFAULT NULL,
  `Test7` int(11) DEFAULT NULL,
  `Test8` int(11) DEFAULT NULL,
  `Test9` int(11) DEFAULT NULL,
  `Test10` int(11) DEFAULT NULL,
  `Test11` int(11) DEFAULT NULL,
  `Test12` int(11) DEFAULT NULL,
  `Test13` int(11) DEFAULT NULL,
  `Test14` int(11) DEFAULT NULL,
  `Test15` int(11) DEFAULT NULL,
  `pred` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs2952`
--

INSERT INTO `cs2952` (`StudentName`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`, `pred`) VALUES
('120126K', 70, 76, 100, 30, 50, 50, 50, 30, 60, 60, 70, 70, 100, 100, NULL, 0),
('120542G', 90, 90, 90, 95, 70, 70, 70, 70, 70, 50, 90, 90, 100, 100, NULL, 0),
('120237C', 0, 78, 70, 100, 100, 70, 60, 90, 80, 80, 90, 88, 100, 100, NULL, 0),
('120116F', 80, 68, 90, 70, 70, 70, 90, 90, 90, 90, 80, 90, 100, 100, NULL, 0),
('120132B', 0, 60, 40, 60, 30, 0, 60, 30, 70, 60, 60, 70, 100, 100, NULL, 0),
('120129X', 0, 76, 0, 90, 0, 70, 90, 80, 0, 70, 80, 70, 100, 100, NULL, 0),
('120228B', 80, 64, 70, 40, 20, 50, 70, 40, 70, 40, 80, 70, 100, 100, NULL, 0),
('120733T', 60, 46, 50, 90, 70, 70, 60, 40, 40, 80, 60, 50, 100, 100, NULL, 0),
('120345F', 80, 66, 40, 90, 50, 40, 70, 0, 70, 70, 80, 70, 100, 100, NULL, 0),
('120323L ', 60, 82, 80, 80, 100, 80, 70, 90, 80, 100, 100, 100, 100, 100, NULL, 0),
('120749X', 70, 82, 60, 70, 70, 70, 80, 60, 70, 70, 70, 70, 100, 100, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `cs4444`
--

CREATE TABLE IF NOT EXISTS `cs4444` (
  `nm` varchar(30) DEFAULT NULL,
  `Test1` float DEFAULT NULL,
  `Test2` float DEFAULT NULL,
  `Test3` float DEFAULT NULL,
  `Test4` float DEFAULT NULL,
  `Test5` float DEFAULT NULL,
  `Test6` float DEFAULT NULL,
  `Test7` float DEFAULT NULL,
  `Test8` float DEFAULT NULL,
  `Test9` float DEFAULT NULL,
  `Test10` float DEFAULT NULL,
  `Test11` float DEFAULT NULL,
  `Test12` float DEFAULT NULL,
  `Test13` float DEFAULT NULL,
  `Test14` float DEFAULT NULL,
  `Test15` float DEFAULT NULL,
  `pred` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cs4444`
--

INSERT INTO `cs4444` (`nm`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`, `pred`) VALUES
('122k', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120306M', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120126K', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120116F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120237C', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('120306M', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `Name` varchar(25) NOT NULL,
  `UserName` varchar(25) NOT NULL,
  `PassWord` varchar(25) NOT NULL,
  `SNo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Name`, `UserName`, `PassWord`, `SNo`) VALUES
('Lecturer', 'Yas', 'ló•Îí¥xÖuûàŒÍ‚Ên', 2),
('Lecturer', 'Yas', 'ló•Îí¥xÖuûàŒÍ‚Ên', 2),
('Lecturer', 'Yas', 'ló•Îí¥xÖuûàŒÍ‚Ên', 2);

-- --------------------------------------------------------

--
-- Table structure for table `warnings`
--

CREATE TABLE IF NOT EXISTS `warnings` (
  `Subject` varchar(20) NOT NULL,
  `Student` varchar(20) NOT NULL,
  `Marks` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `warnings`
--

INSERT INTO `warnings` (`Subject`, `Student`, `Marks`) VALUES
('cs2022', '120548F', 30),
('cs2022', '120126K', 22);

-- --------------------------------------------------------

--
-- Table structure for table `weights`
--

CREATE TABLE IF NOT EXISTS `weights` (
  `Subject` varchar(10) NOT NULL,
  `Test1` float DEFAULT NULL,
  `Test2` float DEFAULT NULL,
  `Test3` float DEFAULT NULL,
  `Test4` float DEFAULT NULL,
  `Test5` float DEFAULT NULL,
  `Test6` float DEFAULT NULL,
  `Test7` float DEFAULT NULL,
  `Test8` float DEFAULT NULL,
  `Test9` float DEFAULT NULL,
  `Test10` float DEFAULT NULL,
  `Test11` float DEFAULT NULL,
  `Test12` float DEFAULT NULL,
  `Test13` float DEFAULT NULL,
  `Test14` float DEFAULT NULL,
  `Test15` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `weights`
--

INSERT INTO `weights` (`Subject`, `Test1`, `Test2`, `Test3`, `Test4`, `Test5`, `Test6`, `Test7`, `Test8`, `Test9`, `Test10`, `Test11`, `Test12`, `Test13`, `Test14`, `Test15`) VALUES
('cs2052', 3, 3, 3, 3, 3, 3, 10, 10, 6, 6, 8, NULL, NULL, NULL, NULL),
('cs2022', 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('cs2952', 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 5, 6, NULL);

DELIMITER $$
--
-- Events
--
CREATE DEFINER=`root`@`localhost` EVENT `delete_warnings_data` ON SCHEDULE EVERY 365 DAY STARTS '2015-09-03 21:34:35' ON COMPLETION NOT PRESERVE ENABLE DO DELETE FROM `warnings` where 1$$

DELIMITER ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
