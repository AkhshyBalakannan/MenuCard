<template>
  <div>
    FOOD ADDITION COMPONENT
    <input type="text" v-model="food_data.food_name" placeholder="food name" />
    <button @click.prevent="add_food">Add Food</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      food_data: {
        food_name: "",
      },
    };
  },
  methods: {
    add_food() {
      this.$http
        .post(
          this.$store.getters.url +
            "/food/create?t=" +
            this.$cookie.get("token"),
          this.food_data
        )
        .then((data) => {
          console.log(data);
        });
    },
  },
};
</script>

<style>
</style>

