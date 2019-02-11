<html>

<head>
</head>

<body>

<?php 
################ recupero funzioni da "metodi.php" ################

require'metodi.php';


####### uso la funzione IOQues per ricavare le domande da file  ######################
$domande = IOQuestions("domande.txt");

########## uso la funzione shuffle per mescolare
$domande = shuffle_assoc($domande);

 ?>

    <!-------------------- carico la struttura html e le domande  ------------------------------------------------------------->

    <form method="POST" action="calcola.php">


        <?php $k=1; 
		foreach($domande as $chiave => $valore){ 
		echo $chiave."<br />"; 
		for ($i= 1; $i <=5 ; $i++) { ?>

            <input type="radio" name="<?php echo $k ?>" value=" <?php echo $i ?>"><?php echo $i ?>

            <?php } $k++; echo "<br>"; } ?>
            <input type="submit" value="Submit">
    </form>





</body>

</html>

