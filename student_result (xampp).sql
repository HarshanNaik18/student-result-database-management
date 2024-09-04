-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2024 at 12:02 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_result`
--

-- --------------------------------------------------------

--
-- Table structure for table `participants`
--

CREATE TABLE `participants` (
  `id` int(10) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `participants`
--

INSERT INTO `participants` (`id`, `fname`, `lname`, `contact`, `email`, `question`, `answer`, `password`) VALUES
(4, 'Aishwarya', 'N', '1230987657', 'naishwarya@gmail.com', 'Your pet name', 'aish', 'Aish'),
(5, 'admin', 'name', '9900715426', 'admin123@gmail.com', 'Your pet name', 'Bruno', 'admin123'),
(6, 'fghjk', 'vbnm', 'fghjk', 'abc', 'Your pet name', 'ghj', 'abc'),
(7, 'abc', 'def', '1234567890', 'abc@gmail', 'Your pet name', 'fghj', '123'),
(8, 'qwer', 'werf', '1234567890', 'asdfg', 'Your best friend name', 'sd', 'asd'),
(9, 'aishwarya', 'n', '5555', 'kkkkk', 'Your pet name', 'gdg', 'llkkklk'),
(10, 'admin', 'name', '1234567890', 'abc@gmail', 'Your best friend name', 'api', '123'),
(11, '1', '2', '1', '2', 'Your pet name', '2', '5'),
(12, '1', '1', '1', '1', 'Your pet name', '1', '1'),
(13, 'n', 'n', 'n', 'naish367@gmail.com', 'Your pet name', 'n', 'n'),
(14, '45678', '5678', 'dfg', 'fgh3680@gmail.com', 'Your pet name', 'ggh', 'g'),
(15, 'j', 'j', 'j', 'h6@g.c', 'Your pet name', 'j', 'j'),
(16, 'a', 'a', 'a', 'a1@g.c', 'Your birth day', 'a', 'a'),
(17, '123', '12', '12', 'w1@l.c', 'Your best friend name', 'w', 'w'),
(18, 'aish', 'asisj', '9876543211', 'aish1234@gmail.com', 'Your best friend name', '123', 'Aishu@10'),
(19, 'aish', 'aish', '9876543211', 'aish301@gmail.com', 'Your pet name', 'dog', 'Aishu@10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `participants`
--
ALTER TABLE `participants`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `participants`
--
ALTER TABLE `participants`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
