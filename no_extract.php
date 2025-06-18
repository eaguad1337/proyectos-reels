<?php

// Mímica de un Request (formulario)
global $_POST;
$_POST = [
    "nombre" => "Juan",
    "edad" => 25,
    "email" => "juan@example.com",
    "hora" => "reemplazado por el usuario"
];
//

function guardar_formulario($hora) {
    extract($_POST, EXTR_PREFIX_ALL, "t");

    echo "Nombre: $t_nombre" . PHP_EOL;
    echo "Edad: $t_edad" . PHP_EOL;
    echo "Email: $t_email" . PHP_EOL;
    echo "T Hora: $t_hora" . PHP_EOL;
    echo "Hora: $hora" . PHP_EOL;
}

$hora = date("H:i:s");
guardar_formulario($hora);