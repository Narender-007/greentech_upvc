/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function enbaleDisableCard(e)
{
    $('#c1,#c2,#c3').removeClass('active');
         $(e).addClass('active');
    
}

$(document).ready(function () 
{
    
     $('#c1,#c2').click(function()
     {
         enbaleDisableCard(this);
         
     });
      $('#token').text(_ImeiForMobileInSession);

    
    $('#c3').click(function()
    {
        enbaleDisableCard(this);
         $( "#dialog" ).html('');
        $( "#dialog" ).dialog({height:500,width:750});
        takeshot();
       
//var save = document.createElement('a');
//save.href = $('#CurrentImage').attr('src');
//save.target = '_blank';
//save.download = 'photo.jpg'
//save.click();
//var event = document.createEvent('Event');
//event.initEvent('click', true, true);
//save.dispatchEvent(event);
//(window.URL || window.webkitURL).revokeObjectURL(save.href);
    });
    
    
    $('#sendfile').click(function()
    {
       HostFile();  
    });
     
});

function HostFile()
{
    if(document.getElementById('file').files.length<=0)
    {
        alert('Please select eert file');
        return;
    }
    var fileInput=document.getElementById('file');
    var file = fileInput.files[0];
    var filename=file.name;
    alert(filename)
    var formData = new FormData();
    formData.append('filename', file);
    formData.append('imei',_ImeiForMobileInSession);
//    alert(myimei);

    $.ajax({
        //url: 'http://localhost:8080/RemoteMaxService_Aman/HostFile',
        url: 'http://54.171.35.140:8080/SocketService/HostFile',
        type: 'POST',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) 
        {
var currentDate = new Date();
var currentDayOfMonth = currentDate.getDate();
var currentMonth = currentDate.getMonth(); // Be careful! January is 0, not 1
var currentYear = currentDate.getFullYear();
var dateString = currentDayOfMonth + "-" + (currentMonth + 1) + "-" + currentYear;
var timeString=currentDate.getHours()+":"+currentDate.getMinutes()+":"+currentDate.getSeconds();
            $('#filediv').append('<div class="mycontainer"><p>Send File'+filename+' </p><span class="time-left">'+dateString+' '+timeString+'</span></div>');
           
        }});
       
}


//Display Screen shot click on automatically 

function takeshot() {
    debugger;
  const captureElement = document.querySelector('#CurrentImage')
  html2canvas(captureElement).then(canvas => {
      canvas.style.display = 'block'
      document.body.appendChild(canvas)
      return canvas
  })
          .then(canvas => {
              const image = canvas.toDataURL('image/png').replace('image/png', 'image/octet-stream')
      const a = document.createElement('a')
      a.setAttribute('download', 'Remote-Session-ScreenShot.png')
      a.setAttribute('href', image)
      a.click()
      canvas.remove()
  })
}

const btn = document.querySelector('#dailog')
btn.addEventListener('click', capture)



// after session completed click on stopsession tab will closed
//
//function close_tab() {
//  if (confirm("Do you want to close this tab?")) {
//    window.close();
//  }
//}


// web through android send to file progess 

//var i = 0;
//function move() {
//  if (i == 0) {
//    i = 1;
//    var elem = document.getElementById("myBar");
//    var width = 10;
//    var id = setInterval(frame, 10);
//    function frame() {
//      if (width >= 100) {
//        clearInterval(id);
//        i = 0;
//      } else {
//        width++;
//        elem.style.width = width + "%";
//        elem.innerHTML = width  + "%";
//      }
//    }
//  }
//}


//function takeshot() 
//{ 
//            let div =  document.getElementById('CurrentImage'); 
//            html2canvas(div).then( 
//
//                function (canvas) { 
//                    document.getElementById('dialog').appendChild(canvas); 
//                }) 
//
//        }
        
