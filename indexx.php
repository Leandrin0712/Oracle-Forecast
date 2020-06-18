<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Oracle Forecast</title>
    <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
       <h1>Oracle Forecast</h1>

       <h2>
             <?php
             $cidade = $_POST["cidade"];
                echo $cidade;
             ?>
        </h2>
        <h3>


            <?php
                $cidade = $_POST["cidade"];
        		shell_exec("python3 python.py {$cidade}");
        		$condicao = file_get_contents("condicao.txt");
        		$temperatura = file_get_contents("temperatura.txt");
                
                echo "<br>";
        		echo $condicao;
        		echo "<br>";
        		echo $temperatura;
        	?>


            	</h3>
</body>
</html>
