<template>
  <div>
    <router-view></router-view>
    <div class="row mt-3">
      <div class="col"></div>
      <div class="col-6">
        <h3>Meal List</h3>
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Meal Name</th>
              <th scope="col">Public ID</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data in meal_data" :key="data.id">
              <td>{{ data.meal_name }}</td>
              <td>{{ data.public_id }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col"></div>
    </div>
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
    this.$http.get(this.$store.getters.url + "/meal/types").then((data) => {
      this.meal_data = data.body;
    });
  },
};
</script>

<style>
</style>
