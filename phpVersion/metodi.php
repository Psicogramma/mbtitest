<?php


########### ritorna un array con domande e funzioni mbti associate ###################
 
function IOquestions($filename)
{
    $i       = 0;
    $flag    = 0;
    $domande = array();
    
    $file = fopen($filename, "r");
    
    if ($file) {
        while (($line = fgets($file)) !== false) {
            
            if ($line != "\r\n") {
                if ($flag == 0) {
                    
                    $mbtiFunction = explode(" ", $line);
                    
                    $flag = 1;
                } else {
                    
                    $domande[$line] = $mbtiFunction[$i];
                    $i++;
                }
            }
            
            
        }
        fclose($file);
        return $domande;
        
        
    } else {
        echo "Errore ";
    }
}


########### ritorna un array associativo mescolato ###################

function shuffle_assoc($my_array)
{
    $keys = array_keys($my_array);
    
    shuffle($keys);
    
    foreach ($keys as $key) {
        $new[$key] = $my_array[$key];
    }
    
    $my_array = $new;
    
    return $my_array;
}



?>
