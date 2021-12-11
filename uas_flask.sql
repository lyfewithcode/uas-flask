-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2021 at 06:20 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uas_flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `iduser` int(3) NOT NULL,
  `namalengkap` varchar(40) NOT NULL,
  `username` varchar(6) NOT NULL,
  `password` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`iduser`, `namalengkap`, `username`, `password`) VALUES
(1, 'Maulana Ahmad', 'ahmad', 'admin'),
(6, 'Devi Pusputasari', 'devdev', 'devdev'),
(8, 'Siskaaa', 'siska', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `idpost` int(3) NOT NULL,
  `judul` varchar(40) NOT NULL,
  `isi` text NOT NULL,
  `keyword` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`idpost`, `judul`, `isi`, `keyword`) VALUES
(147, 'Welcome Note', 'Kalau lo lagi membaca kalimat ini berarti lo niatin untuk nge-klik menu di atas dan mencari tahu lebih tentang blog ini. I appreciate you for doing that and I’d like to welcome you to my new home.', 'introduction'),
(148, 'Photography', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vulputate ex eget facilisis laoreet. Nulla mollis dui ut nulla tincidunt commodo. Etiam sollicitudin ac dui id tristique. Mauris sit amet maximus urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla in fermentum quam, eu rhoncus lorem.', 'photography'),
(149, 'Nature cinematic photography', 'Mauris non augue at neque gravida luctus eget tincidunt lorem. Mauris convallis at felis ac consequat. Mauris dictum orci in libero gravida, in tincidunt dui aliquam. Nam hendrerit vulputate tempus. Sed imperdiet pellentesque est, ut varius orci tristique id. In scelerisque varius iaculis. Fusce tortor velit, egestas vel rutrum at, viverra et ante.', 'photography'),
(150, 'Street cinematic photography', 'Nunc vehicula lectus id fringilla dictum. Integer molestie viverra odio, id maximus tellus consectetur eu. Curabitur tristique tempus neque sed scelerisque. Quisque tempor nec eros a vestibulum. Cras nec suscipit eros. Donec venenatis nunc sed mi viverra, sed dignissim nulla consectetur. Phasellus ac ornare nisl, a finibus erat. Aenean sit amet sodales libero.', 'photography, cinematic'),
(151, 'Teh cinematic look', 'Sed quis lectus dictum, scelerisque augue non, aliquam nibh. Etiam non dapibus nisl. Sed nec consectetur justo, in dapibus dui. Curabitur tincidunt vitae purus nec elementum. Praesent cursus augue erat, sit amet aliquet nibh tristique eu. Interdum et malesuada fames ac ante ipsum primis in faucibus.', 'photography');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`iduser`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`idpost`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `iduser` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `idpost` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=152;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
