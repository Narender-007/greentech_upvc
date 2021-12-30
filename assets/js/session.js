/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
var connectflag=false;
//var _ImeiForMobileInSession = "";
window.onload = init;
var isDeviceInfo = false;
var isSessionActive = false;
var isRequestSent = false;
var strWidthApp;
var strHeightApp;
var imageStyle = 0;
var orientationFlag = 0;
//var socket = new WebSocket("ws://mdm.kochar.co:8080/SocketService/websocket/Test2");
var socket = new WebSocket("ws://127.0.0.1:8000/socketsending");
socket.binaryType = 'arraybuffer';
socket.onopen =onOpen;
socket.onmessage = onMessage;
socket.onclose =onClose;
socket.onerror =onError;
//        function (e) {
//    var DeviceAction = {
//        Command: "stopSession",
//        SettingName: "",
//        description: "",
//        imei: _ImeiForMobileInSession
//    };
//    isSessionActive = false;
//    console.log(JSON.stringify(DeviceAction))
//    socket.send(JSON.stringify(DeviceAction));
//    clearInterval(timerId);
//    BindCloseSession();
//    $('#loading').hide();

//};

function onOpen(e) {
    console.log("my Connection Open: " + e);
    socketStart();
//     $('#btnNumberSubmit').click();
//     alert(1);
};

function onError(err) {
    console.error(err)
};

