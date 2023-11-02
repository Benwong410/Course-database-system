-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+08:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

------------------------------------------------------------------------------------------------------
-- Table structure for table `Users`
--
DROP TABLE IF EXISTS `Users`;

# Create TABLE 'Users'
CREATE TABLE `Users` (
  `user_id` int AUTO_INCREMENT PRIMARY KEY,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(200) NOT NULL,
  `user_login_time` time NOT NULL,
  `user_login_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1, "JACK", "jack@gmail.com", NOW(), '2021-01-20');
INSERT INTO `Users` VALUES (2, "TOM", "tom@gmail.com", NOW(), '2021-01-20');
INSERT INTO `Users` VALUES (3, "Prof. Smith", "p.smith@gmail.com", NOW(), '2021-01-20');
INSERT INTO `Users` VALUES (4, "Prof. Wong", "p.wong@gmail.com", NOW(), '2021-01-20');
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

------------------------------------------------------------------------------------------------------
-- Table structure for table `Students`
--
DROP TABLE IF EXISTS `Students`;

# Create TABLE 'Students'
CREATE TABLE `Students` (
  `user_id` INT PRIMARY KEY,
  `student_id_string` varchar(50) NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES Users(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1, "Y123456");
INSERT INTO `Students` VALUES (2, "B123456");
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

------------------------------------------------------------------------------------------------------
-- Table structure for table `Teachers`
--
DROP TABLE IF EXISTS `Teachers`;

# Create TABLE 'Teachers'
CREATE TABLE `Teachers` (
  `user_id` INT PRIMARY KEY,
  `teacher_office` varchar(50) NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES Users(`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Teachers` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Teachers` VALUES (3, "KB217");
INSERT INTO `Teachers` VALUES (4, "CYM111");
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;


------------------------------------------------------------------------------------------------------
-- Table structure for table `Courses` 
--
DROP TABLE IF EXISTS `Courses`;

# Create TABLE 'Courses'
CREATE TABLE `Courses` (
  `course_id` int AUTO_INCREMENT PRIMARY KEY,
  `course_code` varchar(50) NOT NULL,
  `course_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Courses` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Courses` VALUES (1, "COMP2120", "Computer Organization");
INSERT INTO `Courses` VALUES (2, "COMP3278", "Introduction to database management systems");
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;


# Create TABLE 'Coursetimeslots'
-- Ben: to do: create table sql
-- Ben: to do: insert data sql

# Create TABLE 'CourseMaterials'
-- Ben: to do: create table sql
-- Ben: to do: insert data sql

# Create TABLE 'Takes_course'
-- Ben: to do: create table sql
-- Ben: to do: insert data sql

-- # Ben: Create TABLE 'Teahes' optional
-- # Ben: Create TABLE 'Discussion' optional



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
