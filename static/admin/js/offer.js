$(function() {
    $("#offer-default-dt").DataTable({
        "responsive": true,
        "autoWidth": false,
        "pageLength": 50,
        "order": [
            [0, "asc"]
        ],
    });
    $("#offer-desc-dt").DataTable({
        "responsive": true,
        "autoWidth": false,
        "pageLength": 50,
        "order": [
            [0, "desc"]
        ],
    });

    $("#offer-offers-dt").DataTable({
        "responsive": true,
        "autoWidth": false,
        "pageLength": 50,
        "order": [
            [1, "desc"]
        ],
    });

    $('#example2').DataTable({
        "paging": true,
        "lengthChange": false,
        "searching": false,
        "ordering": true,
        "info": true,
        "autoWidth": false,
        "responsive": true,
    });
});


$(function() {
    $('[data-toggle="tooltip"]').tooltip()
})

// Doucment Ready Functions

$(document).ready(function() {

    // Initialize Select 2
    $('.fire_select2').select2({
        allowClear: true,
        placeholder: 'Select an option'
    });

    // Initialize Select 2 Multiple
    $('.fire_select2_multiple').select2({
        allowClear: true,
        multiple: true,
        placeholder: 'Select an option'
    });

    // Function Call
    getAffiliateTrackingLink();

    // Offer Approval Private Call

    $("#offerform_offer_approval").change(function() {
        if ($("#offerform_offer_approval").val() == '3') {
            $('#offer_approval_private').css('display', 'block');
            $('#offer_approval_private_mode').css('display', 'block');
            $('#offerform_offer_private_affiliates').attr('required', 'required');
        } else {
            $('#offer_approval_private').css('display', 'none');
            $('#offer_approval_private_mode').css('display', 'none');
            $('#offerform_offer_private_affiliates').removeAttr('required');
        }
    });
});


// Functions


function getAffiliateTrackingLink() {
    var subdomain = $('#subdomain').val();
    var offer_id = $('#offer_id').val();
    var affiliate_id = $('#offerdetail_affiliate_id').val();

    $.ajax({
        type: "POST",
        url: subdomain + "user/ajax/get_affiliate_tracking_link",
        datatype: "json",
        data: { 'offer_id': offer_id, 'affiliate_id': affiliate_id, },
        // async: false,
        success: function(data) {
            var data = $.parseJSON(data);
            if (affiliate_id == null || affiliate_id == '') {
                $('#offerdetail-affiliate-tracking-link-textarea').text('');
            } else {
                $('#offerdetail-affiliate-tracking-link-textarea').text(data.trackinglink);
            }

        },
    });
}


// chart
 

// const labels = [
//   {% for i in click %} '{{i.id}}', {% endfor %}
// ];
// const data = {
//   labels: ['{% for i in click %} {{i.id}}, {% endfor %}'],
//   datasets: [{
//     label: 'clicks',
//     backgroundColor: 'transparent',
//     borderColor: 'rgb(255, 47, 15)',
//     data: [{% for i in click %} {{i.id}}, {% endfor %}],
//   },{
//     label: 'conversion',
//     backgroundColor: 'transparent',
//     borderColor: 'rgb(66, 126, 245)',
//     data: [{% for i in conversion %} {{i.id}} ,{% endfor %}],
//   }]
// };
// const config = {
//   type: 'line',
//   data,
//   options: {}
// };

//  var myChart = new Chart(
//     document.getElementById('myChart'),
//     config
//   );