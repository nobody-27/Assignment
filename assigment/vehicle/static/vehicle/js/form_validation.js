 

$("#modal-popup").on("click",function(e){
  $('#myModal').modal('show');
});


// add 
document.getElementById("saveing").addEventListener("click",function(e){
  var vehicle_number = $('#vehicle_number').val()
  var vehic_type = $('#types').val()
  var vehicl_model = $('#model').val()
  var desc  = $('#description').val()

  //validation
  if (vehicle_number == "" ||  vehicl_model == "" || desc == ""){
      $('#myModal').modal('show');
      var alert_mess = document.getElementById('message')
      alert_mess.innerHTML = "All Filed Manadetory"
  }

  else{
    $.ajax({
      type: 'POST',
      url: '/add-vehicle/',
      data : {
        number : vehicle_number,
        vehicle_type : vehic_type,
        vehicle_model : vehicl_model,
        description : desc,
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
      },
      success: function(data){
        console.log(data)
        location.reload()
      }
    });
  }
});


//get vehicle details
async function vehicle_details_by_id(id){
  const result  = await fetch('/get-vehicle-details/' + id + '/')
  const data = await result.json()
  return data
}


// edit showing in modal
async function edit(edit_id){
  var obj = await vehicle_details_by_id(edit_id)
  document.getElementById('edit_vehicle_number').value = obj.vehicle_obj.number
  document.getElementById('edit_types').value = obj.vehicle_obj.type
  document.getElementById('edit_model').value = obj.vehicle_obj.model
  document.getElementById('edit_description').value = obj.vehicle_obj.description
  document.getElementById('vehicle_id').value = obj.vehicle_obj.id
  $('#Edit').modal('show');
}


//




document.getElementById('test').addEventListener("click",function(e){


  var vehic_type = $('#edit_types').val()
  var vehicle_number = $('#edit_vehicle_number').val()
  var vehicl_model = $('#edit_model').val()
  var desc  = $('#edit_description').val()
  var id = $('#vehicle_id').val()


  

  if (vehicle_number == "" ||  vehicl_model == "" || desc == ""){
      $('#Edit').modal('show');
      var alert_mess = document.getElementById('message-error')
      alert_mess.innerHTML = "All Filed Manadetory"
  }
  else {
    $.ajax({
      type: 'POST',
      url: '/edit-vehicle/',
      data : {
        id : id,
        number : vehicle_number,
        vehicle_type : vehic_type,
        vehicle_model : vehicl_model,
        description : desc,
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
      },
      success: function(data){
        location.reload()
      }
    });
  }


})



// delete
async function delete_vehicle(delete_id){
  var data = confirm(`Are You Sure to delete ${delete_id}`);
  if (data == true){
    $.ajax({
    type: 'POST',
    url: '/delete-vehicle/' + delete_id + '/',
    data : {
      id : delete_id,
      csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function(data){
      console.log(data)
      location.reload()
    }
  });
  }
}




