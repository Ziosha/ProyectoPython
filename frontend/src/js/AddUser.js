let adduser = document.getElementById('adduser'),
    rootAddUser = document.getElementById('root')


adduser.addEventListener('click', () =>{
    rootAddUser.innerHTML = null
    rootAddUser.innerHTML = `
    <div class="form">
    <h1 style="text-align: center">Registro</h1>
      <input type="text" name="nombre" placeholder="Nombres" size="40" id="nom" required/>
      <input type="text" name="apellidoP" placeholder="Apellido Paterno" size="40" id="ap" required/>
      <input type="text" name="apellidoM" placeholder="Apellido Materno" size="40" id="am" required/>
      <input type="text" name="pais" placeholder="Pais" size="40" id="pais" required/>
      <input type="password" name="pass" placeholder="Contraseña" size="40" id="pass" required/>
      <input type="text" name="telefono" placeholder="Telefono" size="40" id="phone" required/>
      <input type="email" name="email" placeholder="E-mail" size="40" id="email" required/>
      <input type="reset" value="Enviar" id="send" />
  </div>
    `
    let nom = document.getElementById('nom'),
        ap = document.getElementById('ap'),
        am = document.getElementById('am'),
        pass = document.getElementById('pass'),
        phone = document.getElementById('phone'),
        email = document.getElementById('email'),
        pais = document.getElementById('pais'),
        send = document.getElementById('send')

    send.addEventListener('click', () => {
        var data = {
            Nombre_usuario : nom.value,
            Apellido_Paterno : ap.value,
            Apellido_Materno : am.value,
            Pais : pais.value,
            Correo : email.value,
            Contraseña : pass.value,
            Telefono : phone.value
            
          }                
            
          const addUsers = fetch("http://localhost:3000/usuario",{
                  method : 'POST',
                  body:  JSON.stringify(data),
                  headers:{'Content-Type': 'application/json'}
              })
              addUsers.then(res => res.json())
                      .then(data => {
                          if(data.statusCode = 200)
                          {
                              alert("Producto registrado")
                          }
                          else {alert("error al registrar producto")}
          
                      })
                      .catch(error => console.log(error))

    })
        



} )