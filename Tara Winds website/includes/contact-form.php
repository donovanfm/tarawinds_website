<?php

    $name = strip_tags(trim($_POST["name"]));
            $name = str_replace(array("\r","\n"),array(" "," "),$name);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $phone = trim($_POST["phone"]);
    $message = trim($_POST["message"]);

    //$emailto = 'andrea.strauss22@gmail.com ';
    $emailto = 'masjaha88@gmail.com ';

    $msg = "Name: ".$name."   Email: ".$email."     Phone: ".$phone."      Message: ".$message;

    //$admin_email = "andrea.strauss22@gmail.com ";
    $admin_email = "masjaha88@gmail.com ";
    mail($admin_email, "Tara Winds", $msg);

?>
