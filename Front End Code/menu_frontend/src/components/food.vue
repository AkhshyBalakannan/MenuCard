<template>
  <div>
     <router-view></router-view>
    FOOD COMPONENT
    <ul>
      <li v-for="data in food_data" :key="data.id">
        Food Name : {{ data.food_name }} <br>
        Public Id: {{ data.public_id }}
        </li>
    </ul>
   
  </div>
</template>

<script>
import store from "../store";
export default {
  data() {
    return {
      food_data: [],
    };
  },
  beforeMount() {
    this.$http
      .get(this.$store.getters.url + "/food/all?t=" + this.$cookie.get("token"))
      .then((data) => {
        console.log(data);
        this.food_data = data.body;
      });
  },
};
</script>

<style>
</style>
