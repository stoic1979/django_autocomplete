function resetCustomerForm() {
    /* 
     * reset/empty customer form fields
     */
    $("#id_email").val("");
    $("#id_address_street").val("");
    $("#id_address_house").val("");
    $("#id_address_flat").val("");
    $("#id_address_postal_code").val("");
    $("#id_address_comment").val("");
}

function getCustomer() {
    /* 
     * sending AJAX request to fetch customer data
     */
    var p = $("#id_phone").val();
    $.get( "/customer_lookup/" + p, function( data ) {
        var obj = jQuery.parseJSON(data);
        if(obj.length == 0) {
            resetCustomerForm();
            return;
        }

        // setting fields of customer form
        var customer = obj[0].fields;
        $("#id_email").val(customer.email);
        $("#id_address_street").val(customer.address_street);
        $("#id_address_house").val(customer.address_house);
        $("#id_address_flat").val(customer.address_flat);
        $("#id_address_postal_code").val(customer.address_postal_code);
        $("#id_address_comment").val(customer.address_comment);
        $("#id_phone").val(customer.phone);
    });
}

$(document).ready(function() {

    // resetting form when phone becomes empty
    $('#id_phone').on('keyup',function(e){
        var p = $("#id_phone").val();
        if(!p.length) {
            resetCustomerForm();
            return;
        }
    });

    // sending AJAX request to get all phones
    $.get( "/get_phones/", function( data ) {
        var availablePhones = jQuery.parseJSON(data);
        $("#id_phone").autocomplete({
            source: availablePhones,
            close: getCustomer
        });
    });

});//ready


///////////////////////////////////////////////////////////////////////////////
//   ADDRESS AUTOCOMPLETE CODE FOLLOWS
///////////////////////////////////////////////////////////////////////////////

// convenience function to dump a javascript variable
function dumpObject(object) {
    var output = '';
    for (var property in object) {
        output += property + ': ' + object[property]+'; \n';
    }
    alert(output);
}

// initializing geocomplete 
$(function(){
    $("#geocomplete").geocomplete({
        details: "form",
        types: ["geocode", "establishment"],
    });
});

// event handler when getting address result
$("#geocomplete")
    .geocomplete()
    .bind("geocode:result", function(event, result){

        var house   = result.address_components[0].short_name;
        var street  = result.address_components[1].long_name;
        var flat    = result.address_components[2].long_name;
        var city    = result.locality;
        var state   = result.administrative_area_level_1;
        var country = result.country;

        // Zip is the last element inside the address components of Google API result
        var zip = result.address_components[result.address_components.length - 1].long_name;

        $("#id_address_street").val(street);
        $("#id_address_house").val(house);
        $("#id_address_flat").val(flat);
        $("#id_address_postal_code").val(zip);

        // checking address components
        //for(i=0; i< result.address_components.length; i++) {
        //dumpObject(result.address_components[i]);
        //}

});
