

const show_a_rests = () => {
    const rest_container = document.querySelector('#rest-info');
  
    fetch('/get_restaurants')
    .then(response => response.json())
    .then(responseData => {
  
        data=responseData;
        imgUrl = rest.url;

        rest_container.insertAdjacentHTML('beforeend',
        `<div>
          <a href="/rest_details/${rest.id}">
            <div class="restaurant-info">
              <img src=${imgUrl}/>
              <div>${rest.alias}</div>
              <div>${rest.price}</div>
              <p>What people are saying</p>
            </div>
          </a>
        `);
    });
  }
  
  show_a_rests();
  