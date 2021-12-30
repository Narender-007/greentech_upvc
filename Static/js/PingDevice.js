$(document).ready(function () 
{
    $('#remote_dashboard').click(function()
    {
        $(".div_deviceinfo").hide();
        $('#div_history_class_id').show();
//        pingDevice(true);
//        $("#CurrentImage").css({height: "480px", width: "320px"});
//        TransactionTimer(true);
    });
    
    
    
});
function pingDevice(devicestatus)
{
       
    console.log("imei==="+ $('#number').val()+" global variable===="+_ImeiForMobileInSession);
    $.ajax({
                type: 'POST',
                url: '../PingDevice',
                data:{imei: _ImeiForMobileInSession,status:devicestatus},
                success: function (data) 
                {
                     $('#date').text(data);   
                        
                }});

}


