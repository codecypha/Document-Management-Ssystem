$(document).ready(function()
{
var $select1 = $("#vendorid");
    $select2 = $("#bankid");
    $options =$select2.find('option');
    $select1.on('change', function()
  { 
     $select2.html($options.filter('[value ="'+this.value+'"]'));
     $('#select2 :selected').text();
  }).trigger('change');
});

// $(document).ready(function(){ 
//   $('#submit').click(function(){ 
//    console.log($('#vendorid').val());
//    console.log($('#bankid').val());
//   console.log($('#select2 :selected').text());
//    });
// });