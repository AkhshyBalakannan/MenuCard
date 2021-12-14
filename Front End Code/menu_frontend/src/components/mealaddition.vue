<template>
  <div>
    MEAL ADDITION COMPONENT
    <input type="text" v-model="meal_data.meal_name" placeholder="meal name" />
    <button @click.prevent="add_meal">Add Meal</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      meal_data: {
        meal_name: "",
      },
    };
  },
  methods: {
    add_meal() {
      this.$http
        .post(
          this.$store.getters.url +
            "/meal/create?t=" +
            this.$cookie.get("token"),
          this.meal_data
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
