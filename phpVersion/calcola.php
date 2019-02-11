<?php 



############### leggo le risposte e le inserisco nell 'array risposte   ###############
   
$punteggi = ['Si ' => 0, 'Ne ' => 0,'Fi ' => 0,'Te ' => 0,'Ti ' => 0,'Fe ' => 0,'Ni ' => 0,'Se ' => 0];
$risposte = array();

################ carico le risposte nell'array "risposte" ###################

for($i=0; $i<2; $i++){
	   
  $risposte[$i]=$_POST[$i+1];
  
  echo $risposte[$i];

}


###################     stampo punteggi  ##########################
		   		   
foreach($punteggi as $chiave => $valore)  
   {  
   echo $chiave.": ".$valore."<br />";  
   }  
?>