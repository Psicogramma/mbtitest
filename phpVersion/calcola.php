<?php 



############### leggo le risposte e le inserisco nell 'array risposte   ###############
   
$punteggi = ['Si ' => 0, 'Ne ' => 0,'Fi ' => 0,'Te ' => 0,'Ti ' => 0,'Fe ' => 0,'Ni ' => 0,'Se ' => 0];
$inverse = ['Si' => 'Ne', 'Ne' => 'Si', 'Fi' => 'Te', 'Te' => 'Fi', 'Ti' => 'Fe', 'Fe' => 'Ti', 'Ni' => 'Se', 'Se' => 'Ni']
$opposte = ['Si' => 'Se', 'Ne' => 'Ni', 'Fi' => 'Fe', 'Te' => 'Ti', 'Ti' => 'Te', 'Fe' => 'Fi', 'Ni' => 'Ne', 'Se' => 'Si']
$correzione_opposte = ['']
$risposte = array();

################ carico le risposte nell'array "risposte" ###################

for($i=0; $i<2; $i++){
	   
  $risposte[$i]=$_POST[$i+1];
  echo $risposte[$i];
  if

}

" <br> "

###################     stampo punteggi  ##########################
		   		   
foreach($punteggi as $chiave => $valore)  
   {  
   echo $chiave.": ".$valore."<br />";  
   }  
?>