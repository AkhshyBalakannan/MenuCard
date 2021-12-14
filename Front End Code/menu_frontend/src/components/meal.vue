<template>
  <div>
    MEAL COMPONENT
    {{ meal_data }}
    <router-view></router-view>
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
