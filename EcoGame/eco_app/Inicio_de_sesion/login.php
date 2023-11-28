<?php
require 'conexion_postgres.php';
session_start();
$usuario=$_POST['txtusuario'];
$pass=$_POST['txtpass'];

$query="SELECT * FROM usuarios WHERE usuario='$usuario' AND contrasena='$pass'";
$consulta=pg_query($conexion,$query);
$cantidad=pg_num_rows($consulta);
if($cantidad>0){
    $_SESSION['nombre_usuario']=$usuario;
    header("location: ingreso.php");
}else{
    echo "Datos incorrectos";
}



?>