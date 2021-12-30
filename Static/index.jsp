<%-- 
    Document   : index
    Created on : 10-Jul-2021, 14:13:47
    Author     : himanshukumar
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="style.css">
         <link href="../Content/projectcss/project-common.css" rel="stylesheet"/>
        <script>var _ImeiForMobileInSession ='<%=request.getParameter("token")%>';</script>
        <script src="../Scripts/basejs/base-jquery-1.9.1.js"></script>
        <!--<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <script src= "https://cdn.jsdelivr.net/npm/html2canvas@1.0.0-rc.5/dist/html2canvas.min.js"></script>
        <script src="../views/HostFile.js" type="text/javascript"></script>
        <link href="../Content/basecss/base-jquery-ui.css" rel="stylesheet"/>
        <script src="../Scripts/basejs/base-jquery-ui.js"></script>
        
    </head>
    <body>
        <section class="frame">
            <div class="container">
                <div class="row">
                    <div class="moniter">
                        <div id="c1" class="card">
                            <img src="images/lcd 1.png" alt="image" class="img-fliud">
                            <p style="font-size:11px" id="token">123456</p>
                        </div>
                        <div id="c2" class="card active">
                           <img src="images/lcd 2.png" alt="image" class="img-fliud">
                                <p>Remote</p>
                        </div>
                        <div id="c3" class="card">
                            <img id="" src="images/lcd 3.png" alt="image" class="img-fliud">
                            <p>screenshot</p>
                        </div>
                    </div>
                    <div class="screen">
                        <div class="time">
                           <p id="s_timer">00: 00: 00</p> 
                        </div>
                        <div class="session" id="btnsession">
                            
                            <a href="javascript:closeWindow(); "><img src="images/stop-icon.png" alt="image" class="img-fluid"> Stop Session</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="display">
            <div class="container">
                <div id="imgDiv " style="width:80%;height:500px">
                    <!--<div class="display-screen"></div>-->
                    <img class="display-screen" id="CurrentImage">
                </div>
            </div>
        </section>
        <section class="icons">
            <div class="container">
                <div class="row">
                    <div class="icon-section">
                        <div class="icon1">
                            <img id="btnBack" src="images/back-icon.png" alt="image" class="image-fluid">
                            <p>Back</p>
                        </div>
                        <div class="icon1">
                            <img id="btnHome" src="images/home-icon.png" alt="image" class="image-fluid">
                            <p>Home</p>
                        </div>
                        <div class="icon1">
                            <img id="btnMenu" src="images/menu-icon.png" alt="image" class="image-fluid">
                            <p>Menu</p>
                        </div>
                        <div class="icon1">
                            <img id="btnPower" src="images/powe-icon.png" alt="image" class="image-fluid">
                            <p>Power</p>
                        </div>
                        <div class="icon1">
                            <img id="btnScrollUp" src="images/top-icon.png" alt="image" class="image-fluid">
                            <p>Top</p>
                        </div>
                        <div class="icon1">
                            <img id="btnScrollLeft" src="images/left-icon.png" alt="image" class="image-fluid">
                            <p>Left</p>
                        </div>
                        <div class="icon1">
                            <img id="btnScrollDown" src="images/bottom-icon.png" alt="image" class="image-fluid">
                            <p>Bottom</p>
                        </div>
                        <div class="icon1">
                            <img id="btnScrollRight" src="images/right-icon.png" alt="image" class="image-fluid">
                            <p>Right</p>
                        </div>
                    </div>
                    <div class="icon-section1">
                        <!--<div class="icon2">-->
                        <div class>   
                            <input id="file" type="file">
                            <!--            <span><label>File upload</label></span>
                                        <label for="file-input">
                                             <input id="file" type="file">
                                          <img src="images/upload-icon.png" alt="image" class="image-fluid" style="width: 30px;"> 
                                        </label>-->


                        </div>
                        <div class="send">
                            <button type="btn" onclick="HostFile()" id="sendfile" class="send-btn">Send</button>
                        </div>

                    </div>
                </div>
            </div>
        </section>

            <div id="dailog" title="Screen Shot">

        </div>
        
        
         <div id="loading">
            <span id="Close_Loader_Process">Close</span>
            <p style="margin-top: 16%;margin-left: 35%;"><b>Please Click The Start Remote Access <br> To Take Control Of Your Device</b></p>
            <img id="loading-image"  class="center_image_loading" src="../Content/images/loader.gif" alt="Loading..." />
            
        </div>
        
    </body>
     
       <script src="../Scripts/retrieveData/project-main.js"></script>
        <script src="../Scripts/retrieveData/DataStream.js"></script>
        <script src="../Scripts/retrieveData/load-image.js"></script>
        <script src="../Scripts/retrieveData/session.js"></script>
        <script src="../Scripts/retrieveData/project-timer.js"></script>
        <script src="../Scripts/retrieveData/json2.js"></script>
        <!--<scrip>-->
<!--$(document).ready(function () 
{
     $('#c1').click(function()
     {
         alert(1);
         $('#c1 #c2 #c3').removeClass('active');
         $(this).addClass('active');
 });
});-->
        <!--</scrip>-->
</html>
