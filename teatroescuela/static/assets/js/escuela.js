function loading(config) {

  var temp = ''
  temp += '<div class="text-center">'
  // temp += '<div><i class="fas fa-spinner fa-pulse fa-3x"></i></div>'
  temp += '<div><i class="fas fa-theater-masks fa-pulse fa-3x"></i></div>'
  temp += '<h1>@title<h1>'
  temp += '<p>@decription</p>'
  temp += '</div>'
  temp = temp.replace(/@title/g, config.title == null ? 'Por favor espere' : config.title);
  temp = temp.replace(/@decription/g, config.description == null ? '' : config.description);

  if (config.active) {
    $.blockUI({
      message: temp,
      css: {
        backgroundColor: 'none',
        color: '#fff',
        border: 'none',
      }
    });
  } else {
    $.unblockUI();
  }
}


$.validator.addMethod("rut", function(value, element) {
    var status = true;
    if (!$.validateRut(value)) {
        status = false
    }
    return status;
}, 'R.U.T. inválido.');
