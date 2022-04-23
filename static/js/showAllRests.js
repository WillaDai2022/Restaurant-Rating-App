
const rest_container = document.querySelector('#listing-grids');
let query_string = ""; // The data from the form to fetch 

const show_all_rests = () => {
  fetch('/get_restaurants.json' + query_string)
  .then(response => response.json())
  .then(responseData => {
    console.log(responseData);
    
    for(const rest of responseData.businesses){
      imgUrl = rest.image_url;
      rest_container.insertAdjacentHTML('beforeend',
      `<div>
        <a href="/rest_details/${rest.id}" >
          <div class="restaurant-box">
            <img src="${imgUrl}"/>
            <div>${rest.alias}</div>
            <div>${rest.price}</div>
          </div>
        </a>
      `)
    };
  });
}

document.querySelector('#home-where-to').addEventListener('submit', (evt)  => {
  evt.preventDefault(); // Prefent the submision of the form
  query_string = `?location=${evt.target.querySelector("input").value}`; // Get the location value from the form
  rest_container.innerHTML = '';
  show_all_rests(); // Fetch the data
});

show_all_rests();