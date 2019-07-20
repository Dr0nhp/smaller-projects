$wort = "hallo";
$wortArray = str_split($wort);
$haeufigkeit = array();

for ($i =0; $i < count($wortArray); $i++) {
    
    $buchstabe = $wortArray[$i];                                // Damit holst du dir den aktuellen Buchstaben -> Zuerst an stelle 0, dann 1 ,...


    if (!isset($haeufigkeit[$buchstabe])) {                     // isset prüft ob ein wert enthalten ist. 
                                                                // Das ! davor macht das gegenteil - es wird also geprüft ob KEIN wert enthalten ist.
                                                                // Wichtig - auch eine 0 ist ein Wert, deswegen darfst du nicht prüfen ob da 0 drin steht.
                                                                // Was evtl. gehen würde, wäre zu prüfen ob der wert NULL ist. Also ob er leer ist.

        $haeufigkeit[$buchstabe] = 1;                           // Falls also im Array an der Stelle Buchstabe nichts drin steht -
                                                                // haben wir den buchstaben zum ersten mal
                                                                // Getroffen und sagen dann - okay dann ist er jetzt 1x drin.
    } 
    else
    $haeufigkeit[$buchstabe] = $haeufigkeit[$buchstabe] +1;     // Wenn da schon eine Zahl drin steht, rechnen wir +1 drauf - weil er ja wieder gefunden
                                                                // wurde.
}
var_dump($haeufigkeit);