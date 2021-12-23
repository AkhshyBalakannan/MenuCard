<template>
  <div>
    <div id="cards_landscape_wrap-2">
      <div class="container">
        <h1>MENUCARD HOME</h1>
        <div class="row">
          <div
            class="col-xs-12 col-sm-6 col-md-3 col-lg-4"
            v-for="data in menu_data"
            :key="data.id"
          >
            <a href="">
              <div class="card-flyer">
                <div class="text-box">
                  <div class="image-box">
                    <!-- <img
                      src="https://cdn.pixabay.com/photo/2018/03/30/15/11/deer-3275594_960_720.jpg"
                      alt=""
                    /> -->
                    <img src="../assets/menucard.png" alt=""/>
                  </div>
                  <div class="text-container">
                    <h6>{{ data.meal_name }}</h6>
                    <div>
                     <!-- <p> PUBLIC_ID = {{ data.public_id }} </p> -->
                      <h6 v-if="data.meal_food[1]" style="margin-top:10px"> 
                        <p class="food_list">Food List</p>
                        <span v-for="(food_data,key,index) of data.meal_food" :key="key">
                          {{food_data}}
                          <span v-if="index != Object.keys(data.meal_food).length - 1">, </span>
                        </span>
                      </h6>
                    </div>
                  </div>                
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu_data: [],
    };
  },
  beforeMount() {
    this.$http.get(this.$store.getters.url + "/meal/all").then((data) => {
      console.log(data);
      this.menu_data = data.body;
    });
  },
};
</script>

<style scoped>
/*----  Main Style  ----*/
#cards_landscape_wrap-2 {
  text-align: center;
  background: #f7f7f7;
}
#cards_landscape_wrap-2 .container {
  padding-top: 80px;
  padding-bottom: 100px;
}
#cards_landscape_wrap-2 a {
  text-decoration: none;
  outline: none;
}
#cards_landscape_wrap-2 .card-flyer {
  border-radius: 5px;
}
#cards_landscape_wrap-2 .card-flyer .image-box {
  background: #ffffff;
  overflow: hidden;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.5);
  border-radius: 5px;
}
#cards_landscape_wrap-2 .card-flyer .image-box img {
  width: 100%;
  height: 200px;
}
#cards_landscape_wrap-2 .card-flyer:hover .image-box img {
  opacity: 0.7;
  -webkit-transform: scale(1.15);
  -moz-transform: scale(1.15);
  -ms-transform: scale(1.15);
  -o-transform: scale(1.15);
  transform: scale(1.15);
}
#cards_landscape_wrap-2 .card-flyer .text-box {
  text-align: center;
}
#cards_landscape_wrap-2 .card-flyer .text-box .text-container {
  padding: 30px 18px;
}
#cards_landscape_wrap-2 .card-flyer {
  background: #ffffff;
  margin-top: 50px;
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
  box-shadow: 0px 3px 4px rgba(0, 0, 0, 0.4);
}
#cards_landscape_wrap-2 .card-flyer:hover {
  background: #fff;
  box-shadow: 0px 15px 26px rgba(0, 0, 0, 0.5);
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
  margin-top: 50px;
}
#cards_landscape_wrap-2 .card-flyer .text-box p {
  margin-top: 10px;
  margin-bottom: 0px;
  padding-bottom: 0px;
  font-size: 14px;
  letter-spacing: 1px;
  color: #000000;
}
#cards_landscape_wrap-2 .card-flyer .text-box h6 {
  margin-top: 0px;
  margin-bottom: 4px;
  font-size: 18px;
  font-weight: bold;
  text-transform: uppercase;
  font-family: "Roboto Black", sans-serif;
  letter-spacing: 1px;
  color: #00acc1;
}
</style>