function onClose()
{
    console.log('isSessionActive in onClose function==='+isSessionActive);
    if(isSessionActive==true)
    {
socket = new WebSocket("ws://127.0.0.1:8000/socketsending"); //WebSocket("ws://54.171.35.140:8080/SocketService/websocket/Test2");
socket.binaryType = 'arraybuffer';
socket.onopen =onOpen;
socket.onmessage = onMessage;
socket.onclose =onClose;
socket.onerror =onError;

var DeviceAction = {
        reconnect: "true",
        imei: _ImeiForMobileInSession
    };
    console.log("in socket on close method==="+JSON.stringify(DeviceAction))
    socket.send(JSON.stringify(DeviceAction));
}
}
var divheight=0;
var divwidth=0;
function changediv(flag)
{
    if(flag=='P')
    {
    $('#imgDiv,#CurrentImage').css("height",divwidth);
    $('#imgDiv,#CurrentImage').css("width",divheight);
    }
    else
    {
    $('#imgDiv,#CurrentImage').css("height",divheight);
    $('#imgDiv,#CurrentImage').css("width",divwidth);
    }
}
$(document).ready(function () {
  divheight=$('#imgDiv').height();
  divwidth=$('#imgDiv').width();

//    setTimeout(changediv,3000);
    $('#loading').show();
    $('#Close_Loader_Process').click(function () {
        var DeviceAction = {
            Command: "stopSession",
            SettingName: "",
            description: "",
            imei: _ImeiForMobileInSession
        };
        isSessionActive = false;
        console.log("Sending Stop Command : " + JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
        console.log("Succesful Sent Stop Command : " + JSON.stringify(DeviceAction))
        clearInterval(timerId);
        BindCloseSession();
//        $('#loading').hide();

    });
    $(window).bind("beforeunload", function () {
        var DeviceAction = {
            Command: "stopSession",
            SettingName: "",
            description: "",
            imei: _ImeiForMobileInSession
        };
        isSessionActive = false;
        console.log("Sending Stop Command : " + JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
        console.log("Succesful Sent Stop Command : " + JSON.stringify(DeviceAction))
        clearInterval(timerId);
        BindCloseSession();
//        return confirm("Do you really want to close?");
    });

    $('#anchor_dashboard').click(function () {
        if (isDeviceInfo) {
            $(".div_advance").hide();
            $('#div_history_class_id').hide();
            $(".div_deviceinfo").show(1000);
        } else {
            var DeviceAction = {
                Command: "HandsetInfo",
                SettingName: "",
                description: "",
                X: 0,
                Y: 0,
                imei: _ImeiForMobileInSession
            };
            console.log(JSON.stringify(DeviceAction))
            socket.send(JSON.stringify(DeviceAction));
            alert("No Device Info Retrieved, Please try again later.");
        }
    });
    $("#btnNumberSubmit").click(function () {

    });

//    $('#remote_dashboard').click(function () {
//          var DeviceAction = {
//            Command: "Start Remote",
//            //commandName: "Home",
//            SettingName: "",
//            description: "",
//            X: 0,
//            Y: 0
//        };
//        $(".div_deviceinfo").hide();
//        $('#div_history_class_id').show();
//        $("#CurrentImage").css({height: "480px", width: "320px"});
//        TransactionTimer(true);
//    });

    $("#btnHome").click(function () {
        var DeviceAction = {
            Command: "Home",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnBack").click(function () {
        var DeviceAction = {
            Command: "Back",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnMenu").click(function () {
        var DeviceAction = {
            Command: "Menu",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnScrollLeft").click(function () {
        var DeviceAction = {
            Command: "ScrollLeft",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
//        alert("imei at scroll left=="+_ImeiForMobileInSession);
        console.log(JSON.stringify(DeviceAction));
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnScrollRight").click(function () {
        var DeviceAction = {
            Command: "ScrollRight",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnScrollUp").click(function () {
        var DeviceAction = {
            Command: "ScrollUp",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnScrollDown").click(function () {
        var DeviceAction = {
            Command: "ScrollDown",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#btnPower").click(function () {
        var DeviceAction = {
            Command: "Power",
            SettingName: "",
            description: "",
            X: 0,
            Y: 0,
            imei:_ImeiForMobileInSession
        };
        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });
    $("#advance_dashboard").click(function () {
        UpdateHeading("Advance Settings");
        ShowLoader(true);
        getOpenSettCat();
        ControlLeftTabPanel("4");
        ShowLoader(false);

    });

    $("#imgDiv").click(function (e) {

        var position = $("#imgDiv").position();
        console.log("e.pageX " + e.pageX + "  " + e.pageY);
        var widthtPage = e.pageX - $("#imgDiv").position().left;
        var heightPage = e.pageY - $("#imgDiv").position().top;
//        var widthtPage = e.pageX - ($("#asideHolder").position().left + $("#asideHolder").width() + 5);
//        var heightPage = e.pageY - ($("#headerHolder").position().top + $("#asideHolder").height() + 15);


//        console.log("strWidthApp " + strWidthApp)
//        console.log("strHeightApp " + strHeightApp)
        console.log("orientationFlag " + orientationFlag)
//        var X = parseInt((widthtPage * parseInt(strWidthApp)) / 320);
//        var Y = parseInt((heightPage * parseInt(strHeightApp)) / 480);
        var X, Y;
        if (orientationFlag == 1 || orientationFlag == 3) { // lenovo portrait //landscape
            X = parseInt((widthtPage / $("#imgDiv").width()) * parseInt(strWidthApp));
            Y = parseInt((heightPage / $("#imgDiv").height()) * parseInt(strHeightApp));
        } else if (orientationFlag == 0 || orientationFlag == 2) { // lenovo landscape  potrait
//            Y = parseInt((widthtPage / $("#imgDiv").width()) * parseInt(strWidthApp));
//            X = parseInt((heightPage / $("#imgDiv").height()) * parseInt(strHeightApp));

            X = parseInt((widthtPage / $("#imgDiv").width()) * parseFloat(strHeightApp));
            Y = parseInt((heightPage / $("#imgDiv").height()) * parseFloat(strWidthApp));
            //Y = (parseFloat(strWidthApp) - Y);
        }

//        printLogs("e.pageX", e.pageX, "e.pageY", e.pageY, "$(#imgDiv)position().left", $("#imgDiv").position().left, "$(#imgDiv).position().top", $("#imgDiv").position().top, "widthtPage", widthtPage, "heightPage", heightPage);
           console.log('device x====='+X+"  Y==============="+Y+" Device height======="+strHeightApp+" Device width======="+strWidthApp);
//        var X = parseInt((widthtPage * parseInt(strWidthApp)) / 320);
//        var Y = parseInt((heightPage * parseInt(strHeightApp)) / 480);
        console.log("WidthtPage " + widthtPage + " Height Page " + heightPage + " X: " + X + " Y: " + Y + " strWidthApp: " + strWidthApp + " strHeightApp: " + strHeightApp)
        var DeviceAction = {
            Command: "Coordinates",
            SettingName: "",
            description: "",
            X: X,
            Y: Y,
            ImageDebug:true,
            ImageQuality:75,
            imei:_ImeiForMobileInSession
        };

        console.log(JSON.stringify(DeviceAction))
        socket.send(JSON.stringify(DeviceAction));
    });

    $('#ddl_settings_category').change(function ()
    {

        var catId = $('#ddl_settings_category option:selected').val();
        if (catId == '--Select--') {
            alert("Please Select Valid Category");
        } else {
//            var modelId = $('#idDeviceNameModelId option:selected').val().split('~')[1];
            var modelId = "227";
            var allVal = new Array();
            allVal[0] = "getOpenSettSubCat";
            allVal[1] = catId;
            allVal[2] = modelId;
            var dataString = 'allVal=' + allVal + '&search_name=' + 0;
            var script_url = '../GetHandsetSettingCategory_Servlet';
            $.ajax({
                type: 'POST',
                url: script_url,
                data: dataString,
                success:
                        function (data) {
                            var responseData = $.trim(data);
                            if (responseData == "" || responseData == null || responseData == "{}" || responseData == '{"OpenSettSubCat":]}') {
                            } else {
                                var base_html = "";
                                var arr = JSON.parse(responseData);
                                if (arr.OpenSettSubCat !== null) {
                                    for (var i = 0; i < arr.OpenSettSubCat.length; i++)
                                    {
//                                        base_html += '<option value="' + arr.OpenSettSubCat[i].SubCatId + '~' + arr.OpenSettSubCat[i].SubCatAbbr + '~' + arr.OpenSettSubCat[i].ImageName + '" id="' + arr.OpenSettSubCat[i].SubCatId + '" >' + arr.OpenSettSubCat[i].SubCatName + '</option>';
                                        base_html += '<option value="' + arr.OpenSettSubCat[i].SubCatAbbr + '" id="' + arr.OpenSettSubCat[i].SubCatId + '" >' + arr.OpenSettSubCat[i].SubCatName + '</option>';
                                    }
                                    $("#ddl_settings_subcategory").html(base_html);
                                    $("#html_settings_subcategory").parent().show();
                                    $("#btn_executesettings").parent().show();

                                }
                            }
                        }
            });
        }


    });
    $("#btn_executesettings").click(function () {
        if (CheckForNull("", "ddl_settings_subcategory")) {
            var settingsname = $("#ddl_settings_subcategory").val();
            if (settingsname != "0") {
//                BindSendSettingsCommand(settingsname);
                var DeviceAction = {
                    Command: "Setting",
                    SettingName: settingsname,
                    description: "",
                    X: 0,
                    Y: 0,
                    imei:_ImeiForMobileInSession
                };
                console.log(JSON.stringify(DeviceAction))
                socket.send(JSON.stringify(DeviceAction));
            }
        } else {
            RaiseError("Please select sub-settings");
        }
    });
});

function onMessage(event) {
    if (event.data instanceof ArrayBuffer) {
        var arrayBuffer = event.data;

        var bytes = new Uint8Array(arrayBuffer);

        var image = document.getElementById('CurrentImage');
//        console.log("Image Type " + bytes[0]);
//        console.log(encode(bytes));
        orientationFlag = bytes[0];
//        var position = $("#imgDiv").position();
        console.log("orientationFlag " + orientationFlag);
//        var widthtPage = parseInt(($("#imgDiv").width()/2)) - $("#imgDiv").position().left;
//        var heightPage = parseInt(($("#imgDiv").height()/2))- $("#imgDiv").position().top;




        if (orientationFlag == 1 || orientationFlag == 3)
        { // lenovo portrait
            changediv('L');

//            X = parseInt((widthtPage * parseInt(strHeightApp)) / $("#imgDiv").width());
//            Y = parseInt((heightPage * parseInt(strWidthApp)) / $("#imgDiv").height());
        } else if (orientationFlag == 0 || orientationFlag == 2)
        { // lenovo landscape
        changediv('P');
//                 X = parseInt(((widthtPage / $("#imgDiv").width()) * parseInt(strWidthApp)));
//            Y = parseInt(((heightPage / $("#imgDiv").height()) * parseInt(strHeightApp)));
        }

//        if (bytes[0] == 0 || bytes[0] == 2)
//        {
//
////            $('#imgDiv').css("height", "480px");
////            $('#imgDiv').css("width", "720px");
////            $('#imgDiv').css("height", "500px");
////            $('#imgDiv').css("width", "300px");
////            $('#CurrentImage').css("height", "500px");
////            $('#CurrentImage').css("width", "300px");
////            $('#imgDiv').removeClass("rotate-90")
////            $('#imgDiv').addClass("rotate-90")
////            $('#imgDiv').addClass("rotate90")
//        } else if (bytes[0] == 1 || bytes[0] == 3)
//        {
////            $('#imgDiv').css("height", "720px");
////            $('#imgDiv').css("width", "480px");
////            $('#imgDiv').css("height", "300px");
////            $('#imgDiv').css("width", "500px");
////            $('#CurrentImage').css("height", "300px");
////            $('#CurrentImage').css("width", "500px");
////            $('#imgDiv').addClass("rotate90")
//        }

//        else if (bytes[0] == 2)
//        {
//            $('#imgDiv').css("height", "480px");
//            $('#imgDiv').css("width", "720px");
//        } else {
//            $('#imgDiv').css("height", "720px");
//            $('#imgDiv').css("width", "480px");
//
//        }
        image.src = 'data:image/png;base64,' + encode(bytes);
    } else if (event.data instanceof Blob) {
    } else {
        console.log("event.data==="+event.data);
        var recData = JSON.parse($.trim(event.data));
        if(recData.Command=="download File")
        {

var currentDate = new Date();
var currentDayOfMonth = currentDate.getDate();
var currentMonth = currentDate.getMonth(); // Be careful! January is 0, not 1
var currentYear = currentDate.getFullYear();
var dateString = currentDayOfMonth + "-" + (currentMonth + 1) + "-" + currentYear;
var timeString=currentDate.getHours()+":"+currentDate.getMinutes()+":"+currentDate.getSeconds();
console.log(dateString+' '+timeString);
//$('#filediv').append('<div class="mycontainer"><a target="_blank" href="'+recData.fileURL+'"><img src="dd.jpg" alt="Avatar" class="right" style="width:50px;border-radius:30px"><p>'+recData.fileName+'</p><span class="time-left">'+dateString+' '+timeString+'span></a></div>');

        }
        if (recData.Command != undefined) {
            isDeviceInfo = true;

//            console.log(event.data + " ")
            $('#loading').hide();

            CreateHandsetInfoHtml(recData);
            SessionTimer(true);
        }

        else if (recData.response != undefined) {
            if (recData.response == "Ok") {
                if (isRequestSent) {
//                    console.log("Caling session Timer on" + recData)
//                    SessionTimer(true);
//                    $('#welcomewindow').animate({'left': '-100%'}, 500);
//                    $('#mainwindow').show().animate({'left': '0%'}, 500);

                    isRequestSent = false;
//                    SessionTimer(true);
                    console.log("Inside respoonse Ok1");
                    $('#remote_dashboard').click();
                } else {
                    $('#loading').hide();
                    console.log("Inside respoonse Ok2")
                }
            }
        } else {
            console.log("Else")
        }
    }

}

function addDevice(name, SettingName, description) {
    var DeviceAction = {
        Command: "add",
        name: name,
        SettingName: SettingName,
        description: description,
        imei:_ImeiForMobileInSession
    };
    socket.send(JSON.stringify(DeviceAction));
}

function removeDevice(element) {
    var id = element;
    var DeviceAction = {
        Command: "remove",
        id: id,
        imei:_ImeiForMobileInSession
    };
    socket.send(JSON.stringify(DeviceAction));
}

function toggleDevice(element) {
    var id = element;
    var DeviceAction = {
        Command: "toggle",
        id: id,
        imei:_ImeiForMobileInSession
    };
    socket.send(JSON.stringify(DeviceAction));
}

function printDeviceElement(device) {
    console.log("PrintDevice Element " + device)
//    var content = document.getElementById("content");
//
//    var deviceDiv = document.createElement("div");
//    deviceDiv.setAttribute("id", device.id);
//    deviceDiv.setAttribute("class", "device " + device.SettingName);
//    content.appendChild(deviceDiv);
//
//    var deviceName = document.createElement("span");
//    deviceName.setAttribute("class", "deviceName");
//    deviceName.innerHTML = device.name;
//    deviceDiv.appendChild(deviceName);
//
//    var deviceType = document.createElement("span");
//    deviceType.innerHTML = "<b>Type:</b> " + device.SettingName;
//    deviceDiv.appendChild(deviceType);
//
//    var deviceStatus = document.createElement("span");
//    if (device.status === "On") {
//        deviceStatus.innerHTML = "<b>Status:</b> " + device.status + " (<a href=\"#\" OnClick=toggleDevice(" + device.id + ")>Turn off</a>)";
//    } else if (device.status === "Off") {
//        deviceStatus.innerHTML = "<b>Status:</b> " + device.status + " (<a href=\"#\" OnClick=toggleDevice(" + device.id + ")>Turn on</a>)";
//        //deviceDiv.setAttribute("class", "device off");
//    }
//    deviceDiv.appendChild(deviceStatus);
//
//    var deviceDescription = document.createElement("span");
//    deviceDescription.innerHTML = "<b>Comments:</b> " + device.description;
//    deviceDiv.appendChild(deviceDescription);
//
//    var removeDevice = document.createElement("span");
//    removeDevice.setAttribute("class", "removeDevice");
//    removeDevice.innerHTML = "<a href=\"#\" OnClick=removeDevice(" + device.id + ")>Remove device</a>";
//    deviceDiv.appendChild(removeDevice);
}

function showForm() {
    document.getElementById("addDeviceForm").style.display = '';
}

function hideForm() {
    document.getElementById("addDeviceForm").style.display = "none";
}

function formSubmit() {
    var form = document.getElementById("addDeviceForm");
    var name = form.elements["device_name"].value;
    var SettingName = form.elements["device_type"].value;
    var description = form.elements["device_description"].value;
    hideForm();
    document.getElementById("addDeviceForm").reset();
    addDevice(name, SettingName, description);
}

function init() {
//    hideForm();
}





function ShowLoader(swtch) {
    if (swtch)
        $("#loading").slideDown(500);
    else
        $("#loading").slideUp(500);
}

function UpdateHeading(headingname) {
    if (CheckForNull(headingname))
        $(".heading").html(headingname);
    else
        $(".heading").html("");
}

function ControlLeftTabPanel(id) { //It will show the tab whose id will be provided
    $(".div_common_class").hide(500); //first hide all div
    switch (id) {
        case "1":
            $(".div_deviceinfo").show(1000);
            break;
        case "2":
            $(".div_completediagnostic").show(1000);
            break;
        case "3":
            $(".div_applicationinfo").show(1000);
            break;
        case "4":
            $(".div_advance").show(1000);
            break;
        case "5":
            $(".div_history").show(1000);
            break;
        case "7":
            $(".div_troubleshoot").show(1000);
            break;
        default:
            $(".div_common_class").hide(500);
            break;
    }
}


function ResetArray() {
    _arrayDataHolder = [];
}


function CheckForNull(value, id_element) {
    if (id_element != "" & id_element != undefined) {
        value = $("#" + id_element).val();
    }
    if (value == "" || value == null || value == undefined || value == "0")
        return false;
    return true;
}

function encode(input) {
    var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    var output = "";
    var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
    var i = 1;
    var count = input.length;
//    input = input.split("#")[1];

    while (i < input.length) {
        chr1 = input[i++];
        chr2 = i < input.length ? input[i++] : Number.NaN; // Not sure if the index
        chr3 = i < input.length ? input[i++] : Number.NaN; // checks are needed here

        enc1 = chr1 >> 2;
        enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
        enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
        enc4 = chr3 & 63;

        if (isNaN(chr2)) {
            enc3 = enc4 = 64;
        } else if (isNaN(chr3)) {
            enc4 = 64;
        }
        output += keyStr.charAt(enc1) + keyStr.charAt(enc2) +
                keyStr.charAt(enc3) + keyStr.charAt(enc4);
    }
    console.log("output " + output)
    return output;
}



function UpdateControl(val, ulclassname, parentclassname) {

    $("ul.offOnBtn." + ulclassname + " li").removeClass("on");
    $("ul.offOnBtn." + ulclassname + " li").each(function () {
        var current = $(this).attr('data-value');
        if (val == current) {
            $(this).addClass("on");
        }
    });
    if (val == "true") {//On
        var path = $("ul.offOnBtn." + ulclassname + " li").parents().find(".box-adHolder." + parentclassname).find(".imgHolder img").attr("src");
        var a1 = path.split("/");
        var a2 = a1[4].split(".");
        var a3 = a2[0].split("-");
        var pathInput = Constants.ImagePath + "/Content/images/icon-" + a3[1] + "-active.png";
        $("." + ulclassname).parents().find("." + parentclassname + ".box-adHolder").find(".imgHolder img").attr("src", pathInput);
    } else {//Off
        var path = $("ul.offOnBtn." + ulclassname + " li").parents().find(".box-adHolder." + parentclassname).find(".imgHolder img").attr("src");
        var a1 = path.split("/");
        var a2 = (a1[3].split(".") == "images" ? a1[4].split(".") : a1[3].split("."));
        var a3 = a2[0].split("-");
        var pathInput = Constants.ImagePath + "/Content/images/icon-" + a3[1] + ".png";
        $("." + ulclassname).parents().find("." + parentclassname + ".box-adHolder").find(".imgHolder img").attr("src", pathInput);
    }
}

function getOpenSettCat()
{
    var allVal = new Array();
    allVal[0] = "getOpenSettingsCat";
    var dataString = 'allVal=' + allVal + '&search_name=' + 10673;
    var script_url = '../GetHandsetSettingCategory_Servlet';
    $.ajax({
        type: 'POST',
        url: script_url,
        data: dataString,
        success:
                function (data) {
//                    $('#SettCatName').html("");
//                    $('#SettCatName').html("<option val=" + "--Select--" + " >--Select--</option>");
                    var responseData = $.trim(data);
                    if (responseData == "" || responseData == null || responseData == "{}" || responseData == '{"OpenSettCat":]}') {
                    } else {
                        var arr = JSON.parse(responseData);
                        if (arr.OpenSettCat !== null) {
//                            for (var i = 0; i < arr.OpenSettCat.length; i++)
//                            {
//                                $('#SettCatName').append('<option value="' + arr.OpenSettCat[i].CatId + '" id="' + arr.OpenSettCat[i].CatId + '">' + arr.OpenSettCat[i].CatName + '</option>');
//                            }
                            var base_html;
//                            var base_html = "<select id='ddl_settings_subcategory' class='html_ddl_settings form-control input-sm'><option value='0'>--Select Subcategory--</option>";
                            for (var i = 0; i < arr.OpenSettCat.length; i++)
                            {
                                base_html += '<option value="' + arr.OpenSettCat[i].CatId + '" id="' + arr.OpenSettCat[i].CatId + '" >' + arr.OpenSettCat[i].CatName + '</option>';

                            }
                            base_html += "</select>";
                            $("#ddl_settings_category").html(base_html);
                            $("#html_settings_category").parent().show();
                        }
                    }
                }
    });
}
function printLogs(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
{
    console.log(p1 + " " + p2 + " " + p3 + " " + p4 + " " + p5 + " " + p6 + " " + p7 + " " + p8 + " " + p9 + " " + p10 + " " + p11 + " " + p12)
}

function socketStart()
{
//    console.log('called==='+globalimei);
    $('#filediv').html('');
        $('#filediv').html('<h2>File List</h2>');
         $('#CurrentImage').attr('src','../Content/images/ScreenShotSmall.jpg');
//        _ImeiForMobileInSession = $.trim($("#number").val()); //Store the number in global variable
//        myimei=$.trim($("#number").val());
//        socket = new WebSocket("ws://localhost:8080/KTRMS/websocket/Test2?imei="+_ImeiForMobileInSession);

//        _ImeiForMobileInSession = globalimei;
//            pingDevice(true);
//            console.log("myimei==="+myimei);
//        if (_ImeiForMobileInSession != '') {
            var DeviceAction = {
                Command: "startSession",
                imei: _ImeiForMobileInSession,
                msisdn: "9876543210",
                SettingName: "",
                description: ""
            };
            console.log(JSON.stringify(DeviceAction))
            socket.send(JSON.stringify(DeviceAction));
            if (!_sessionStarted) {
//                $('#loading').show();
                console.log("Inside Main button click");
                isSessionActive = true;
                isRequestSent = true;
                $('.callNumber').html(_ImeiForMobileInSession);

//            SessionTimer(true);
//            $('#welcomewindow').animate({'left': '-100%'}, 500);
//            $('#mainwindow').show().animate({'left': '0%'}, 500);
            }
//        } else {
//            alert("Please specify IMEI");
//        }
}

