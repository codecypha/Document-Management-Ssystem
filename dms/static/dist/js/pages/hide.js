

function Hide() 
{
      if(document.getElementById('retention_id').options[document.getElementById('retention_id').selectedIndex].value != "Inactive") 
      {
          //  document.getElementById('id_port_permission_moc').style.display = '';
           document.getElementById('retention').value = 'block';
           document.getElementById('retention').style.display = 'none';
      } 
      else if (document.getElementById('retention_id').options[document.getElementById('retention_id').selectedIndex].value == "Inactive") 
      {
           document.getElementById('retention').style.display = '';
          //  document.getElementById('id_port_permission_moc').style.display = '';
           document.getElementById('retention').value = 'none';
      }
      else
      {
        document.getElementById('retention').value = 'block';
        document.getElementById('retention').style.display = 'none';
      }
}
window.onload = function() {
    document.getElementById('retention_id').onchange = Hide;
    
};




