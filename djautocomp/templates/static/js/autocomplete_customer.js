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
