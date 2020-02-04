$(function() {
    // SEND REQUEST TO OUR API FOR CUPCAKE LIST
    async function getCupcakes() {
        let resp = await axios.get('localhost:5000/api/cupcakes');
        return resp.data;
    }
    // APPEND TO UL
    async function addCupcakesToDom() {
        let resp = await getCupcakes();
        for (cupcake in resp) {
            $('#cupcake-list').append('<li>'+cupcake.flavor+'</li>')
        }
        
    }

    addCupcakesToDom()
    //ADD EVENT HANDLER TO FORM
    //DEFINE addCupcake FUNCTION WITH POST REQUEST, APPEND THE RETURNED JSON TO THE LIST
});