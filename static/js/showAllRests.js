let data = null;


const show_all_rests = () => {
  const rest_container = document.querySelector('#listing-grids');

  fetch('/get_restaurants')
  .then(response => response.json())
  .then(responseData => {
    
    for(const rest of responseData.businesses){
      imgUrl = rest.image_url;
      rest_container.insertAdjacentHTML('beforeend', `<div class="restaurant-info">
        <img src="${imgUrl}"/>
      </div>`)
    };
  });
};

show_all_rests();




fetch('/get_default_restaurants')
  .then(response => response.json())
  .then(responseData => {

     "<div> " 
    data = responseData.businesses;


    document.querySelector('#Listing-grids')
  });