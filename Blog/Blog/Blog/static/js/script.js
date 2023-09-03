function lajkujPost(id_posta) {
    $.ajax({
        url: '/lajkuj/',
        data: {
            'id_posta': id_posta,
            'csrfmiddleware token': "{{ csrf_token }}"
        },
        type: 'post',
        success: function(response) {
            $('#id_lajki').text(response.lajki_total);
        }
    });
}
