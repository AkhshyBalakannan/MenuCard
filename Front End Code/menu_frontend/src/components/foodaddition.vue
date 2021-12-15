<template>
  <div>
    FOOD ADDITION COMPONENT
    <input type="text" v-model="food_data.food_name" placeholder="food name" />
    <button @click.prevent="add_food">Add Food</button>
    <form
      class="row g-3 needs-validation"
      novalidate
    >
      <div class="col-md-4">
        <label for="validationCustom01" class="form-label">Food name</label>
        <input
          type="text"
          class="form-control"
          id="validationCustom01"
          v-model="food_data.food_name"
          name="food_data.food_name"
          required
        />
        <div class="valid-feedback">Looks good!</div>
      </div>
      <div class="col-12">
        <button class="btn btn-primary" type="submit" @submit="add_food">Add Food</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      food_data: {
        food_name: "",
      },
      url : ""
    };
  },
  methods: {
    add_food() {
      console.log("entering Function")
      this.$http
        .post(
          this.$store.getters.url +
            "/food/create?t=" +
            this.$cookie.get("token"),
          this.food_data
        )
        .then((data) => {
          console.log(data);
          // this.$router.go();
        });
    },
  }
};
</script>

<style>
</style>

