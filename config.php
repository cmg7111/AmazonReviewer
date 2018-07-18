<?php
    $host = 'ec2-35-169-85-70.compute-1.amazonaws.com';
    $user = 'root';
    $pw = 'root';
    $dbName = 'reviewer';
    $dsn = "mysql:host=localhost;port=3306;dbname=$dbName;charset=utf8"; 

    try { 
    	$db = new PDO($dsn, $user, $pw); 
    	$db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); 
    	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

	} catch(PDOException $e) { echo $e->getMessage(); }

 ?>


