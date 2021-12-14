<template>
  <div>
    FOOD COMPONENT
    {{ food_data }}
    <router-view></router-view>
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
