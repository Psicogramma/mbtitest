<html>
<head>
</head>
<body>

 
<?php
// prelevo file di funzioni
require 'metodi.php';




      // prelevo le domande da file	
	$domande = IOquestions("domande.txt");
	
	// mixo le domande
	$domande = shuffle_assoc($domande);
	
	   
	   
   
  
 //  creo pagina di visualizzazione con domande mixate

?>
                  
<form method="POST" action="calcola.php" >

 
<?php


$k=1;


foreach($domande as $chiave => $valore){
	
	 echo $chiave."<br />";  
	
	
for ($i= 1; $i <= 5; $i++) {
	?>

<input type="radio" name="<?php echo $k ?>" value=" <?php echo $i ?>"> <?php echo $i ?> 

<?php
}
$k++;
echo "<br>";
}
 
?>
<input type="submit" value="Submit">
</form>





</body>
</html>

