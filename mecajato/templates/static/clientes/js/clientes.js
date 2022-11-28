function add_carro(){

    container = document.getElementById("form-carro")

    html = `
    <br>
    <div class='row'>
        <div class='col-md py-2'> 
            <input type='text' placeholder='carro' class='form-control' name='carro'>
        </div> 
        <div class='col-md py-2'>
            <input type='text' placeholder='Placa' class='form-control' name='placa'>
        </div>
        <div class='col-md py-2'>
            <input type='number' placeholder='Ano' class='form-control' name='ano'>
        </div>
    </div>
    `;
    
    "<br><div class='row'> <div class='col-md py-2'> <input type='text' placeholder='carro' class='form-control' name=''></div> <div class='col-md py-2'><input type='text' placeholder='Placa' class='form-control'> </div></div>"

    container.innerHTML += html


}