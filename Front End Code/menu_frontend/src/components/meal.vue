<template>
  <div>
    <router-view></router-view>
    MEAL COMPONENT
    <ul>
      <li v-for="data in meal_data" :key="data.id">
        Meal Name : {{ data.meal_name }} <br>
        Public Id: {{ data.public_id }}
        </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      meal_data: [],
    };
  },
  beforeMount() {
    this.$http
      .get(this.$store.getters.url + "/meal/types?t=" + this.$cookie.get("token"))
      .then((data) => {
        console.log(data);
        this.meal_data = data.body;
      });
  },
};
</script>

<style>
</style>
